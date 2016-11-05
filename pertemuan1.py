# pip3 install pillow

# from PIL import Image
# im=Image.open('pixel')
# px=im.load()
#
# for i in range(im.width);
#     for j in range(im.height):
#         r,g,b=px[i,j]

# f=open('lorem.txt','r')
# test=f.read()
# test=test.split()
# unique=set()
# for i in test:
#     unique.add(i)
# print(len(unique))

import bs4 as bs
import urllib.request
import re

def ltoInt(a):
    result=0
    for i in range(len(a)):
        result=result*10+int(a[i])
    return result

def cariInt(s):
    sacue=urllib.request.urlopen(s).read()
    soup=bs.BeautifulSoup(sacue,"lxml")
    for i in soup.find_all('code'):
        patFinder=re.compile("\d+")
        afterSearch=re.findall(patFinder,str(i))
        final=ltoInt(afterSearch)
    return final

s='http://chal.hmif.cf:5001/?flag=HMIF{a'
maks=6


# a=['1','2','3']
# print(cariInt(s))

alphaNumeric='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890_'
increasing = True

while increasing:
    for i in alphaNumeric:
        temp = s + i
        if cariInt(temp) == maks + 1:
            print(maks+1)
            maks+=1
            s += i
            break;
        elif (i == '_'):
            increasing = False
        print('lol')

print(s)
