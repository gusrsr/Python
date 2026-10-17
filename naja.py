# Bloco 1 ->.Exercícios Python
(
    """""
#1
print("Hello World")
"""
    ""
)

"""""
#2
nome = 'Gustavo'
idade = 17
cidade = 'Uberlândia'
print(f'Meu nome é {nome}.', f'Minha idade é {idade} e', f'moro em {cidade}.')
""" ""
"""""
#3
x = input('Coloque seu NOME: ')
print(f'Olá, {x}!')
""" ""
"""""
#4
x = input('Quantos anos você tem? ')
print(f'Você tem {x} anos.')
""" ""
"""""
#5
a = int(input('Coloque o número A: '))
b = int(input('Coloque o número B: '))
sum = a + b
print(sum)
""" ""
"""""
#6
a = int(input('Coloque o número A: '))
b = int(input('Coloque o número B: '))

sum = a + b
sub = a - b
mult = a * b
div = a / b
print(f'{sum}\n{sub}\n{mult}\n{div}')
""" ""
"""""
#7
a = int(input('Coloque um número: '))
sum = a * 2
print(f'A soma é: {sum}')
""" ""
"""""
#8
a = int(input('Coloque um número: '))
s1 = a * 3
s2 = a / 2

t = f'{s2:.02f}'

print(f'O triplo é: {s1}\nA metade é: {t}')
""" ""
"""""
#9
a = input('Coloque seu nome: ')
b = input('Coloque seu sobrenome: ')

print(f'Seu nome é: {a} {b}')
""" ""
"""""
#10
a = int(input('Ano em que nasceu: '))
sum = 2026 - a
print(f'Sua idade é: {sum}')
""" ""
"""""
#11
a = int(input('Dê a medida de um metro: '))
sC = a * 100
sMm = a * 1000
print(f'As medidas são: {a}M --> {sC}CM e {sMm}MM.')
""" ""
"""""
#12
a = float(input('Dê uma minutagem: ')); sum = a * 60; t = f'{sum:.02f}'; print(f'Seus segundos: {t}')
""" ""
"""""
#13
a = float(input('Dê uma hora: ')); sum = a * 60; t = f'{sum:.02f}'; print(f'Seus minutos: {t}')
""" ""
"""""
#14
a = float(input('Dê uma temperatura em Celsius: ')); sum = a * 9 / 5 + 32; t = f'{sum:.02f}'; print(f'Sua temperatura: {t}°')
""" ""
"""""
#15
a = float(input('Forneça uma quantidade monetária em R$: ')); b = 5; sum = a / b; t = f'{sum:.02f}'; print(f'Equivale a $ {sum}')
""" ""

# Bloco 2

