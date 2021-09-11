import requests
from bs4 import BeautifulSoup
import string
import os
articles = []
gap = ''
for i in range(len(string.punctuation)):
    gap = gap + ' '
url = str('https://www.nature.com/nature/articles')  # input('Input the URL:\n')
n = int(input())
types = input()
pages = []
# Create directory after checking their presence

for i in range(1, n + 1):
    pages.append(url+'?searchType=journalSearch&sort=PubDate&page='+str(i))
    if 'Page_'+str(i) not in os.listdir():
        os.mkdir('Page_'+str(i))

if __name__ == "__main__":
    # for loop to get the list of page urls
    for p in pages:
        r = requests.get(p)
        soup = BeautifulSoup(r.content, 'html.parser')
        all_articles = soup.find_all(class_='app-article-list-row__item')
        for i in range(len(all_articles)):
            if all_articles[i].find('span', class_='c-meta__type').text == types:
                title = (all_articles[i].find('h3').text
                         .replace('\n', '')
                         )
                for j in title:
                    if j in string.punctuation:
                        title = title.replace(j, '')
                title = title.replace(' ', '_')
                head = all_articles[i].find('span', class_='c-meta__type').text
                link = all_articles[i].find('a', href=True)['href']
                articles.append((title, head, link))
                # gathering news content
                r = requests.get('https://www.nature.com'+link)
                soup = BeautifulSoup(r.content)
                # read the content line nby line and make changes in body and title
                # insert directory before the save
                file = open('Page_'+p[-1]+'/'+title+'.txt', 'wb')
                # file.write(bytes(str(soup.title.text.strip('\n')), encoding='utf-8'))
                for d in soup.find_all('div', class_='article-item__body'):
                    for s in d.find_all('p'):
                        file.write(bytes(str(s.text.strip('\n')), encoding='utf-8'))
                file.close()