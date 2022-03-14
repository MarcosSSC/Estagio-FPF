archive = open('/home/marcos/Documents/Estágio/Projetos/Aulas1/exemplo.txt', 'w+')
archive.write('Meu primeiro arquivo')
archive.close()

archive = open('/home/marcos/Documents/Estágio/Projetos/Aulas1/exemplo.txt', 'a')
content = archive.write('\nSegunda linha do arquivo')
archive.close()

#archive = open('/home/marcos/Documents/Estágio/Projetos/Aulas1/exemplo.txt', 'r')
#lines = archive.readlines()
#for l in lines:
#    print(l)
#archive.close()

#with open('/home/marcos/Documents/Estágio/Projetos/Aulas1/exemplo.txt', 'r') as archive:
#  lines = archive.readlines()
#  for l in lines:
#     print(l)

archive = open('/home/marcos/Documents/Estágio/Projetos/Aulas1/exemplo.txt', 'r')
content = archive.read()
print(content)
archive.close()