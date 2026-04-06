import time
import random

correct_username = "admin"
correct_password = "1234"

ip_attempts = {}
max_attempts = 5

def generate_ip():
    return f"192.168.1.{random.randint(1, 255)}"

while True:
    ip = generate_ip()
    print(f"Bağlanan IP: {ip}")

    username = input("Kullanıcı adı: ")
    password = input("Şifre: ")

    if ip not in ip_attempts:
        ip_attempts[ip] = 0

    if ip_attempts[ip] >= max_attempts:
        print("Bu IP engellendi!")
        continue

    if username == correct_username and password == correct_password:
        print("Giriş başarılı!")
        break
    else:
        ip_attempts[ip] += 1
        print(f"Hatalı giriş! {ip} için deneme: {ip_attempts[ip]}")

        time.sleep(ip_attempts[ip])