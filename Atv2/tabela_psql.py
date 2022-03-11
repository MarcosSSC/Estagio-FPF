import psycopg2

def employees (**kwargs):
    id = kwargs.get('id')
    name = kwargs.get('nome')
    sex = kwargs.get('sexo')
    salary = kwargs.get('salário')

try:
    connection = psycopg2.connect("dbname='aulas' user='postgres' host='localhost' password='123456' port='5432'")
    print('Conexão bem suscedida')
    connection.close()


except Exception:
    print('Conexão falhou')
