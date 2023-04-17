import pyotp
import qrcode
import time


class OTPGenerator:
    def __init__(self, secret_key, account_name, issuer_name):
        self.secret_key   = secret_key
        self.account_name = account_name
        self.issuer_name  = issuer_name

    def genTOTP(self):
        return pyotp.TOTP(self.secret_key, interval=60)

    def genQRCode(self):
        otp_uri = pyotp.totp.TOTP(self.secret_key).provisioning_uri(self.account_name, issuer_name=self.issuer_name)
        img     = qrcode.make(otp_uri)
        return img
        # img.save('qr_code.png')

    def genToken(self):
        totp = pyotp.TOTP(self.secret_key)
        return totp.now()

    def verifyToken(self, token):
        totp = pyotp.TOTP(self.secret_key)
        return totp.verify(token)

'''
1. Пользователь регистрируется в системе.
2. Генерируется секретный ключ.
3. Генерирует QR-код с помощью секретного ключа.
4. Пользователь сканирует QR-код с помощью приложения Google Authenticator.
5. Пользователь получает одноразовый токен JWT.
6. Пользователь отправляет одноразовый токен JWT вместе с запросом на сервер.
7. Сервер проверяет одноразовый токен JWT и выполняет запрос.

    # Generate OTP 
    # Generate JWT
    # Verify JWT
'''
