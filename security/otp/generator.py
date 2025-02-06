import pyotp
import qrcode


class OTP:
    def __init__(self):
        pass

    def genQRcode(self, key, account, issuer) -> qrcode:
        otp_uri = pyotp.totp.TOTP(key).provisioning_uri(account, issuer)
        qr_code = qrcode.make(otp_uri)
        return qr_code

    def getToken(self, key: str):
        totp = pyotp.TOTP(s=key)
        return totp.now()

    def verifyToken(self, token, key):
        totp = pyotp.TOTP(key)
        return totp.verify(token)
