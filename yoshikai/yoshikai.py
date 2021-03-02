import requests
from bs4 import BeautifulSoup

def ja():
    return get("https://yoshikai.net")

def en():
    return get("https://yoshikai.net/en")

def get(site_url):
    html = requests.get(site_url)
    soup = BeautifulSoup(html.text, "html.parser")
    works = soup.find_all("div", {"class": "work" })
    result = []
    for work in works:
        work_title = work.find("span", {"class": "work-title"}).get_text()
        work_detail = work.find("p", {"class": "work-detail"}).get_text().split("\n")[2].strip()
        url = work.find("a")["href"]
        result.append({
            "title": work_title,
            "detail": work_detail,
            "url": url,
        })
    return result

