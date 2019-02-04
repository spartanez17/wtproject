from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import gettext_lazy as _
from articles.api.serializers import WeatherQuerySerializer
from articles.services.weather_service import WeatherService


def validate_city_query(value):
    if not isinstance(value, str) or 2 > len(value) > 40:
        raise ValidationError(
            _('%(value)s is not valid'),
            params={'city_query': value},
        )


class Command(BaseCommand):
    help = 'cache weather'
    q_serializer = WeatherQuerySerializer
    weather_service = WeatherService()

    def add_arguments(self, parser):
        parser.add_argument('city_query', nargs='+', type=str)

    def handle(self, *args, **options):
        for city_query in options['city_query']:
            try:
                validate_city_query(value=city_query)
            except ValidationError:
                raise CommandError('City "%s" does not exist' % city_query)

            self.weather_service.get_weather(
                query=city_query, exp_period_min=10)

            self.stdout.write(self.style.SUCCESS(
                'Successfully fetched weather "%s"' % city_query))
            # f = open('fetch_weather.log', 'a+')
            # f.write('Successfully fetched weather "%s"' % city_query + '\n')
            # f.close()
