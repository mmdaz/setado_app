import os


class DbConfig:
    db_user = os.environ.get('POSTGRES_USER', "postgres")
    db_password = os.environ.get('POSTGRES_PASSWORD', "123456")
    db_host = os.environ.get('POSTGRES_HOST', "localhost")
    db_name = os.environ.get('POSTGRES_DB', "sitado_db")
    db_port = os.environ.get('POSTGRES_PORT', "5432")
    database_url = "postgresql://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name)