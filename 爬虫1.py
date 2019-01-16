from bs4 import BeautifulSoup
import requests
import html5lib
if __name__ == "__main__":
     target = 'http://longzu5.co/post/158.html'
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html,"html5lib")
     p = bf.find_all('p',style='text-indent: 2em;') 
     print(p[0].text.replace('\xa0'*8,'\n\n'))