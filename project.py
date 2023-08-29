import bs4
import requests
from transformers import pipeline

url = "https://www.york.ac.uk/teaching/cws/wws/webpage1.html"
data = requests.get(url)

soup = bs4.BeautifulSoup(data.text, 'html.parser')

# Initialize the paraphrasing pipeline
paraphraser = pipeline("text2text-generation", model="t5-small", tokenizer="t5-small")

for para in soup.find_all('p'):
    original_text = para.get_text(strip=True)
    paraphrased_text = paraphraser(original_text, max_length=50, num_return_sequences=1)[0]['generated_text']
    print("Original:", original_text)
    print("Paraphrased:", paraphrased_text)
    print()

# Rest of your code for extracting links remains the same
