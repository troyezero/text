# -*- coding:UTF-8 -*-
import requests
 
if __name__ == '__main__':
    target = 'http://longzu5.co/post/158.html'
    req = requests.get(url=target)
    print(req.text)