# DJANGO


<center>

<img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_django_icon_130645.png" alt="VB." width="200">
</center>



## Manual de instalacion
En este proyecto, se el framework Django rest Framework para la creación de las api del proyecto InvControl se usara las siguientes tecnologias:

- Visual Studio Code
- XAMPP - MYSQL

## Paso previo
Tener instalado Python con anterioridad para poder ejecutar el proyecto es recomendable la ultima version.version de Python 3.x.x
<center>

<img src="https://cdn.icon-icons.com/icons2/112/PNG/512/python_18894.png" alt="VB." width="200">
</center>


## Manual de instalación y configuracion básica del proyecto 

### Paso 1 
Clonar el repositorio https://github.com/Invcontrol-Back/dasbackend
### Paso 2
Ingresar a la carpeta clonada, abrir una terminal
### Paso 3 
Actualizzar las librerias

python -m pip install --upgrade pip
### Paso 4 
Instalar un virtualizador

python -m pip install virtualenv

### Paso 5
Ejecutar el actualizador 

python -m virtualenv venv

### Paso 6
Ejecutar el siguiente comando en Power Shell en modo administrador

Set-ExecutionPolicy RemoteSigned power shell

### Paso 7
Activar el virtualizador 

.\venv\Scripts\activate

### Paso 8 
Instalar la libreria MYSQL de Django

pip install Django mysqlclient 

### paso 9
Istalar Django rest framework

pip install djangorestframework

### paso 10
Istalar 
pip install django-cors-headers

### Paso 11
Configurar los campos de conexion con respecto a sus datos 

#### Paso 11.1 
- Ingresar a la carpeta ServiceInvControl
- Ir al archivo settings.py
- Buscar la configuracion DATABASES
- Realizar los cambios conforme a sus campos


### Paso 12
Migrar los campos que se realizo una sola vez 

python manage.py migrate

### Paso 13
Ejecutar el servidor

python manage.py runserver 


## Anexos
### Archivo Settings.py parte donde se configura la conexión a la base de datos

![Interfaz.](https://github.com/Kevin-Saquinga/ImagenesGit/blob/main/batabase.png?raw=true
)

