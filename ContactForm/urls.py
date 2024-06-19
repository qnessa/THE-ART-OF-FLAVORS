from django.urls import path
from . import views

#Custom model urls start here
urlpatterns = [
    path('contactform/', views.contactform, name='contactform'),
   

]
