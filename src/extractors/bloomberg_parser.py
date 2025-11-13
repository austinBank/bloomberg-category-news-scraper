thonimport json

class BloombergParser:
    @staticmethod
    def parse_article(article_data):
        parsed_data = {
            'headline': article_data['headline'],
            'author': article_data['byline'],
            'publishedAt': article_data['publishedAt'],
            'summary': article_data.get('summary', ''),
            'url': article_data['url'],
            'image': article_data['image']
        }
        return parsed_data
    
    @staticmethod
    def parse_json(filename):
        with open(filename, 'r') as f:
            articles = json.load(f)
        return [BloombergParser.parse_article(article) for article in articles]