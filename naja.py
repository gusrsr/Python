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
# p1 = {}
# p2 = {}
# p3 = {}
# lista = [p1, p2, p3]
# maior = 0
# for i in lista:
#     i['nome'] = input('Insira o nome do produto: ')
#     i['preco'] = int(input('Insira o preco do produto: '))
#     maior = p1['preco']
#     if i['preco'] > maior:
#         maior = i['nome'], i['preco']
#     else:
#         maior = p1['nome'], p1['preco']
# print(maior)
# 98
# p1 = {}
# agenda = [p1]
# c = False
# for i in agenda:
#     for a in range(3):
#         nome = input('Digite um nome: ') 
#         i[nome] = input('Digite um telefone: ')
# b = input('Digite um nome para buscar um telefone: ')
# for i in agenda:
#     for nome, nomeValue in i.items():
#         if b == nome:
#             c = True
#             print(nome, nomeValue) 
# if c == False:
#     print('Nome nao existe!')
# 99
# p1 = {}
# frase = input().split()
# conj = set(frase)
# for i in conj:
#     qnt = frase.count(i)
#     p1[i] = qnt
# print(p1)
# 100
# p1 = {}
# n = False
# for i in range(5):
#     produto = input('Digite o nome do produto: ')
#     p1[produto] = int(input('Digite o valor do produto: '))
# print(p1)
# b = input('Procure um produto: ')
# for produto, produtoValue in p1.items():
#     if b == produto:
#         n = True
#         print(f'{produto}.')
#         c = int(input('Qual a quantidade que deseja retirar: '))
#         calc = produtoValue - c
#         if calc < 0:
#             print('Numero negativo!')
#         else:
#             print(calc)
# if n == False:
#     print('Produto nao encontrado!')
# 101
# def saudacao():
#     print('oi')
# saudacao()
# 102
# def saudacao(nome):
#     print(f'Ola, {nome}')
# saudacao('Gustavo!')
#103
# def sumo(a, b):
#     resultado = a + b
#     return resultado
# somar = sumo(1, 2)
# print(somar)
# 104
# def maior(a, b):
#     if b > a:
#         print('B maior que A')
#     else:
#         print('A maior que B')
# c, d = input().split()
# calc = maior(c, d)
# print(calc)
# 105
# def evens(a):
#     if a % 2 == 0:
#         print('par')
#     else:
#         print('impar')
# calc = evens(1)
# print(evens)
# 106
# a, b, c = map(int, input().split())
# def media(a, b, c):
#     cal1 = a + b + c     
#     cal2 = cal1 / 3
#     return cal2
# mediaRE = media(a, b, c)
# print(mediaRE)
# 107
# s = list(map(int, input().split()))
# calc = 0
# def cal(s):
#     print(s)
#     calc = s[0] * s[1]
#     return calc
# calk = cal(s)
# print(f'A area do retangulo e: {calk}')
# 108
# s = int(input())
# def graus(s):
#     calc = (s * 9 / 5) + 32
#     return calc
# calk = graus(s)
# print(f'Fahrenheit: {calk}')
# 109
# a = int(input())
# b = 1
# def fatorial(a, b):
#     for i in range(1, a +1):
#         b *= i
#     return b
# cal = fatorial(a, b)
# print(cal)
# 110
# n = int(input())
# def primo(n):
#     b = False
#     for i in range(2, n):
#         if n % i == 0:
#             b = False
#             break
#         else:
#             b = True
#     if b == True:
#         print('numero Primo!')
#     else:
#         print('numero nao Primo ou Invalido!')
#     return b
# cal = primo(n)
# print(cal)
# 111
# a = input()
# def vogal(a):
#     total = 0
#     b = ['a', 'e', 'i', 'o', 'u']
#     for i in b:
#         if i in a:
#             total += a.count(i)
#     return total
#     print(total)
# cal = vogal(a)
# print(cal)
# 112
# a = [1, 3, 9, 10, 304, -203, 89, 43]
# def maior(a):
#     b = a[0]
#     for i in a:
#         if i > b:
#             b = i
#     print(b)
# cal = maior(a)
# print(cal)
# 113
# a = list(map(int, input().split()))
# def media(a):
#     o = 0
#     c = 0
#     cal = 0
#     for i in range(len(a)):
#         o += i
#         c = i + i
#     cal = c / o
#     print(cal)
# cal = media(a)
# print(cal)
# 114
# a = [1, -34, 5, -10 , 67, 19, -209]
# def positivo(a):
#     novaLista = []
#     for i in a:
#         if i > 0:
#             novaLista.append(i)
#     print(novaLista)
# cal = positivo(a)
# print(cal)
# 115
# def soma():
#     a, b = map(int, input('Digite numeros para a soma: ').split())
#     a = a + b
#     print(a)
# def sub():
#     a, b = map(int, input('Digite numeros para a subtracao: ').split())
#     a = a - b
#     print(a)
# def mult():
#     a, b = map(int, input('Digite numeros para a multiplicacao: ').split())
#     a = a * b
#     print(a)
# def div():
#     a, b = map(int, input('Digite numeros para a divisao: ').split())
#     a = a / b
#     print(a)
# try:
#     cal = 0
#     a = int(input('Calculadora em PythoN! \nDigite de 1-4 para as opcoes: \n1 == SOMA\n2 == SUBTRACAO\n3 == MULTIPLICACAO\n4 == DIVISAO\n'))
#     match a:
#         case 1:
#             cal = soma()
#         case 2:
#             cal = sub()
#         case 3:
#             cal = mult()
#         case 4:
#             cal = div()
# except ValueError:
#     print('Digite os 2 valores mané!')
from pathlib import Path

