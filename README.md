# search-engine
A Python search engine that indexes HTML pages, ranks results, and analyzes links. Supports GUI and CLI.

# CS600 Search Engine Project

## Overview
This project implements a simplified search engine that indexes words from local HTML pages, excludes stop words, and supports hyperlink analysis and ranking based on word frequency. The engine is designed to work with small websites and provides both a command-line interface (CLI) and a graphical user interface (GUI).

## Features
1. **Indexing**: Parses HTML pages, extracts words, and builds an inverted index while excluding common stop words.
2. **Searching**: Returns documents containing the query word, ranked by frequency of occurrence.
3. **Hyperlink Analysis**: Captures and displays hyperlinks between pages.
4. **GUI**: Provides a user-friendly interface for interactive searching.

## Approach
### Data Structures
- **Inverted Index**: A `defaultdict` of `defaultdict(int)` to map words to documents and their frequencies.
- **Hyperlinks**: A `defaultdict` of sets to store outgoing links for each page.

### Algorithms
1. **Indexing**:
   - Uses `BeautifulSoup` to parse HTML and extract text.
   - Tokenizes text into words using regex (`\b\w+\b`).
   - Excludes stop words (e.g., "the", "and", "is") during indexing.
   - Counts word frequencies per document.

2. **Ranking**:
   - Results are ranked by the frequency of the query word in each document (higher frequency = higher rank).

3. **Hyperlink Analysis**:
   - Extracts all `<a href>` tags to map page connections.

### Boundary Conditions Tested
- Searching for non-existent words.
- Searching for stop words (e.g., "the").
- Handling pages with no outgoing links.
- Empty or malformed HTML files.

## How to Run
### Dependencies
Install `beautifulsoup4` for HTML parsing:
```bash
pip install beautifulsoup4
