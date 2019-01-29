from rest_framework import serializers
from enum import Enum


# class Units(Enum):
#     KELVIN = 'kelvin',
#     CELSIUS = 'celsius',
#     FAHRENHEIT = 'fahrenheit'


# class EnumField(serializers.ChoiceField):
#     def __init__(self, enum, **kwargs):
#         self.enum = enum
#         kwargs['choices'] = [(e.name, e.name) for e in enum]
#         super(EnumField, self).__init__(**kwargs)

#     def to_representation(self, obj):
#         return obj.name

#     def to_internal_value(self, data):
#         try:
#             return self.enum[data]
#         except KeyError:
#             self.fail('invalid_choice', input=data)


# class WeatherQuerySerializer(serializers.Serializer):
#     query = serializers.CharField(required=True, max_length=20, min_length=3)
#     units = EnumField(enum=Units)
#     # units = EnumChoiceField(enum_class=UnitsTypes)
