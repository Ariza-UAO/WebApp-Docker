import os

class Config:
    # Lee las credenciales de la base de datos desde las variables de entorno
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD', 'root')
    MYSQL_DB = os.environ.get('MYSQL_DATABASE', 'myflaskapp')

    # Construye la URI de conexión usando las variables y el driver 'mysql+pymysql'
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@"
        f"{MYSQL_HOST}/{MYSQL_DB}"
    )
