from rest_framework import serializers

from .models import *

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('id','name', 'birth_year', 'eye_color')

