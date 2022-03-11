add = lambda parameter_a, parameter_b : parameter_a + parameter_b

def add_then_multiply(a, b, multiplier):
    return add(parameter_a=a, parameter_b=b) * multiplier

print(add_then_multiply(10, 20, 2))