from generator import OTP
import pyotp



key = pyotp.random_base32()
otp = OTP()

token = otp.getToken(key)
print(token)

verify = otp.verifyToken(token, key)
print(verify)
