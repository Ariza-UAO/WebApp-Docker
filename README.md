# MiniWebApp
Este es un proyecto de una aplicación web construida con Python y Flask, una base de datos MySQL, y un proxy de Nginx para manejar el tráfico con SSL. Todo el entorno de desarrollo y despliegue se gestiona con Vagrant y Docker.
Estructura del Proyecto
.
├── docker-compose.yml
├── Dockerfile
├── init.sql
├── nginx
│   ├── nginx.conf
│   └── ssl
│       ├── nginx-selfsigned.crt
│       └── nginx-selfsigned.key
├── README.md
├── requirements.txt
├── script.sh
├── Vagrantfile
└── webapp
    ├── config.py
    ├── run.py
    ├── users
    │   ├── controllers
    │   └── models
    └── web
        ├── static
        ├── templates
        └── views.py


# Requisitos Previos
Para ejecutar este proyecto, necesitas tener instalados:
Vagrant
VirtualBox
Docker
# Guía de Inicio
1. Clonar el Repositorio
Abre una terminal y clona este repositorio en tu máquina local.
git clone https://github.com/Ariza-UAO/WebApp-Docker.git
cd WebApp-Docker


2. Levantar el Entorno con Vagrant
Una vez dentro del directorio del proyecto, levanta la máquina virtual con el siguiente comando. Esto instalará y configurará Docker dentro de la VM.
vagrant up


3. Ejecutar el Proyecto con Docker Compose
Una vez que la VM esté en funcionamiento, accede a ella con vagrant ssh y luego, desde el directorio del proyecto dentro de la VM, levanta los servicios de Docker.
vagrant ssh
cd /vagrant # (o la ruta del proyecto si es diferente)
sudo docker compose up --build -d


4. Acceder a la Aplicación
La aplicación estará accesible a través de la dirección IP de la VM.
HTTP: http://localhost:8080 (será redirigido a HTTPS)
HTTPS: https://localhost:8443 (verás una advertencia de seguridad debido al certificado autofirmado)

# Otra Forma
To Run application

Start and SSH into Vagrant VM

```
vagrant up
vagrant ssh servidorWeb
```

Run the webApp

```
cd /home/vagrant/webapp
export FLASK_APP=run.py
/usr/local/bin/flask run --host=0.0.0.0
