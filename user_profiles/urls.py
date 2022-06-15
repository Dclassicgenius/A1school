from django.urls import path
from .import views

urlpatterns = [

    path('user_dashboard_view/', views.user_dashboard_view, name="user_dashboard_view"),
    path('quiz_playground/', views.quiz_playground, name="quiz_playground"),
    path('user_marks_view/', views.user_marks_view, name="user_marks_view"),
    path('check_marks/<int:pk>/<int:sk>/', views.check_marks_view,name='check_marks'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

]