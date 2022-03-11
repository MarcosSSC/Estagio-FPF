def compute (**kwargs):
    operation = kwargs.get('operacao', '+')
    value1 = kwargs.get('valor1', 0)
    value2 = kwargs.get('valor2', 0 if not operation =='/' else 1)
    return eval(f'{value1} {operation} {value2}')

print(compute(valor1=1, valor2=10, operacao='+'))

parameters = {
    'valor1': 1,
    'valor2': 10,
    'operacao': '+'
}

print(compute(**parameters))