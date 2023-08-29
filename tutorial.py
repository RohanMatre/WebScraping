import bs4
import requests

url = "https://dev.to/digvijayjadhav98/code-documentation-a-guide-for-beginners-4cj7"
data = requests.get(url)

soup = bs4.BeautifulSoup(data.text, 'html.parser')
# print(soup.prettify) 

# for para in soup.find('p'): --> only 1st p paragraph
for para in soup.find_all('p'):
    print(para)
    # print(para.text)

# to get all link in that page
# for links in soup.find_all('a'):
#     link = links.get('href')
#     # print(link.get('href'))
#     if link[0:3] == "../" and link!="#":
#         print("https://dev.to"+link[2:len(link)])
#     elif link[0] == "/" and link!="#":
#         print("https://dev.to"+link)
#     elif link!="#":
#         print(link)

# url2 = "https://www.youtube.com/@SonySAB/playlists"

# data = requests.get(url2)
# soup = bs4.BeautifulSoup(data.text, 'html.parser')

# for link in soup.find_all('a'):
#     link = link.get('href')
#     if link[0:3] == "/wa":
#         print("https://www.youtube.com"+link)
    # elif link!="#":
    #     print(link)


