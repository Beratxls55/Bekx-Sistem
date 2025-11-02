import requests
from bs4 import BeautifulSoup

def get_m3u8_link():
    url = "https://www.tv8.com.tr/canli-yayin"  # Buraya linki yaz

    response = requests.get(url)
    if response.status_code != 200:
        print("Sayfa çekilemedi:", response.status_code)
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Örnek: sayfadaki <source> etiketi içindeki src değerini alıyoruz
    source_tag = soup.find("source", {"type": "application/x-mpegURL"})
    if source_tag:
        return source_tag.get("src")

    return None

def save_link_to_file(link):
    with open("current.m3u8", "w") as f:
        f.write(link)

if __name__ == "__main__":
    link = get_m3u8_link()
    if link:
        print("Bulunan link:", link)
        save_link_to_file(link)
    else:
        print("Link bulunamadı.")
