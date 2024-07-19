import requests

def fetch_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
    return None

def main():
    url = input("Enter the URL of the social media page: ")
    html_content = fetch_html(url)
    if html_content:
        print("Page fetched successfully.")
        print(html_content[:500])

if __name__ == "__main__":
    main()
