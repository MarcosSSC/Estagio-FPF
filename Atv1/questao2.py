word = str(input('Digite uma palavra: '))
vowels = 0
consoants = 0

for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels = vowels + 1
    else:
        consoants = consoants + 1

print(f'A palavra tem {vowels} vogais e {consoants} consoantes')