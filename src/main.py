import requests
from bs4 import BeautifulSoup

#This Assignment contains getting news from indianexpress.com
resp = requests.get('https://indianexpress.com/section/india/')
soup = BeautifulSoup(resp.content, 'html.parser')
path = '/home/lab/HadoopProject/creation_testdata/data/output.txt'
f_o = open(path, 'w')
# Getting news
title = soup.find_all(class_='articles')

#printing news :
len = len(title)
for i in range(len):
    f_o.write("\n------------- Letest News ------------------\n")
    f_o.write("HEADLINE {0}: {1}".format(i ,list(title[i])[1].get_text()))
    f_o.write("\n")
    f_o.write("DATE : {0}".format(list(title[i])[2].get_text()))
    f_o.write("\n")
    f_o.write("Discription : {0}".format(list(title[i])[3].get_text()))
    f_o.write("\n")
f_o.close()

