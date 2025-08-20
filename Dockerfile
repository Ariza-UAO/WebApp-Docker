# Usa una imagen base oficial de Python
FROM python:3.6-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

RUN pip install --upgrade pip

# Copia el archivo de dependencias y las instala
COPY requirements.txt .
RUN pip install --no-warn-script-location -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto en el que la aplicación se ejecuta
EXPOSE 5000

# Comando para ejecutar la aplicación usando Gunicorn
# Se añade --chdir para cambiar al directorio webapp antes de ejecutar
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--chdir", "webapp", "run:app"]
