import requests

def search_google_books(title):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": title}
    
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

results = search_google_books("English for programmers")

# Print titles and IDs
for item in results.get("items", []):
    volume_info = item.get("volumeInfo", {})
    print("Title:", volume_info.get("title"))
    print("Authors:", volume_info.get("authors"))
    print("ID:", item.get("id"))
    print()