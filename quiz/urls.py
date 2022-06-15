from django.urls import path
from .import views


urlpatterns = [
    path('html/', views.html, name="html"),
    path('css', views.css, name="css"),
    path('js/', views.js, name="js"),
    path('take-test/<int:pk>/<int:sk>', views.take_test,name='take-test'),
    path('start-test/<int:pk>/<int:sk>', views.start_test,name='start-test'),  
    path('feedback/<int:course_id>/<int:level_id>/', views.feedback,name='feedback'),  
]