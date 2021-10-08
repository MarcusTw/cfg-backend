from django.db import models
from django.db.models import fields
from django.utils import translation
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
)

from education.models import Region, Household, School, EducationLevel

class RegionReadSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "RegionName", "RegionDescription")
class EducationLevelSerializer(ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = ("id", "type_of_education")

class HouseholdReadSerializer(ModelSerializer):
    class Meta:
        model = Household
        fields = ("HouseholdID", "Region", "averageeducationlevel", "HouseholdIncome")
        Region = RegionReadSerializer()
        averageeducationlevel = EducationLevelSerializer()
class HouseholdWriteSerializer(ModelSerializer):
    class Meta:
        model = Household
        fields =  ("HouseholdID", "Region", "averageeducationlevel", "HouseholdIncome")
        Region = PrimaryKeyRelatedField(queryset=Region.objects.all())
        averageeducationlevel = PrimaryKeyRelatedField(queryset=EducationLevel.objects.all())

class SchoolReadSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ("schoolID","Region", "subjectProvided", "numberofTeachers", "attendanceRate", "dropoutRate")
