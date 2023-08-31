import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, 'w') as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/india/india-lodges-strong-protest-over-chinas-standard-map-says-such-steps-only-complicate-resolution-of-boundary-question-pm-modi-s-jaishankar-china-map/articleshow/103180070.cms"

r=requests.get(url)
print(r.text)

fetchAndSaveToFile(url, "data/times.html")