"""""
#16
a = int(input('Digite o lado de um quadrado: '))
sum = a * a
print(f'A área do quadrado é : {sum}')
""" ""
# #17
# a = int(input('Digite o lado de um retangulo: '))
# b = int(input('Digite a altura de um retangulo: '))
# sum = a * b
# print(f'a area e: {sum} ')
# # 18
# a = int(input('Digite a base de um triangulo: '))
# b = int(input('Digite a altura de um triangulo: '))
# sum = a * b
# print(f"a area e: {sum} ")
# # 19
# a = int(input('Digite o raio de um circulo: '))
# pi = 3.14
# sum = (a ** 2) * pi
# t = f'{sum:.2f}'
# print(f'A area e: {t}')
# # 20
# a = int(input('Digite a largura de um retangulo: '))
# b = int(input('Digite a altura de um retangulo: '))
# sum = (b + a) * 2
# print(f'o perimetro do retangulo e: {sum}')
# # 21
# a, b, c = map(int, input('Coloque uma nota: ').split())
# sum = (a + b + c) / 3
# print(f'a media e: {sum}')
# # 22
# a = int(input('Digite quanto ganha por hora: '))
# b = int(input('Digite quantas horas trabalhou: '))
# sum = a * b
# print(f'Salario bruto: {sum}')
# # 23
# a = int(input('Digite seu salario: '))
# s1 = a * 0.10
# s2 = a + s1
# print(f'{a}', f'{s1}', f'{s2}')
# # 24
# a = int(input('Digite o valor de um produto: '))
# s1 = a * 0.15
# s2 = a - s1
# print(s1, s2)
# # 25
# a = int(input('Digite o valor total de uma compra: '))
# b = int(input('Digite quantas parcelas: '))
# sum = a / b
# print(f'{b}x de: {sum} ')
# # 26
# a = int(input('Digite o peso: '))
# b = float(input('Digite a altura: '))
# sum = a / (b ** 2)
# t = f'{sum:.2f}'
# print(f'Seu IMC e: {t}')
# # 27
# a, b = map(int, input('Digite duas notas: ').split())
# s1 = a * 2
# s2 = b * 3
# sum = (s1 + s2) / (a + b)
# print(sum)
# # 28
# a, b = map(int, input('Digite dois numeros: ').split())
# s1 = a // b
# s2 = a % b
# print(f'Quociente: {s1}', f'Resto: {s2}')
# # 29
# a = int(input('Digite um numero: '))
# s1 = a - 1
# s2 = a + 1
# print(s1, a, s2)
# # 30
# a = int(input('Digite uma base: '))
# b = int(input('Digite seu expoente: '))
# sum = a ** b
# print(sum)
# # 31
# a = int(input('Digite um numero: '))
# if a >= 1:
#     print('positivo')
# elif a < 0: 
#     print('negativo')
# elif a == 0:
#     print('= 0')
# # 32
# a = int(input())
# if a > 17:
#     print('maior de idade')
# else:
#     print('menor de idade')
# # 33
# a = int(input())
# if a % 2 == 0:
#     print('par')
# else:
#     print('impar')
# #34
# try:
#     a, b = map(int, input().split())
#     if a > b:
#         print('A maior que B')
#     elif a < b:
#         print('B maior que A')
#     else:
#         print('Numeros iguais')
# except ValueError:
#     print('preenche tudo ai pae')
# else:
#     print('tudo certin')
#35
# a, b, c = map(int, input().split())
# if a > b and c:
#     print('A e maior que os outros valores')
# elif b > c and a:
#     print('B e maior que os outros valores')
# elif c > b and a:
#     print('C e maior que os outros valores')
# 36
# a, b, c = map(int, input().split())
# if a < b and c:
#     print('A e menor que os outros valores')
# elif b < c and a:
#     print('B e menor que os outros valores')
# elif c < b and a:
#     print('C e menor que os outros valores')
# # 37
# a = int(input())
# if a >= 6:
#     print('Aprovado')
# else:
#     print('Reprovado')
# 38
# try:
#     a, b, c = map(int, input().split())
#     sum = (a + b + c) / 3
#     if sum >= 7:
#         print('Aprovado')
#     elif sum >= 5 and sum < 7:
#         print('Recuperacao')
#     else:
#         print('Reprovado')
# except ValueError:
#     print('Preencha corretamente')
# else:
#     print('Tente no proximo ano!')
# # 39
# a = int(input())
# if a <= 11:
#     print('Criança')
# elif a <= 17:
#     print('Adolescente')
# elif a <= 59:
#     print('Adulto')
# else:
#     print('Idoso')
# 40
# a = int(input())
# if a == 1234:
#     print('Senha correta! Pode entrar!')
# else:
#     print('Tente novamente!')
# # 41
# a = input()
# b = int(input())
#
# name = "gugu"
# passwd = 1234
#
# if a and b == name and passwd:
#     print('logou com sucesso!')
# else:
#     print('tente novamente!')
#   42
# a = int(input())
# if a % 5 == 0:
#     print('boa!')
# else:
#     print('Tente novamente!')
#   43
# a = int(input())
# if a % 3 == 0 and a % 5 == 0:
#     print('boa')
# else:
#     print('tente novamente')
# 44
# a = int(input())
# if a % 4 == 0:
#     print('bissexto')
# else:
#     print('tente novamente')
# 45
# a = int(input())
# if a >= 200:
#     sum = a * 10 / 100
#     sum2 = a - sum
#     print(sum2)
# else:
#     print(a)
# 46
# a, b = map(int, input().split())
# if a >= 150:
#     b = 0
#     print(f"Preco da compra: {a}, Frete: {b}")
# else:
#     sum = b + 20
#     print(f"Preco da compra: {a}, Frete: {sum}")
# 47
# try:
#     c = input()
#     a, b = map(int, input().split())
#     s1 = a + b
#     s2 = a - b
#     s3 = a * b
#     s4 = a / b
#     if c == "+":
#         print(s1)
#     elif c == "-":
#         print(s2)
#     elif c == "*":
#         print(s3)
#     elif c == "/":
#         print(s4)  
# except ValueError:
#     print('preenche tudo ae')
# except ZeroDivisionError:
#     print('SEM 0 NA DIVISAO')
# else:
#     print('boa!')
# 48
# a, b, c = map(int, input().split())
# if a < (b + c) and b < (a + c) and c < (b + a):
#     print('certo')
# else:
#     print('deu nao pae')
# 49
# a, b, c = map(int, input().split())
# if a < (b + c) and b < (a + c) and c < (b + a):
#     if a == b and b == c:
#         print('equilatero')
#     elif a == b or a == c or b == c:
#         print('isosceles')
#     else:
#         print('escaleno')
# else:
#     print('deu nao pae')
# 50
# a = float(input())
# s1 = a * 10 / 100
# s2 = a * 20 / 100
# s3 = a - s1
# s4 = a - s2
#
# if a < 2000.1:
#     print(f'Valor = R${a}, Taxa = 0')
# elif a <= 4000:
#     print(f'Valor = R${s3}, Taxa = {s1}')
# elif a > 4000:
#     print(f'Valor = R${s4}, Taxa = {s2}')
# 51
# for numero in range(1, 11):
#     print(numero)
# # 52
# for a in range(10, -1, - 1):
#     print(a)
# print('Fim!')
# 53
# a = int(input())
# for a in range(0, 100, 2):
#     print(a)
# 54
# for a in range(1, 101, 2):
#     print(a)
# 55
# a = int(input())
# b = 0
# for b in range(1, 11):
#     sum = a * b
#     print(f'{a} x {b} = {sum}')
# 56
# n = int(input())
# soma = 0
# for i in range(1, n+ 1):
#     soma = soma + i
# print(soma)
# 57
# n = int(input())
# ft = 1
# for i in range(1, n +1):
#     ft = ft * i 
#     print(ft)
# 58
# b = 0
# for i in range(1, 11):
#     a = int(input())
#     if a % 2 == 0:
#         b += 1
# print(b)   
# 59
# sum = 0
# b = 0
# for i in range (1,11):
#     a = int(input())
#     if a > 0:
#         b += 1
#         sum = sum + a
#
# print(b, sum)
# 60
# numeros = list(map(int, input().split()))
# maior = numeros[0]
# for i in range(0, 5):
#     if numeros[i] > maior:
#         maior = numeros[i]
#         print(f'Este {maior}!')
#     else:
#         print('menor')
# print(maior)
# 61
# numeros = list(map(int, input().split()))
# menor = numeros[0]
# for i in range(5):
#     if numeros[i] < menor:
#         menor = numeros[i]
#         print(f'Este {menor}!')
#     else:
#         print('Maior')
# print(menor)
# 62
# notas = list(map(int, input().split()))
# cal = 0
# for i in range(5):
#     cal += notas[i]
#     div = cal / 5 
# print(cal, div)
# 63
# senha = input()
# while senha != 'bestfriends4ever':
#     print('Tente novamente!')
#     senha = input()
# else:
#     print('Senha Correta! Entrando...')
# 64
# numero = int(input())
# while numero <= 0:
#     print('Digite um numero positivo!')
#     numero = int(input())
# else:
#     print(f'Voce digitou um numero positivo! \n{numero}')
# 65
# n = int(input('Digite um numero: '))
# while n != 0:
#     print(' Digite 1 para dizer Ola. \n Digite 2 para mostrar uma mensagem. \n Digite 0 para sair.') 
#     if n == 1:
#         print('Parabens! Escolheu 1! --> Ola')
#     elif n == 2:
#         print('Parabens! Escolheu 2! --> Uma mensagem')
#     n = int(input())
# else:
#     print('Feito!')
# 66
# n = int(input())
# sum = 0
# while n != 0:
#     print('Digite um numero: ')
#     sum += n
#     n = int(input())
# else:
#     print(f'Feito! Sua soma e: {sum}')
# 67
# n = int(input())
# sum = 0
# calc = 0
# while n != -1:
#     print('Digite um numero: ')
#     sum += n
#     calc = sum / n
#     n = int(input())
# else:
#     print(f' Suas notas: {sum}. \n Sua media: {calc}')
# 68
# n = int(input('Tente acertar o numero: '))
# while n != 19: 
#     if n <= 5:
#         print('Precisa de um numero maior.')
#     elif n <= 9:
#         print('Numero pequeno.')
#     elif n <= 12:
#         print('Ta chegando perto.')
#     elif n <= 15:
#         print('To gostando da resiliencia.')
#     elif n <= 17:
#         print('Ta MUITO perto.')
#     elif n > 19 and n < 30:
#         print('Agora ta longe.')
#     elif n <= 30:
#         print('Mds, mt longe, esquece bro.')
#     elif n == 18:
#         print('Que isso? do lado?')
#     n = int(input())
# else:
#     print('Acertou o numero!')
# 69
# n = int(input())
# ct = 0
# for i in range(2, n):
#     if n % i == 0:
#         ct += 1
# if ct > 0:
#     print('Numero nao primo!')
# elif n == 1:
#     print('1 Nao vale!')
# else:
#     print('Numero primo!')
# 70
# a, b = map(int, input().split())
# ct = 0
# tc = 0
# for i in range(a + 1, b):
#     if a and b % i == 0:
#         ct += 1
#     else:
#         tc = i
# if ct > 0:
#     print('Nao tem primos')
# elif ct == 0:
#     print(tc)
# 71
# a = input()
# b = len(a)
# print(f'A palavra {a} possui {b} caracteres.')
# 72
# a = input()
# b = a.upper()
# c = a.lower()
# print(f'A frase {a}. \nMaiusculo. {b} \n \b Minusculo. {c}')
# 73
# a = input()
# b = a[0]
# c = a[-1]
# if a == " ":
#     print('Digite uma palavra!')
# else:
#     d = a[0].upper()
#     print(f'A palavra: {a}. \n Primeira letra: {d} \n Ultima letra: {c}')
# 74
# a = input()
# b = a.count('a')
# print(f'Quantas vezes a letra A apareceu: {b}')
# 75
# a = input()
# b = a[::-1]
# if b == a:
#     print(f'Ela pode ser lida de tras pra frente')
# else:
#     print('Nao pode ser lida.')
# 76
# a = input()
# b = a[::-1]
# print(f'O input fatiado \n {b[2:]} \n {b[:3]}')
# 77
# a = list(input().split())
# for i in range(0, len(a)):
#     print(a[i])
# 78
# a = list(input().split())
# print(len(a))
# 79
# a = input()
# print(f'A frase: {a}') 
# b = input('Palavra a substituir: ')
# r = a.replace("Hoje",b)
# print(r)
# 80
# a = input('Digite um endereço de e-mail: ')
# novoTexto = a.split('@')
# if '.' in novoTexto[1]:
#     print('contem . apos o @')
# 81
# a = list(input().split())
# for i in range(len(a)):
#     print(a[i])
# 82
# a = []
# for i in range(6):
#     nome = input()
#     a.append(nome)
# print(a)
# 83
# a = list(map(int, input().split()))
# b = 0
# for i in range(len(a)):
#     b += a[i]
# print(b)
# 84
# a = list(map(int, input().split()))
# b = a[0]
# for i in range(len(a)):
#     if a[i] > b:
#         b = a[i]
# print(b)
# 85
# a = list(map(int, input().split()))
# b = a[0]
# for i in range(len(a)):
#     if a[i] < b:
#         b = a[i]
# print(b)
# 86
# a = list(map(int, input().split()))
# cal2 = 0
# for i in range(len(a)): 
#     cal2 += a[i] 
# print(cal2 / len(a))
# 87
# numeros = list(map(int, input().split()))
# pares = []
# for i in range(len(numeros)):
#     if numeros[i] % 2 == 0:
#         pares.append(numeros[i])
# print(pares)
# 88
# nomes = list(input().split())
# for i in range(1):
#     nome = input('Digite um nome para retirar: ') 
#     if nome in nomes:
#         nomes.remove(nome)
# print(nomes)
# 89
# a = list(input().split())
# for i in range(len(a)):
#     produto = input('Pesquise por um produto: ')
#     if produto in a:
#         print(f'Produto encontrado! \n {produto}')
# 90
# a = list(map(int, input().split()))
# for i in range(1):
#     a.sort()
#     print(a)
#     a.sort(reverse=True)
#     print(a)
# 91
# a = set(map(int, input().split()))
# print(a)
# 92
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(a & b)
# 93
# a = tuple(map(int, input().split()))
# x = a[0]
# y = a[1]
# print(f'X: {x}, Y: {y}')
# 94
# pessoa = {}
# pessoa['nome'] = input('Digite seu nome: ')
# pessoa['idade'] = input('Digite sua idade: ')
# pessoa['cidade'] = input('Digite sua cidade: ')
# print(f'Seu nome: {pessoa['nome']} \nSua idade: {pessoa['idade']} \nSua cidade: {pessoa['cidade']}')
# 95
# aluno = {}
# aluno['nome'] = input('Digite seu nome: ')
# aluno['nota1'] = int(input('Digite sua primeira nota: '))
# aluno['nota2'] = int(input('Digite sua segunda nota: '))
# cal = (aluno['nota1'] + aluno['nota2']) / 2
# aluno.update({'media': {cal}})
# print(aluno)
# 96
# p1 = {}
# p2 = {}
# p3 = {}
# lista = [p1, p2, p3]
# for i in lista:
#     i['nome'] = input('Digite o nome do produto: ')
#     i['preco'] = input('Digite o preco do produto: ')
#     for nome, preco in i.items():
#         print(nome, preco)
# 97
