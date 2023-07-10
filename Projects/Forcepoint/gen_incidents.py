from faker import Faker
import random
import argparse

fake = Faker()

# Service Name and ID:
service = {
    "USB": 16, "LAN": 17,
    "HTTP": 18, "HTTPS": 19,
    "Printer": 20}
service_name = list(service.keys())
service_id = list(service.values())

# PolicyEngineClient.exe -o Test -src IPAddress '10.39.66.227' -dst EmailAddress 'buchananjennifer@schwartz-freeman.net' -file C:\tmp\1.txt -i 20

# Arguments:
parser = argparse.ArgumentParser(description='\tGenerate incidents')
parser.add_argument('--src', type=str, help='Source IP address')
parser.add_argument('--dst', type=str, help='Destination IP address')
parser.add_argument('--sid', type=int, help='Service ID', choices=service_name)
parser.add_argument('--cnt', type=int, help='Number of incidents')
args = parser.parse_args()


def random_src():
    return random.choice([
        f"IPAddress '{fake.ipv4_private()}'",
        f"Hostname '{fake.hostname()}'",
        f"EmailAddress '{fake.company_email()}'",
        f"UserName '{fake.name()}'",
    ])


def random_dst(svc_Name):
    internal_ip   = f"IPAddress '{fake.ipv4_private()}'"
    external_ip   = f"IPAddress '{fake.ipv4_public()}'"
    url           = f"URL '{fake.url()}'"
    hostname      = f"Hostname '{fake.hostname()}'"
    company_email = f"EmailAddress '{fake.company_email()}'"
    user_name     = f"UserName '{fake.name()}'"
    usb_device    = f"DeviceName '{fake.user_name()}'"
    lan_device    = f"IPAddress '{hostname}/{usb_device}'"

    if svc_Name == "USB":    return usb_device
    if svc_Name == "LAN":    return random.choice([lan_device, hostname, internal_ip])
    if svc_Name == "HTTP":   return random.choice([url, hostname, external_ip])
    if svc_Name == "HTTPS":  return random.choice([url, hostname, external_ip])
    if svc_Name == "Printer":return random.choice([internal_ip, hostname, company_email, user_name])

src     = args.src
dest    = args.dst
svcName = args.sid
cnt     = args.cnt or 10


if svcName == None and src == None and dest == None:
    for i in range(cnt):
        svc_ID   = service[random.choice(service_name)]
        svc_Name = service_name[service_id.index(svc_ID)]
        src = random_src()
        dest = random_dst(svc_Name)
        print(fr"PolicyEngineClient.exe -o Test -src {src} -dst {dest} -file C:\tmp\1.txt -i {svc_ID}")

'''
# IPAddress
# Hostname
# EmailAddress
# URL
# Domain
# UserName
# DeviceName
# PrinterName
# UserSID
# ApplicationID
# Subnet
# IPRange
# PrimaryEmail
# MailServer
# Category
# UserDN
# GeoLocation
'''