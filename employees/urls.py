from django.urls import path

from employees import views

urlpatterns = [
	path('<int:pk>/', views.employee_details, name='employee_detail')
]
