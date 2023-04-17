import pyotp
import qrcode
import time

# # Создание объекта PyOTP с помощью секретного ключа, полученного от Google Authenticator.
# # Этот секретный ключ можно найти в настройках приложения Google Authenticator.
# totp = pyotp.TOTP('secret_key_from_google_authenticator')

# # Генерация одноразового токена на основе текущего времени.
# token = totp.now()

# # Ожидание 30 секунд и генерация нового токена.
# time.sleep(10)
# token = totp.now()

# # Печать сгенерированного токена.
# print(token)




# Генерация секретного ключа для аккаунта.
# Этот ключ должен быть сохранен на сервере и использоваться для проверки одноразовых токенов, генерируемых приложением Google Authenticator.
secret_key = pyotp.random_base32()

# Формирование информации об аккаунте.
account_name = 'Notes App'  # Название приложения или сервиса.
issuer_name = 'NS Lab'  # Название организации, предоставляющей приложение или сервис.
otp_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(account_name, issuer_name=issuer_name)

# Генерация QR-кода.
img = qrcode.make(otp_uri)

# Сохранение QR-кода в файле.
img.save('qr_code.png')



# Создание объекта PyOTP с помощью секретного ключа, полученного от Google Authenticator.
# Этот секретный ключ можно найти в настройках приложения Google Authenticator.
totp = pyotp.TOTP(secret_key)

# Генерация одноразового токена на основе текущего времени.
token = totp.now()

# Ожидание 30 секунд и генерация нового токена.
time.sleep(60)
token = totp.now()

# Печать сгенерированного токена.
print(token)

# Проверка токена.
print(totp.verify(token))

user_token = input('Enter token: ')

# Проверка токена с помощью метода verify().
print(totp.verify(user_token))

# Проверка токена с помощью метода verify().
print(totp.verify(user_token, valid_window=1))