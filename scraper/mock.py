import json

def scrape_facebook_group():
    # Use 'utf-8' encoding to correctly handle special characters
    with open('scraper/mock.json', encoding='utf-8') as mock_data:
        results = json.load(mock_data)
    return results
