import colorama
from colorama import init
init()
from colorama import Fore
from interface import a
from faker import Faker
import random
import string
from nickname_generator import generate

fake = Faker("ru_RU")

print(Fore.RED + a)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

people = f"""
ФИО: {fake.name_male()}
Номер телефона: {fake.phone_number()}
Работа: {fake.job()}
Адрес: {fake.address()}"""

card = f"""
{fake.credit_card_full()}"""

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())

b = input('\n[+]. Выбери: ')

if b == '1':
    print(Fore.RED + people)
elif b == '2':
    print(Fore.RED + card)
elif b == '3':
    password_length = int(input(Fore.RED + "Длина пароля: "))
    generated_password = generate_password(password_length)
    print(Fore.RED + "Сгенерированный пароль:", generated_password)
elif b == '4':
    print(Fore.RED + generate())