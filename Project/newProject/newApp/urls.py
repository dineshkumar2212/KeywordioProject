from django.urls import path,include
from newApp import views

urlpatterns = [
    path('student/',views.StudentListView.as_view()),

]
