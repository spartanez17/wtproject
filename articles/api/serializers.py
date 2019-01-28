from rest_framework import serializers
# from articles.models import Article, Weather


class EnumField(serializers.ChoiceField):
    def __init__(self, enum, **kwargs):
        self.enum = enum
        kwargs['choices'] = [(e.name, e.name) for e in enum]
        super(EnumField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return obj.name

    def to_internal_value(self, data):
        try:
            return self.enum[data]
        except KeyError:
            self.fail('invalid_choice', input=data)


class WeatherSerializer(serializers.Serializer):
    query = serializers.IntegerField()
    KELVIN = 'KELVIN'
    CELSIUS = 'CELSIUS'
    FAHRENHEIT = 'FAHRENHEIT'
    UNITS = (
        (KELVIN, 'kelvin'),
        (CELSIUS, 'celsius'),
        (FAHRENHEIT, 'fahrenheit'),
    )
    units = serializers.CharField(
        max_length=2,
        choices=UNITS,
        default=CELSIUS
    )
