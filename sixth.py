import sys
import requests


def download_url_and_get_all_hrefs(url):
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"HTTP chyba: Kód stavu {response.status_code}")
            return []

        obsah = response.text
        hrefs = []
        start_idx = 0

        while True:
            start_idx = obsah.find('<a ', start_idx)
            if start_idx == -1:
                break

            href_start = obsah.find('href="', start_idx)
            if href_start == -1:
                break
            href_start += len('href="')

            href_end = obsah.find('"', href_start)
            if href_end == -1:
                break
            
            href = obsah[href_start:href_end]

            if href.startswith('https://'):
                hrefs.append(href)

            start_idx = href_end
        
        return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        download_url_and_get_all_hrefs(url)
    except requests.exceptions.RequestException as e:     
        print(f"Chyba při stahování URL: {e}")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
