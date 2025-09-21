print("Введите пароль:")

password = input()

if len(password) < 16:
    print("Слишком короткий")
elif password.isalpha() or password.isdigit():
    print("Слабый пароль")
else:
    print("Надежный пароль")