from rest_framework import serializers
from .models import Student1
class StudnetSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student1
        fields=['id','stuname','email']