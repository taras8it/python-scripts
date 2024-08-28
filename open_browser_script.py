import webbrowser
import urllib.parse

# Define the search query
search_query = "Hello World"

# Encode the search query to be URL-safe
encoded_query = urllib.parse.quote(search_query)

# Define the Google search URL with the encoded query
google_search_url = f"https://www.google.com/search?q={encoded_query}"

# Open the default web browser and search for the query
webbrowser.open(google_search_url)
