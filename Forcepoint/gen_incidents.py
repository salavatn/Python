import random
import requests


def get_ipaddress():
    last_octet = random.randint(10, 250)
    ipaddress = "172.30.3."
    return f'IPAddress "{ipaddress}{str(last_octet)}"'


def get_https():
    url_start = "https://www."
    url_region = [".ru/", ".com/", ".org/", ".net/", ".kz/", ".cn/", ".edu/"]
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    data = requests.get(word_site)
    select_word1 = random.randint(10, 1000)
    select_url = random.randint(0, 6)
    word_raw = data.content.splitlines()
    domain1 = str(word_raw[select_word1])[2:-1]
    domain2 = str(url_region[select_url])
    return f'Hostname "{url_start}{domain1}{domain2}"'


def get_hostname():
    last_name = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                 "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
                 "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
                 "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
                 "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"]
    corp_domain = "HQ/"

    rand = random.randint(0, 49)
    return f'Hostname "HQ/D0{str(rand)}-{last_name[rand].upper()}"'


def get_lan():
    last_name = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                 "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
                 "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
                 "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
                 "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"]

    address = get_ipaddress()
    rand = random.randint(0, 49)
    return fr'IPAddress "\\{address[11:-1]}\{last_name[rand].lower()}"'


def get_email():
    last_name = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                     "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
                     "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
                     "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
                     "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"]

    rand = random.randint(0, 49)
    return last_name[rand].lower() + "@hq.org"


def get_printer():
    printer_list = ["HP OfficeJet 4212", "HP OfficeJet 4215", "HP OfficeJet 4215v", "HP OfficeJet 4215xi""HP OfficeJet 4219",
                    "HP OfficeJet 4251", "HP OfficeJet 4252", "HP OfficeJet 4255", "HP OfficeJet 4259", "HP OfficeJet 4300",
                    "HP OfficeJet 4310", "HP OfficeJet 4311""HP OfficeJet 4353", "HP OfficeJet 4355", "HP OfficeJet 4357",
                    "HP OfficeJet 4359", "HP OfficeJet 4360", "HP OfficeJet 4500", "HP OfficeJet 4500 Wireless",
                    "HP OfficeJet 4500w""HP OfficeJet 5508", "HP OfficeJet 5510", "HP OfficeJet 5510v", "HP OfficeJet 5510xi",
                    "HP OfficeJet 5515", "HP OfficeJet 5520", "HP OfficeJet 5600", "HP OfficeJet 5605""HP OfficeJet 5607",
                    "HP OfficeJet 5608", "HP OfficeJet 5609", "HP OfficeJet 5610", "HP OfficeJet 5610v", "HP OfficeJet 5610xi",
                    "HP OfficeJet 5615", "HP OfficeJet 570", "HP OfficeJet 590", "HP OfficeJet 600", "HP OfficeJet 6000", "HP OfficeJet 6000 Wireless"]

    rand = random.randint(0, 35)
    return f'PrinterName "{printer_list[rand]}"'


def get_usb():
    usb_device = ["USB", "USB 2.0", "USB 3.0", "Flash Card", "64 GB", "SD Card", "TS1GCF133", "MAXFLASH 4GB",
                "SanDisk 128 GB", "Transcend 8GB", "SanDisk 512MB", "Extreme PRO 32 GB", "Transend 1GB"]
    rand = random.randint(0, 12)
    return f'DeviceName "{usb_device[rand]}"'


def get_src():
    src = [get_hostname(), get_ipaddress()]
    rand = random.randint(0, 1)
    return src[rand]


def get_channel():
    channel = [16, 17, 18, 19, 21] #, 60, 70, 80]
    num = random.randint(0, 4)
    return channel[num]


def get_file():
    data = [r"C:\docs\partners\contacts.csv",
            r"c:\docs\info.txt",
            r"C:\docs\books\History-of-Rockingha-D--Hamilton--Du.txt",
            r"C:\docs\books\part1.txt",
            r"C:\docs\books\part2.txt",
            r"C:\docs\books\Student-s-cases---il-Philip-Bertie-P.txt",
            r"C:\docs\books\The-complete-works-o-Michael-Drayton.txt"
            ]
    rand = random.randint(0, 6)
    return data[rand]



'''
    16 - Endpoint Removable Media
    17 - Endpoint LAN
18 - Endpoint HTTP
    19 - Endpoint Printing
21 - Endpoint HTTPS
60 - HTTP
70 - HTTPS
80 - FTP
'''

count = 0
while count <= 100:
    count += 1
    timer = random.randint(1, 1000)
    channel = get_channel()

    if channel == 16:
        print(f'PolicyEngineClient.exe -o Test -src {get_src()} -dst {get_usb()} -file {get_file()} -i {channel} & timeout {timer} > NUL  & ', end="")
    elif channel == 17:
        print(f'PolicyEngineClient.exe -o Test -src {get_src()} -dst {get_lan()} -file {get_file()} -i {channel} & timeout {timer} > NUL  & ', end="")
    elif channel == 19:
        print(f'PolicyEngineClient.exe -o Test -src {get_src()} -dst {get_printer()} -file {get_file()} -i {channel} & timeout {timer} > NUL  & ', end="")
    elif channel == (18 or 21):
        print(f'PolicyEngineClient.exe -o Test -src {get_src()} -dst {get_https()} -file {get_file()} -i {channel} & timeout {timer} > NUL  & ', end="")

print("\n Finish")