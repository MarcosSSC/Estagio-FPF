import psycopg2

try:
        connection = psycopg2.connect("dbname='aulas' user='postgres' host='localhost' password='123456' port='5432'")
        print('Conexão bem suscedida')

except Exception:
        print('Conexão falhou')

curs = connection.cursor()

def list_employees():
    curs.execute('select * from employees')
    result = curs.fetchall()
    return print(result)

def save_employees(id, name, salary, gender):
    curs.execute('insert into employees(id, name, salary, gender) values(%s, %s, %s, %s)', (id, name, salary, gender))
    connection.commit()

op = int(input('1: Adicionar pessoas \n2: Listar funcionáios \n3: Sair \nEscolha sua opção: '))

while op!=3:
    if op == 1:
        id = int(input('Insira uma identificação para esse funcionário: '))
        name = input('Digite o nome do funcionário: ')
        salary = float(input('Salário do funcionário: '))
        gender = input('Gênero do funcionário: ')
        save_employees(id, name, salary, gender)

    elif op == 2:
        list_employees()

    elif op ==3:
        print('Conexão encerrada')
        connection.close()

    else:
        print('Opção inválida')

    op = int(input('1: Adicionar pessoas \n2: Listar funcionáios \n3: Sair \nEscolha sua opção: '))