from django.urls import path
from .import views


urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('admin_question_view/', views.admin_question_view, name="admin_question_view"),
    path('admin_view_question_view/', views.admin_view_question_view, name="admin_view_question_view"),
    path('admin_user_view/', views.admin_user_view, name="admin_user_view"),
    path('admin_update_user/<int:pk>/', views.admin_update_user, name="admin_update_user"),
    path('admin_delete_user/<int:pk>/', views.admin_delete_user, name="admin_delete_user"),

    path('admin_view_user_view/', views.admin_view_user_view, name="admin_view_user_view"),
    path('admin_view_user_marks_view/', views.admin_view_user_marks_view, name="admin_view_user_marks_view"),
    path('admin_view_marks_view/<str:pk>/', views.admin_view_marks_view, name="admin_view_marks_view"),
    path('admin_check_marks_view/<str:pk>/<str:sk>/', views.admin_check_marks_view, name="admin_check_marks_view"),
    path('admin_add_questions/', views.admin_add_questions, name="admin_add_questions"),

    path('view_question_view/<int:pk>/<int:sk>/', views.view_question_view, name="view_question_view"),

    path('delete_question_view/<int:pk>/', views.delete_question_view, name="delete_question_view"),
    path('update_question/<int:pk>/', views.update_question, name="update_question"),

    path('playground/', views.playground, name="playground"),
    path('admin_quiz', views.admin_quiz, name="admin_quiz"),
]