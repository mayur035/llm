import requests;

def scrape_linkedin_profile(linked_profile_url:str):
    response = requests.get(linked_profile_url,timeout=10)
    data= response.json()
    data = {
        k:v
        for k,v in data.items()
        if v not in ([],"","",None)
        and k not in ["certifications"]
    }
    print('linked in scraper')
    return data