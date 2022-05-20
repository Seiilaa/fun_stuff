from bs4 import BeautifulSoup as bs
import requests
import pickle

url = 'https://artistro.com/blogs/news/30-most-famous-artworks-in-history-the-greatest-art-of-all-time'

# mask as a user
headers1 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
headers2 = {'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

session = requests.Session()
request = session.get(url, headers=headers1)
if request.status_code == 200:
    soup = bs(request.content, 'lxml')


# extract images
image_tags = soup.find_all('img', attrs=['lazybloggle blog__img m--auto'])
image_links = []
for image_tag in image_tags:
    image_link = image_tag.get('data-src')
    image_links.append(image_link)

# extract headlines
headline_tags = soup.find_all('h2', attrs=['margin_vertical--medium margin-top_none text--1636212957474'])
headlines = []
for tag in headline_tags:
    headlines.append(tag.text)

# extract image descriptions
description_tags = soup.find_all('div', attrs=['bggle--block bggle_text margin_vertical--medium margin-top_none'])
description_tags = description_tags[1:] # first text is a description to the article, so we drop it
descriptions = []
for tag in description_tags:
    descriptions.append(tag.text)

# combine data to dict
art_dict = {}
for i in range(len(headlines)):
    art_dict[headlines[i]] = [image_links[i], descriptions[i]]

# save to txt file
with open("art_dict.txt", "wb") as tf:
    pickle.dump(art_dict, tf)
