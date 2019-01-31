# from django.core.management.base import BaseCommand, CommandError
# from articles.models import Question as Poll
# from articles.services.weather_service import WeatherService


# class Command(BaseCommand):
#     help = 'fetch weather'

#     # def add_arguments(self, parser):
#     #     parser.add_argument('poll_id', nargs='+', type=int)

#     def handle(self, *args, **options):
#         for poll_id in options['city']:

#             poll.opened = False
#             poll.save()

#             self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))