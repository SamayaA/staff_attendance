
# Create your views here.
from operator import contains
from bs4 import BeautifulSoup
from django.shortcuts import render

from diploma.settings import TEMPLATE_DIR
def workers(request):
    content = {
        "n": range(10),
        "status": 'done',
    }
    # soup = BeautifulSoup(open(TEMPLATE_DIR + '\index.html'), 'html.parser')
    # h1 = soup.find_all('h1')
    return render(request,"index.html", content)

# def change_color():
#     soup = BeautifulSoup(open(TEMPLATE_DIR + '\index1.html'), 'html5lib')
#     h1 = soup.find_all(tag)

def homepage(request):
    content = {
        "user": "User",
        "done_hours": "40",
    }
    return render(request,"homepage.html", content)
