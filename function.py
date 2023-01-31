from bs4 import BeautifulSoup
import requests

def get_title_content_img(URL):
    res = requests.get(URL)
    soup = BeautifulSoup(res.content,'lxml')
    soup = soup.main

    if soup.find(class_='entry-title'):
        title = soup.find(class_='entry-title').text
        type = 1
    elif soup.find(class_='entry_title'):
        title = soup.find(class_='entry_title').text
        type = 2
    else:
        title = soup.find('h1').text
        type = 3

    contents = soup.find_all('p')
    content = ''
    for i, c in enumerate(contents):
        content += c.text
        if len(content) >100:
            break

    tmp_list = []
    for img in soup('img'):
        img_src = img.get('src')
        if img_src.startswith('http'):
            if 'wp-content' in img_src:
                tmp_list.append(img_src)
    img_url = tmp_list[0]

    return title, content, img_url