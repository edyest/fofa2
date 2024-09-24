import requests
from bs4 import BeautifulSoup

# URL for the Fofa search
search_url = 'https://fofa.info/result?qbase64=Y2VydD0id3d3LnNwZWVkdGVzdC5uZXQiICYmIHBvcnQ9IjQ0MyI%3D'

# Function to scrape IPs
def scrape_fofa_ips():
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ips = []
        
        # Extracting all IP addresses from the search results
        for result in soup.find_all('div', class_='list_mod_t'):
            ip = result.find('a').text.strip()
            ips.append(ip)
        
        return ips
    else:
        print('Failed to fetch the page.')
        return []

# Saving the scraped IPs to a file
def save_ips_to_file(ips):
    with open('fofa_ips.txt', 'w') as f:
        for ip in ips:
            f.write(f'{ip}\n')

if __name__ == '__main__':
    ips = scrape_fofa_ips()
    if ips:
        save_ips_to_file(ips)
        print(f'Successfully saved {len(ips)} IPs to fofa_ips.txt')
    else:
        print('No IPs found.')
      
