import requests
from bs4 import BeautifulSoup
url = input()
if __name__ == '__main__':
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if soup.find('h1') is not None:
        if soup.find("span", class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD") is not None:
            title = soup.find('h1').text
            description = soup.find("span", class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD").text
            data = dict({"title": title, "description": description})
            print(data)
        else:
            print('Invalid movie page!')
    else:
        print('Invalid movie page!')