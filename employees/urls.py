from django.urls import path

from employees import views

urlpatterns = [
	path('add/', views.employee_form, name='employee_insert'),
	path('<int:id>/', views.employee_form, name='employee_update'),
	path('delete/<int:id>/', views.employee_delete, name='employee_delete'),

	path('details/<int:pk>/', views.employee_details, name='employee_detail')
]
