from rest_framework import serializers
from todayapp1.models import student



class studentdata(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


