from generator import OTP
from dotenv import load_dotenv
import pyotp 
import os


load_dotenv(dotenv_path='.env')
app_name      = os.getenv('OTP_APP_NAME')
company_name  = os.getenv('OTP_COMPANY_NAME')
time_interval = os.getenv('OTP_TIME_INTERVAL')


folder_name   = (f'{app_name}').replace(' ', '')
if not os.path.exists(folder_name):
    os.mkdir(folder_name)


key = pyotp.random_base32()
otp = OTP(
    secret_key=key, 
    account_name=app_name, 
    issuer_name=company_name,
    time_interval=time_interval
    )


# totp    = otp.genTOTP(key, time_interval)
qr_code = otp.genQRcode(key, app_name, company_name)
qr_code.save(f'{folder_name}/QR_Code.png')

token   = otp.getToken()
verify  = otp.verifyToken(token)


# print(f'TOTP: {totp}')
# print(f'QRcode: {qr_code}')
# print(f'\nToken: {token}\n')
# print(f'Verify: {verify}')






