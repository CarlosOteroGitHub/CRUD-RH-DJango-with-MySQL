from django.urls import path
from . import views

#Direccionamiento de rutas al archivo de vistas de la aplicación RH (views.py).
urlpatterns = [
	path('', views.inicio, name='inicio'),
	path('nosotros', views.nosotros, name='nosotros'),
	path('empleados', views.empleados, name='empleados'),
	path('empleado/crear', views.crear_empleado, name='crear_empleado'),
	path('insertarEmpleado/', views.insertarEmpleado, name='insertarEmpleado'),
	path('empleado/editar/<id_empleado>', views.editar_empleado, name='editar_empleado'),
	path('actualizarEmpleado/', views.actualizarEmpleado, name='actualizarEmpleado'),
	path('eliminarEmpleado/<id_empleado>', views.eliminarEmpleado, name='eliminarEmpleado'),
]