from ConstructorOTP import OTPGenerator
import pyotp


secret_key = pyotp.random_base32()
otp = OTPGenerator(secret_key=secret_key, account_name='Notes', issuer_name='NS-Lab Ltd.')


TOTP    = otp.genTOTP()
QRcode  = otp.genQRCode()
Token   = otp.genToken()
Verify  = otp.verifyToken(Token)


print(f'TOTP: {TOTP}')
print(f'QRcode: {QRcode}')
print(f'\nToken: {Token}\n')
print(f'Verify: {Verify}')

