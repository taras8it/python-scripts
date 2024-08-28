import webbrowser
import urllib.parse
import argparse
import sys

# Define a dictionary of search engines
SEARCH_ENGINES = {
    'google': 'https://www.google.com/search?q=',
    'bing': 'https://www.bing.com/search?q=',
    'duckduckgo': 'https://duckduckgo.com/?q=',
    'yahoo': 'https://search.yahoo.com/search?p='
}

def search(query, engine='google'):
    """
    Open the web browser and perform a search with the specified engine.
    
    :param query: The search query string.
    :param engine: The search engine to use ('google', 'bing', 'duckduckgo', 'yahoo').
    """
    # Validate the selected search engine
    if engine not in SEARCH_ENGINES:
        print(f"Error: '{engine}' is not a supported search engine.")
        sys.exit(1)
    
    # Encode the search query to be URL-safe
    encoded_query = urllib.parse.quote(query)
    # Construct the search URL
    search_url = SEARCH_ENGINES[engine] + encoded_query
    # Open the browser and perform the search
    webbrowser.open(search_url)

def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Search the web from your terminal.")
    parser.add_argument('query', nargs='+', help="The search query terms.")
    parser.add_argument('-e', '--engine', choices=SEARCH_ENGINES.keys(), default='google',
                        help="Choose a search engine (default: Google).")

    # Parse the arguments
    args = parser.parse_args()
    # Combine query terms into a single string
    search_terms = ' '.join(args.query)
    # Call the search function with the provided query and engine
    search(search_terms, engine=args.engine)

if __name__ == "__main__":
    main()
