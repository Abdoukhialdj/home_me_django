from rest_framework.views import APIView
from django.db import models
from .serializers import UserSerializer,DoctorAppointmentSerializer, NurseAppointmentSerializer,ReportSerializer
from rest_framework.response import  Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User,DoctorAppointment, NurseAppointment,Report
from rest_framework import generics
#status
from rest_framework import status



from rest_framework.exceptions import AuthenticationFailed


#token
import jwt, datetime



class RegisterView (ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
class LoginView (APIView):
    authentication_classes = []
    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role')

        
        
        user = User.objects.filter(email = email, role = role).first()
        
        if user is None :
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrct Password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)
        
        response.data = {
           'user': user.id,
            'jwt': token
        }
        
        return response
    
    
class UserView(APIView):

    
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        
        return Response(serializer.data)
    

class LogoutView(APIView):
    
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        
        return response


class DoctorAppointmentList(generics.ListCreateAPIView):
    queryset = DoctorAppointment.objects.all()
    serializer_class = DoctorAppointmentSerializer

class DoctorAppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorAppointment.objects.all()
    serializer_class = DoctorAppointmentSerializer

class NurseAppointmentList(generics.ListCreateAPIView):
    queryset = NurseAppointment.objects.all()
    serializer_class = NurseAppointmentSerializer

class NurseAppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NurseAppointment.objects.all()
    serializer_class = NurseAppointmentSerializer

class ReportListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer