import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithharry.com/my-gear/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc, "html.parser")

product_names = soup.find_all(
    "h2",
    class_="title-font mt-5 text-xl font-medium text-gray-900 dark:text-gray-100"
)

links = soup.find_all(
    "a",
    class_="my-1 mr-2 inline-flex w-fit cursor-pointer items-center rounded-full bg-purple-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-lg transition ease-in-out hover:scale-105 hover:bg-purple-800"
)

for index, (product_name, link) in enumerate(zip(product_names, links), start=1):
    current_link = (link.get("href"))
    with open("product.html", "a") as f:
        f.write(f"{index}.{product_name.text.strip()} - {current_link}" + "\n")
