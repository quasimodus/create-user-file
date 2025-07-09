#!/usr/bin/python3
from datetime import datetime
import subprocess


def generate_password():
    """Генерация 12-символьного пароля через pwgen"""
    try:
        result = subprocess.run(
            ["pwgen", "-s", "12", "1"],  # -s для случайных, 12 символов, 1 пароль
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except FileNotFoundError:
        print("Ошибка: pwgen не установлен. Установите его (sudo apt install pwgen / brew install pwgen).")
        exit(1)


def create_user_file():
    print("Введите данные пользователя:")
    last_name = input("Фамилия: ").strip()
    first_name = input("Имя: ").strip()
    username = input("Логин: ").strip()
    birth_date = input("Дата рождения (дд/мм): ").strip()
    place_number = input("Номер места: ").strip()  # Запрашиваем номер места

    password1 = generate_password()
    password2 = generate_password()

    # Гарантируем разные пароли
    while password2 == password1:
        password2 = generate_password()

    current_date = datetime.now()
    date_str = current_date.strftime("%d.%m.%y")  # Для содержимого файла
    filename_date = current_date.strftime("%d%m%y")  # Для имени файла (DDMMYY)

    # Формат имени файла: логин_DDMMYY.txt
    filename = f"{username}_{filename_date}.txt"

    content = f"""\
{date_str}

{place_number}

==========================================================
--------------------------
{last_name} {first_name} ({username})

login:
\t{username}
\t------------

pass:
\t{password1}

pass2:
\t{password2}

===========================================================
e-mail:

\t{username}@yandex.ru
"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nФайл {filename} успешно создан.")
    print(f"Пароль 1: {password1}")
    print(f"Пароль 2: {password2}")


if __name__ == "__main__":
    create_user_file()