import os
import re
from bs4 import BeautifulSoup
from collections import defaultdict

STOP_WORDS = {
    'the', 'is', 'at', 'of', 'on', 'and', 'a', 'to', 'in', 'for', 'with', 'as',
    'by', 'an', 'be', 'this', 'that', 'are', 'was', 'it', 'from', 'or', 'but'
}

class SearchEngine:
    def __init__(self):
        self.index = defaultdict(lambda: defaultdict(int))
        self.links = defaultdict(set)

    def index_documents(self, directory):
        for filename in os.listdir(directory):
            if filename.endswith(".html"):
                path = os.path.join(directory, filename)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    soup = BeautifulSoup(content, 'html.parser')
                    text = soup.get_text()
                    words = re.findall(r'\b\w+\b', text.lower())
                    for word in words:
                        if word not in STOP_WORDS:
                            self.index[word][filename] += 1

                    for a in soup.find_all('a', href=True):
                        self.links[filename].add(a['href'])

    def search(self, query):
        results = self.index.get(query.lower(), {})
        ranked = sorted(results.items(), key=lambda x: -x[1])
        return ranked

    def display_links(self, page):
        return self.links.get(page, set())

def main():
    engine = SearchEngine()
    engine.index_documents('pages')

    with open('output.txt', 'w') as f:
        queries = ['taj', 'park', 'city', 'the', 'water']
        for query in queries:
            f.write(f"Search results for '{query}':\n")
            results = engine.search(query)
            for doc, count in results:
                f.write(f"  {doc}: {count}\n")
            f.write('\n')

        f.write("Hyperlinks in each page:\n")
        for page in engine.links:
            links = engine.display_links(page)
            f.write(f"{page} links to: {', '.join(links)}\n")

if __name__ == "__main__":
    main()