# import calculos

caminho = Path(__file__).parent / 'texto.txt'
caminho2 = Path(__file__).parent / 'teste.txt'
# 116
# a = input('Digite texto para colocar em um arquivo: ')

# with open(caminho, 'w', encoding='utf-8') as arquivo:
#     arquivo.write(a)
# 117
# a = input('Bem vindo ao Programa de registro de Nomes!\nDigite 1 para registrar nomes em um arquivo txt.\nDigite s para sair do programa!\n')
# if a == '1':
#     with open(caminho, 'w', encoding='utf-8') as arquivo:
#         pass
#     while True:
#         texto = input('')
#         if texto == 's':
#             break
#         with open(caminho, 'a', encoding='utf-8') as arquivo:
#                 arquivo.write(texto + '\n')
# 118
# a = input('Digita uns nome ae: ')
# with open(caminho, 'w+', encoding='utf-8') as arquivo:
#     arquivo.write(a + '\n')
#     arquivo.seek(0)
#     print(arquivo.readline())
# 119
# with open(caminho, 'r', encoding='utf-8') as arquivo:
#     for i in arquivo:
#         a = i.strip()
#         print(a)
# 120
# with open(caminho2, 'r') as arquivo:
#     print(sum(1 for i in arquivo)) ##essa parte eu tava perguntando pra AI uma forma de  usar uma variavel antes de declarar ela em python(declarando e usando ela em uma operacao ao mesmo tempo.) e ai ele mostrou como contar as linhas, achei interessante e coloquei. NAO ME CRUCIFIQUE RAFAEL!!1111!!1!!1##
# 121
# try:
#     a = int(input('Envie valores inteiros: '))
#     print(f'Valor Aceito!\n--> {a}')
# except ValueError:
#     print('VALOR INCORRETO!')
# 122
# try:
#     a, b = map(int,input('Digite 2 numeros inteiros: ').split())
#     cal = a / b
#     print(cal)
# except ValueError:
#     print('Digite numeros!')
# except ZeroDivisionError:
#     print('Digite valores maiores que 0')
# 123
#outros arquivos
# print(calculos.soma(3, 2))
# 124 e 125
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def __str__(self): 
#         return f'Nome: {self.nome} Tem: {self.idade} anos.\n'
#
# pessoa1 = Pessoa('Gustavo', 17)
# pessoa2 = Pessoa('Danielle', 43)
# print(pessoa1, pessoa2)
# 126
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
#     def apresentar(self):
#         return print(f'Ola {self.nome}!')
# pessoa1 = Pessoa('Gustavo')
# pessoa1.apresentar()
# 127
# class Produto:
#     def __init__(self, nome, preco): 
#         self.nome = nome
#         self.preco = preco
#     def __repr__(self): 
#         return f'Nome={self.nome}, Preco={self.preco}'
# produto1 = Produto('Cacho de Banana', 2)
# produto2 = Produto('Tomate', 1)
# produto3 = Produto('Cebola', 1)
# print(produto1, produto2, produto3, sep='\n')
# 128
# class Produto:
#     def __init__(self, nome, preco): 
#         self.nome = nome
#         self.preco = preco
#     def aplicar_desconto(self, percentual):
#         desconto = (self.preco * percentual) / 100
#         novoPreco = self.preco - desconto
#         self.preco = novoPreco
#         return f'Nome={self.nome}, Preco={self.preco}'
# produto1 = Produto('Cacho de Banana', 10)
# produto2 = Produto('Tomate', 15)
# produto3 = Produto('Cebola', 18)
# print(produto1.aplicar_desconto(2), produto2.aplicar_desconto(2), produto3.aplicar_desconto(2), sep='\n')
# 129
# class contaBanco:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#     def __str__(self):
#         return f'{self.titular}, Bem vindo a sua conta Bancaria! Seu saldo: {self.saldo}. '
#     def depositar(self, valor):
#         self.saldo += valor
#     def sacar(self, valor):
#         self.saldo -= valor
# conta1 = contaBanco('Gustavo', 300)
# print(conta1)
# a = int(input('Digite 1 para depositar e 2 para sacar: '))
# match a:
#     case 1:
#         b = int(input('Digite o valor do deposito: '))
#         contaBanco.depositar(conta1, b)
#         print(conta1)
#     case 2:
#         b = int(input('Digite o valor para sacar: '))
#         contaBanco.sacar(conta1, b)
#         print(conta1)
#         if conta1.saldo < 0:
#             print('Saldos negativos sao invalidos!')
# 130 e 131
# notas = [7.5, 8.0, 9.5, 6.0, 10.0]
# class Aluno:
#     def __init__(self, nome, notas):
#         self.nome = nome
#         self.notas = notas
#     def media(self):
#         cal = sum(notas) / len(notas)
#         cal2 = float(f'{cal:.2f}')
#         return cal2
#     def __str__(self):
#         return f'Nome={self.nome}, Notas={self.notas}'
#     def situacao(self):
#         if aluno1.media() >= 6:
#             return 'Aprovado!'
#         else:
#             return 'Reprovado!'
#
# aluno1 = Aluno('Gustavo', notas)
# print(aluno1,aluno1.media(), aluno1.situacao())
# 132
# class Retangulo:
#     def __init__(self, largura, altura): 
#         self.largura = largura
#         self.altura = altura
#     def area(self):
#         c = self.largura * self.altura
#         return c
#     def perimetro(self):
#         c = 2 * (self.largura + self.altura)
#         return c
# retangulo1 = Retangulo(10, 5)
# print(retangulo1.area(), retangulo1.perimetro())
# 133
# class Carro:
#     def __init__(self, modelo, velocidade_atual, velocidade_maxima):
#         self.modelo = modelo
#         self.velocidade_atual = velocidade_atual
#         self.velocidade_maxima = velocidade_maxima
#     def __str__(self): 
#         return f'Modelo={self.modelo}, Velocidade Atual={self.velocidade_atual}, Velocidade Maxima={self.velocidade_maxima}'
#     def acelerar(self, valor):
#         self.velocidade_atual += valor
#     def frear(self, valor):
#         self.velocidade_atual -= valor
# carro1 = Carro('Ford', 50, 100)
# print(f'O Carro {carro1}')
# b = int(input('Digite 1 para acelerar e 2 para frear: '))
# match b:
#     case 1:
#         c = int(input('Digite quanto voce quer acelerar: '))
#         if c <= carro1.velocidade_maxima and c > 0:
#             carro1.acelerar(c)
#             print(carro1)
#         else:
#             print('Nao pode ultrapassar a velocidade maxima!')
#     case 2:
#         c = int(input('Digite o quanto voce quer frear: '))
#         if c <= carro1.velocidade_maxima and c > 0:
#             carro1.frear(c)
#             print(carro1)
#         else:
#             print('Nao pode ultrapassar a velocidade maxima!') 
# 134
class Livro: ##FRITADOR DE CEREBRO 3000
    def __init__(self, titulo, autor, disponivel, id):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
        self.id = id
