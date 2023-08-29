import http.cookiejar
import urllib.request
import requests
import bs4

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

urllib.request.install_opener(opener)

# authentication_url = "https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100"
# authentication_url = "https://m.facebook.com/login.php"
authentication_url = "https://m.facebook.com//login/device-based/login/async/?refsrc=deprecated&lwv=100"
payload = {
    'email':"rohan.matre11@gmail.com",
        'pass':"Rohan@123"
}

data = urllib.parse.urlencode(payload).encode('utf8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
content = resp.read()
print(content)

url = "https://m.facebook.com/100081575311061/friends?_rdr"
data = requests.get(url, cookies=cj)

soup = bs4.BeautifulSoup(data.text, 'html.parser')
# print(soup.prettify())

z=0
for i in soup.find_all('a'):
    # print(i.get('href'))
    if z>16:
        print(i.text)
    z=z+1    
