from bs4 import BeautifulSoup
import requests
class spiderstory(object):

    def __init__(self):
        self.url = 'http://www.365haoshu.com/Book/Chapter/'
        self.names = []#存放章节名称
        self.hrefs = []#存放章节链接


    def get_urlandname(self):
        '''获取章节名称和和章节URL'''
        response = requests.get(url=self.url + 'List.aspx?NovelId=6686 ')
        req_parser = BeautifulSoup(response.text,"html.parser")
        div = req_parser.find_all('div',class_='user-catalog-ul-li')
        a_bf = BeautifulSoup(str(div))
        a = a_bf.find_all('a') 
        for i in a:
            self.names.append(i.find('span',class_='fl').string)
            self.hrefs.append(self.url + i['href'])


    def get_text(self,url):
        '''获取对应章节内容'''
        respons2 =requests.get(url=url)
        c = BeautifulSoup(str(respons2.text),'html.parser')
        b = c.find_all('p', class_='p-content')
        text = []
        for temp in  b:
            text.append(temp.string)
        return text


    def writer(self,name,path,text1):
        ''' 写入TXT文档'''
        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text1)
            f.write('\n\n')


if __name__ == "__main__": # 运行入口
    a= spiderstory()
    a.get_urlandname()
    for i in range(len(a.names)):
        name = a.names[i]
        text = str(a.get_text(a.hrefs[i]))
        a.writer(name,'F:\小说.txt',text)
    print(a)