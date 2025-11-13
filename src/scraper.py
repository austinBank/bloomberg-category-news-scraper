thonimport requests
from bs4 import BeautifulSoup
import json

class BloombergScraper:
    def __init__(self, category_url):
        self.category_url = category_url
    
    def fetch_articles(self):
        response = requests.get(self.category_url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data, status code: {response.status_code}")
        return response.text
    
    def parse_articles(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        articles = []
        for article in soup.find_all('article'):
            data = {
                'image': article.find('img')['src'] if article.find('img') else None,
                'headline': article.find('h2').text if article.find('h2') else None,
                'byline': article.find('span', {'class': 'byline'}).text if article.find('span', {'class': 'byline'}) else None,
                'url': article.find('a')['href'] if article.find('a') else None,
                'publishedAt': article.find('time')['datetime'] if article.find('time') else None
            }
            articles.append(data)
        return articles
    
    def save_to_json(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def run(self):
        html = self.fetch_articles()
        articles = self.parse_articles(html)
        self.save_to_json(articles, 'articles.json')

if __name__ == '__main__':
    scraper = BloombergScraper('https://www.bloomberg.com/category/technology')
    scraper.run()