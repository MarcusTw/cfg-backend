from django.db import models

# Create your models here.

class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    RegionName = models.CharField(max_length=200)
    RegionDescription = models.CharField(max_length=200)

class EducationLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    type_of_education = models.CharField(max_length=100)


class Household(models.Model):
    Region = models.ForeignKey(Region, on_delete=models.CASCADE)
    HouseholdID = models.IntegerField(primary_key=True)
    averageeducationlevel = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, related_name="education_level")
    HouseholdIncome = models.IntegerField(null = True)


class School(models.Model):
    Region = models.ForeignKey(Region, on_delete=models.CASCADE)
    schoolID = models.IntegerField(primary_key=True)
    subjectProvided = models.CharField(max_length=200)
    numberofTeachers = models.IntegerField(null = True)
    attendanceRate = models.FloatField(null = True)
    dropoutRate = models.FloatField(null = True)




