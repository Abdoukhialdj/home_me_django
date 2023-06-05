# from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import  User,Report,DoctorAppointment, NurseAppointment,Report


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'role',
            'phone_number',
            'address',
            'gender',
            'password',]
        
        extra_kwargs = {
            'password': {'write_only':True}}
        #set role as patient only
        


from .models import DoctorAppointment, NurseAppointment

class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAppointment
        fields = ['id', 'patient', 'appointment_time', 'is_completed']

class NurseAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseAppointment
        fields = ['id', 'patient', 'appointment_time', 'is_completed']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'title', 'body', 'created_at', 'updated_at', 'author']




