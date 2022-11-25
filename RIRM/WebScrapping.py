import requests
import bs4
import re


def get_contact(soup, response):
    try:
        phone = soup.select("a[href*=tel]")[0].text
        return phone
    except:
        pass

    try:
        phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response.text)[0]
        return phone
    except:
        pass

    try:
       phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response.text)[-1]
       return phone
    except:
        print ('Phone number not found')
        phone = ''
        return phone


def get_email(soup, response):
    try:
        email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response.text)[-1]
        return email
    except:
        pass

    try:
        email = soup.select("a[href*=mailto]")[-1].text
    except:
        print ('Email not found')
        email = ''
        return email


def get_social_info(soup, response):
    sm_sites = ['twitter.com', 'facebook.com', 'linkedin.com']
    sm_sites_present = []
    all_links = soup.find_all('a', href=True)

    for sm_site in sm_sites:
        for link in all_links:
            if sm_site in link.attrs['href']:
                sm_sites_present.append(link.attrs['href'])

    return sm_sites_present

def get_url_details(url):
    response = None
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
    except:
        print ('Unsucessful: ' + str(response))

    contact = get_contact(soup, response)
    email = get_email(soup, response)
    social = get_social_info(soup, contact)

    print('Social Links:- ', social)
    print('Email/s:- ', email)
    print('Contact:-', contact)


url = input('Enter the url: ')
get_url_details(url)
# https://ful.io/