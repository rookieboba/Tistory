import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://sungbin-park.tistory.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
START = 1
END = 150
OUTPUT_FILE = "tistory_export.txt"

def extract_article(url):
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    title_tag = soup.select_one("h1.tit")
    article_tag = soup.select_one("#article")

    title = title_tag.get_text(strip=True) if title_tag else "제목 없음"
    content = article_tag.get_text(strip=True) if article_tag else "내용 없음"

    return f"■ {title}\n{url}\n{content}\n\n"

def main():
    print(f"🔍 총 {END}개의 글을 수집합니다...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i in range(START, END + 1):
            url = f"{BASE_URL}/{i}"
            print(f"[{i}] 수집 중: {url}")
            try:
                article = extract_article(url)
                f.write(article)
            except Exception as e:
                print(f"⚠️ [{i}] 오류 발생: {e}")
            time.sleep(0.2)
    print(f"\n✅ 저장 완료: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
