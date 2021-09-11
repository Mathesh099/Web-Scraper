import requests
from bs4 import BeautifulSoup
import string
articles = []
gap = ''
for i in range(len(string.punctuation)):
    gap = gap + ' '
url = str('https://www.nature.com/nature/articles')  # input('Input the URL:\n')
if __name__ == "__main__":
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    all_articles = soup.find_all(class_='app-article-list-row__item')
    for i in all_articles:
        if i.find('span', class_='c-meta__type').text == 'News':
            title = (i.find('h3').text
                     .replace('\n', '')
                     )
            print(title)
            for j in title:
                if j in string.punctuation:
                    title = title.replace(j, '')
            title = title.replace(' ', '_')
            print(title)
            head = i.find('span', class_='c-meta__type').text
            link = i.find('a', href=True)['href']
            articles.append((title, head, link))
            # gathering news content
            r = requests.get('https://www.nature.com'+link)
            soup = BeautifulSoup(r.content)
            # read the content line nby line and make changes in body and title
            file = open(title+'.txt', 'wb')
            file.write(bytes(str(soup.title.text.strip(' ')), encoding='utf-8'))
            file.write(bytes(str(soup.body.text.strip(' ')), encoding='utf-8'))
            file.close()