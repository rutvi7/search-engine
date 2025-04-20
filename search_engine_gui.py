import os
import re
from bs4 import BeautifulSoup
from collections import defaultdict
import tkinter as tk
from tkinter import messagebox, scrolledtext

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

# GUI
def run_gui():
    engine = SearchEngine()
    try:
        engine.index_documents("pages")
    except FileNotFoundError:
        messagebox.showerror("Error", "The 'pages' directory was not found.")
        return

    def perform_search():
        query = entry.get()
        results = engine.search(query)
        output.delete(1.0, tk.END)
        if not results:
            output.insert(tk.END, "No results found.")
        else:
            for doc, count in results:
                output.insert(tk.END, f"{doc}: {count}\n")

    window = tk.Tk()
    window.title("Simple Search Engine")

    tk.Label(window, text="Enter search term:").pack(pady=5)
    entry = tk.Entry(window, width=40)
    entry.pack(pady=5)

    tk.Button(window, text="Search", command=perform_search).pack(pady=5)

    output = scrolledtext.ScrolledText(window, width=60, height=15)
    output.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    run_gui()
