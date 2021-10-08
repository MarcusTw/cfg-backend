from typing import DefaultDict, List

import csv, io, json
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny, BasePermission

from django.db import IntegrityError


from education.serializers import (
    RegionReadSerializer,
    HouseholdReadSerializer,
    SchoolReadSerializer
)
from education.models import Region, Household, School, EducationLevel



class RegionViewSet(GenericViewSet, ListModelMixin):
    queryset = Region.objects.all()
    serializer_class = RegionReadSerializer

class HouseHoldPermission(BasePermission):

    def has_permission(self, request, view):

        return True
    
    def has_object_permission(self, request, view, obj):

        return True

class HouseHoldViewSet(ModelViewSet):
    queryset = Household.objects.all()
    serializer_class = HouseholdReadSerializer
    permission_classes = [HouseHoldPermission]
 
    def get_queryset(self):
        print("i m here")
        queryset = super().get_queryset()
        print(queryset)
        return queryset 

    @action(detail=False, methods=["GET"],url_path="get-all-households")
    def get_all_households(
        self,
        request,
        pk=None
    ):
        data = HouseholdReadSerializer(Household.objects.all(), many=True)
        return Response(
            data=data.data,
            status=status.HTTP_200_OK
        )
    


    @action(detail=False, methods=["POST"], url_path="upload-household-csv")
    def add_household_record(
        self,
        request,
        pk=None
    ):
        data =  request.body.decode('utf-8')
        households = json.loads(data)
        for household in households:
            if len(household) == 3:
                new_household = Household(
                    Region=Region.objects.get(id=int(household["Region"])),
                    averageeducationlevel = EducationLevel.objects.get(id=int(household["educationLevel"])),
                    HouseholdIncome = int(household["householdIncome"].replace('\r', '').replace('\\r', ""))
                )
                new_household.save()
       
        return Response(
            status=status.HTTP_200_OK
        )


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolReadSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    #def create(self, request, *args, **kwargs):

    @action(detail=False, methods=["POST"], url_path="upload-school-csv")
    def upload_school_csv(
        self,
        request,
        pk=None
    ):
        data =  request.body.decode('utf-8')
        schools = json.loads(data)
        for school in schools:
            mySchool = {}
            for k in school:
                mySchool[k.replace('\r', '').replace('\\r', "")] = school[k].replace('\r', '').replace('\\r', "");
            if (len(mySchool) == 5): # invalid data
                print(mySchool)
                subjectProv = mySchool["subjectsProvided"].split(" ")
                subjectProv = "".join(subjectProv)
                new_school = School(
                    Region=Region.objects.get(id=int(mySchool["Region"])),
                    subjectProvided=subjectProv,
                    numberofTeachers=int(mySchool["numberofTeachers"]),
                    attendanceRate=float(mySchool["attendanceRate"]),
                    dropoutRate=float(mySchool['dropoutRate'])
                )
                new_school.save()
        return Response(
            status=status.HTTP_200_OK
        )

    

















