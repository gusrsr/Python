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
#     sum = a + b + c / 3
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
# 41