class Biblioteca:
    def __init__(self):
        self.livros = []
    def adicionar(self, Livro):
        self.livros.append(Livro)
    def visualizar(self):
        for i in self.livros:
            print(i.titulo, i.autor, i.disponivel, i.id)
    def emprestar(self, i):
        self.livros[i].disponivel = 'Nao'
    def devolver(self, i):
        self.livros[i].disponivel = 'Sim'
biblioteca = Biblioteca()
livro1 = Livro('O Auto da compadecida', 'Ariano Suassuna', 'Sim', 0)
livro2 = Livro('Meridiano de sangue', 'Cormac McCarthy', 'Sim', 1)
biblioteca.adicionar(livro1)
biblioteca.adicionar(livro2)
try:
    while True:
        a = int(input('Digite 0 para sair\n1 para visualizar os itens\n2 para emprestar um livro\n3 para devolver o livro\n: '))
        match a:
            case 0:
                break
            case 1:
                biblioteca.visualizar()
                continue
            case 2:
                a = int(input('Digite o id do livro que queira pegar: '))
                biblioteca.emprestar(a)
                continue
            case 3:
                b = int(input('Digite o id do livro que queira devolver: '))
                biblioteca.devolver(b)
                continue
            case _:
                print('Digite os numeros corretos!')
except ValueError:
    print('Pinando no texto ne but')
