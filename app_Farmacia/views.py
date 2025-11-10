from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor

# Página principal
def inicio_Farmacia(request):
    return render(request, 'inicio.html')

# Agregar proveedor
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        tipo = request.POST['tipo_producto']
        Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo_electronico=correo,
            tipo_producto=tipo
        )
        return redirect('ver_proveedor')
    return render(request, 'proveedor/agregar_proveedor.html')

# Ver proveedores
def ver_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})

# Editar proveedor
def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.direccion = request.POST['direccion']
        proveedor.telefono = request.POST['telefono']
        proveedor.correo_electronico = request.POST['correo']
        proveedor.tipo_producto = request.POST['tipo_producto']
        proveedor.save()
        return redirect('ver_proveedor')

# Borrar proveedor
def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})
