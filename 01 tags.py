# Beautiful Soup Docs - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# THIS DOCS is very important for web scraping & easily understand
import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc = f.read()

# important line    
soup = BeautifulSoup(html_doc, "html.parser")
# print the sample html file
# print(soup.prettify())
# print(soup.title,type(soup.title))
# print(soup.title.string)
# print(soup.title.name)
# print(soup.div)
# print(soup.find_all("div")[0])
# print(soup.find_all("div")[1])
# print(type(soup.find_all("div")[1]))

# for link in soup.find_all("a"):
#     # print(link)
#     print(link.get("href"))
#     print(link.get_text())
    

# s = soup.find(id="link3")
# print(s)
# print(s.href) # --> None return
# print(s.get("href")) # --> return the link

# Advance BS4
# print(soup.select("div.italic"))
# print(soup.select("span#italic"))
# print(soup.span.get("class"))


# print(soup.find(id="italic"))
# print(soup.find(class_="italic"))
# print(soup.find_all(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)
#     print(child.text)

# parent-child Concept
# i=0
# for parent in soup.find(class_="box").parents:
#     i+=1
#     print(parent)
#     if(i==2):
#         break

# Modified the HTML file
# cont = soup.find(class_="container")
# cont.name = "span"
# cont["class"] = "myclass class2"
# cont.string = "I am a string"
# print(cont)


# step-1 : tag ko prepare karna hai
# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "About"
# ulTag.append(liTag)


# soup.html.body.insert(0,ulTag)
# with open("modified.html","w") as f:
#     f.write(str(soup))


# cont = soup.find(class_="container")
# print(cont.has_attr("id"))
# print(cont.has_attr("class"))
# print(cont.has_attr("contenteditable"))

def has_class_but_no_id(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")

# results = soup.find_all(has_class_but_no_id)
results = soup.find_all(has_content)
for result in results:
    print(result,"\n\n")













