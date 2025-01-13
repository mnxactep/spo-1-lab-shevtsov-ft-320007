import random
import string
import hashlib

def generate_password(length):
    harakteristiki = string.ascii_letters + string.digits + '%#-&$'
    password = ''.join(random.choice(harakteristiki) for i in range(length))
    return password

def save_passwords_to_file(passwords):
    with open('passwords.txt', 'w') as file:
        for password in passwords:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            file.write(hashed_password + '\n')

def main():
    dlina = int(input("Введите длину пароля(ей): "))
    kolichestvo = int(input("Введите нужное количество паролей: "))

    passwords = [generate_password(dlina) for _ in range(kolichestvo)]

    print("Сгенерированные пароли: ")
    for password in passwords:
        print(password)

    save_passwords_to_file(passwords)
    print('Пароли сохранены в файл "passwords.txt" ')

if __name__ == "__main__":
    main()
