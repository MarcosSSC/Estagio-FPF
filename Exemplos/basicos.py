name = "Marcos"
surname = "Castro"
fullname = name + " de " + surname

birth = int(input("Qual seu ano de nascimento? "))
today = int(input("Em que ano estamos? "))
age = today - birth

fsize = float(input("Qual era sua altura ano passado? "))
grow = float(input("Quantos metros você cresceu? "))
csize = fsize + grow

print("Seu nome é ", fullname)
print("Sua idade é: ", age, "anos")
print("Você mede atualmente ", csize, "metros")