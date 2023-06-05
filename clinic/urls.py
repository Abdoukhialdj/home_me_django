# from django.urls import path
# from .views import MedicalPractitionerListCreateView,UserCreateView, MedicalPractitionerRetrieveUpdateDestroyView,CustomTokenCreateView

# urlpatterns = [
#     path('medical-practitioners/', MedicalPractitionerListCreateView.as_view(), name='medical-practitioner-list-create'),
#     path('medical-practitioners/<int:pk>/', MedicalPractitionerRetrieveUpdateDestroyView.as_view(), name='medical-practitioner-retrieve-update-destroy'),
    
#     #  path('patients/', PatientListCreateView.as_view(), name='patients-list-create'),
#     # path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patients-retrieve-update-destroy'),
    
#     path('api/signup/',UserCreateView.as_view()),
#     path('api/login/',CustomTokenCreateView.as_view())
# ]


from django.urls import  path
from .views import  RegisterView,LoginView,UserView,LogoutView,ReportListView, ReportDetailView
from . import views




urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(),name='login'),
    path('user/', UserView.as_view(),name='user'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('doctorappointments/', views.DoctorAppointmentList.as_view()),
    path('doctorappointments/<int:pk>/', views.DoctorAppointmentDetail.as_view()),
    path('nurseappointments/', views.NurseAppointmentList.as_view()),
    path('nurseappointments/<int:pk>/', views.NurseAppointmentDetail.as_view()),
    path('reports/', ReportListView.as_view(), name='report-list'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    

]
