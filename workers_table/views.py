
# Create your views here.
from operator import contains
from bs4 import BeautifulSoup
from django.shortcuts import render

from diploma.settings import TEMPLATE_DIR
def workers(request):
    content = {
        "n": range(10),
    }
    # soup = BeautifulSoup(open(TEMPLATE_DIR + '\index.html'), 'html.parser')
    # print(soup.prettify())
    # h1 = soup.find_all('h1')
    # print(h1)
    # for i in h1:
    #     classes = i.get('class','')
    #     if 'h1' not in classes:
    #         i['class'] = i.get('class','') + ' h1'
    # print(soup)
    # with open(TEMPLATE_DIR + '\index1.html','w') as file:
    #     file.writelines(soup)
    return render(request,"index.html", content)
