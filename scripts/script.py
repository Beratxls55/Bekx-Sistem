import requests
from bs4 import BeautifulSoup
import sys

def get_m3u8_link():
    url = "https://www.tv8.com.tr/canli-yayin"  # Burayı kendi URL'inle değiştir

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print("Sayfaya erişim hatası:", e)
        sys.exit(1)

    if response.status_code != 200:
        print("Sayfa çekilemedi, durum kodu:", response.status_code)
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")

    # Burayı sayfadaki gerçek yapıya göre güncelle
    source_tag = soup.find("source", {"type": "application/x-mpegURL"})
    if source_tag is None:
        print("M3U8 linki bulunamadı.")
        sys.exit(1)

    m3u8_link = source_tag.get("src")
    if not m3u8_link:
        print("M3U8 link src'si boş.")
        sys.exit(1)

    return m3u8_link

def save_link_to_file(link):
    with open("current.m3u8", "w") as f:
        f.write(link)

if __name__ == "__main__":
    link = get_m3u8_link()
    print("Bulunan link:", link)
    save_link_to_file(link)
