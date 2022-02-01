from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Empleado
from django.contrib import messages

#Función para direccionar a la pagina de inicio.
def inicio(request):
	return render(request, 'paginas/inicio.html')

#Función para direccionar a la pagina de nosotros.
def nosotros(request):
	return render(request, 'paginas/nosotros.html')

#Función para direccionar a la pagina de index de la aplicación RH, incluyendo el listado de todos los empleados desde la base de datos.
def empleados(request):
	empleados_listado = Empleado.objects.all()
	messages.success(request, '¡Empleados listados!')
	return render(request, 'empleado/index.html', {'empleados': empleados_listado})

#Función para direccionar a la pagina de crear de la aplicación empleado.
def crear_empleado(request):
	return render(request, 'empleado/crear.html')

#Función para insertar un registro a la tabla empleado en la base de datos.
def insertarEmpleado(request):
	nombre=request.POST['nombre']
	nacimiento=request.POST['nacimiento']
	correo=request.POST['correo']
	descripcion=request.POST['descripcion']
	empleado = Empleado.objects.create(nombre=nombre, nacimiento=nacimiento, correo=correo, descripcion=descripcion)

	messages.success(request, '¡Empleado Agregado!')

	return redirect('/')

#Función para direccionar a la pagina de editar de la aplicación empleado.
def editar_empleado(request, id_empleado):
	empleado = Empleado.objects.get(id_empleado=id_empleado)
	return render(request, 'empleado/editar.html', {"empleado": empleado})

#Función para actualizar un registro a la tabla empleado en la base de datos.
def actualizarEmpleado(request):
	id_empleado=request.POST['id_empleado']
	nombre=request.POST['nombre']
	nacimiento=request.POST['nacimiento']
	correo=request.POST['correo']
	descripcion=request.POST['descripcion']

	empleado = Empleado.objects.get(id_empleado=id_empleado)
	empleado.id_empleado = id_empleado
	empleado.nombre = nombre
	empleado.nacimiento = nacimiento
	empleado.correo = correo
	empleado.descripcion = descripcion
	empleado.save()

	messages.success(request, '¡Empleado Editado!')

	return redirect('/')

#Función para eliminar un registro a la tabla empleado en la base de datos.
def eliminarEmpleado(request, id_empleado):
	empleado = Empleado.objects.get(id_empleado=id_empleado)
	empleado.delete()

	messages.success(request, '¡Empleado Eliminado!')

	return redirect('/')