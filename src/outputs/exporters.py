thonimport json

class Exporters:
    @staticmethod
    def export_to_json(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def export_to_txt(data, filename):
        with open(filename, 'w') as f:
            for article in data:
                f.write(f"Headline: {article['headline']}\n")
                f.write(f"Author: {article['author']}\n")
                f.write(f"Published At: {article['publishedAt']}\n")
                f.write(f"URL: {article['url']}\n")
                f.write("-" * 40 + "\n")