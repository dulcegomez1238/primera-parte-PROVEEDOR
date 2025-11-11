  # primera-parte-PROVEEDOR


##Parte 1: Creación del Proyecto Django “Farmacia”
1️⃣ Crear carpeta del proyecto

Abre tu explorador de archivos y crea una carpeta llamada:

UIII_Farmacia_0080


O desde terminal (cmd o PowerShell):

mkdir UIII_Farmacia_0080

##2️⃣ Abrir VS Code sobre la carpeta

Abre Visual Studio Code y selecciona:

Archivo → Abrir carpeta → UIII_Farmacia_0080


O desde la terminal:

code UIII_Farmacia_0080

##3️⃣ Abrir terminal en VS Code

En VS Code:

Ver → Terminal


O con el atajo:

Ctrl + ñ

##4️⃣ Crear entorno virtual .venv desde terminal

En la terminal de VS Code:

python -m venv .venv


Esto crea la carpeta del entorno virtual llamada .venv.

##5️⃣ Activar entorno virtual

Windows:

.venv\Scripts\activate


Linux/Mac:

source .venv/bin/activate


Verás algo así en la terminal:

(.venv) C:\Users\TuNombre\UIII_Farmacia_0080>

##6️⃣ Activar intérprete de Python

En VS Code:

Presiona Ctrl + Shift + P

Escribe "Python: Select Interpreter"

Selecciona el que diga:

    .venv\Scripts\python.exe

##7️⃣ Instalar Django

Con el entorno virtual activado:

    pip install django


Puedes verificar:

    django-admin --version

##8️⃣ Crear proyecto Django sin duplicar carpeta

Asegúrate de estar dentro de UIII_Farmacia_0080 y ejecuta:

django-admin startproject backend_Farmacia .


El punto al final evita que se cree una carpeta adicional.

##9️⃣ Ejecutar el servidor en el puerto 0080

    python manage.py runserver 0080

##🔟 Copiar y pegar el link en el navegador

Copia el enlace que aparece en terminal:

    http://127.0.0.1:0080/


Y pégalo en tu navegador.

##Parte 2: Crear aplicación “app_Farmacia”
##11️⃣ Crear aplicación

    python manage.py startapp app_Farmacia

##💾 12️⃣ Agregar modelos en models.py

Copia el código que proporcionaste:

    from django.db import models

# ==========================================
# MODELO: PROVEEDOR
# ==========================================
    class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=100)
    tipo_producto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: PRODUCTO
# ==========================================
    class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=50)
    fecha_caducidad = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return f"{self.nombre} - {self.tipo_producto}"

# ==========================================
# MODELO: INVENTARIO
# ==========================================
    class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventarios')
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='productos/', blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='inventarios')
    fecha_caducidad = models.DateField()
    contenido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

##12.5️⃣ Realizar migraciones

Ejecuta:

    python manage.py makemigrations
    
    python manage.py migrate

##🧮 13️⃣ – 14️⃣ Views para CRUD de Proveedor

    En app_Farmacia/views.py:

    from django.shortcuts import render, redirect, get_object_or_404
    from .models import Proveedor

    def inicio_Farmacia(request):
     return render(request, 'inicio.html')

    def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        correo_electronico = request.POST['correo_electronico']
        tipo_producto = request.POST['tipo_producto']
        Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo_electronico=correo_electronico,
            tipo_producto=tipo_producto
        )
        return redirect('ver_proveedor')
    return render(request, 'proveedor/agregar_proveedor.html')

    def ver_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})

    def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

    def realizar_actualizacion_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.nombre = request.POST['nombre']
        proveedor.direccion = request.POST['direccion']
        proveedor.telefono = request.POST['telefono']
        proveedor.correo_electronico = request.POST['correo_electronico']
        proveedor.tipo_producto = request.POST['tipo_producto']
        proveedor.save()
        return redirect('ver_proveedor')

    def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect('ver_proveedor')


##15️⃣–22️⃣ Templates

##Estructura de carpetas:

app_Farmacia/
│
├── templates/
│   ├── base.html
│   ├── header.html
│   ├── navbar.html
│   ├── footer.html
│   ├── inicio.html
│   └── proveedor/
│       ├── agregar_proveedor.html
│       ├── ver_proveedor.html
│       ├── actualizar_proveedor.html
│       └── borrar_proveedor.html


Incluye Bootstrap y los colores suaves como se pide.
El footer.html debe tener:

    © {{ now|date:"Y" }} Creado por Alumna Dulce_Gomez, CBTis 128


(Usar datetime desde views o el template tag now).


##24️⃣ Crear urls.py en app_Farmacia

app_Farmacia/urls.py:

    from django.urls import path
    from . import views
  
    urlpatterns = [
    path('', views.inicio_Farmacia, name='inicio'),
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('ver_proveedor/', views.ver_proveedor, name='ver_proveedor'),
    path('actualizar_proveedor/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('realizar_actualizacion/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion'),
    path('borrar_proveedor/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),
    ]

##⚙️ 25️⃣ Registrar app en settings.py

   En backend_Farmacia/settings.py, busca INSTALLED_APPS y agrega:

    'app_Farmacia',

##🔗 26️⃣ Configurar URLs principales

  En backend_Farmacia/urls.py:

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_Farmacia.urls')),
    ]

##🗃️ 27️⃣ Registrar modelos en admin.py

En app_Farmacia/admin.py:

    from django.contrib import admin
    from .models import Proveedor, Producto, Inventario

    admin.site.register(Proveedor)
    admin.site.register(Producto)
    admin.site.register(Inventario)


##Y nuevamente ejecuta:

    python manage.py makemigrations
    python manage.py migrate

##🚀 31️⃣ Ejecutar servidor final

    python manage.py runserver 0080


Abre en tu navegador:

    http://127.0.0.1:0080/














