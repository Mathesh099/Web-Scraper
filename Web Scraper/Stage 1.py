import requests
r = requests.get(input('Input the URL:'))
if r:
    if 'content' in r.json().keys():
        print(r.json())
    else:
        print('Invalid quote resource!')
else:
    print('Invalid quote resource!')