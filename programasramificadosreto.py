print('\t Compara tu edad')

user1_Name = input('Ingresa tu nombre: ')
user1_Age = int(input(f'Cual es tu edad {user1_Name}? '))

user2_Name = input('Ingresa el nombre de tu amigo: ')
user2_Age = int(input(f'Cual es la edad de {user2_Name}? '))

if user1_Age > user2_Age:
	print(f'{user1_Name} es mayor que {user2_Name}')
elif user1_Age < user2_Age:
	print(f'{user2_Name} es mayor que {user1_Name}')
else:
	print(f'{user1_Name} y {user2_Name} ambos tienen {user1_Age} años')
