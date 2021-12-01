import requests
import bs4
from django.contrib import messages
from bs4 import BeautifulSoup
import pprint
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
	return render(request,'home.html')

s=1 
def technews(request):
	hn=[]
	global s
	x=request.POST.get("size")
	y=request.POST.get("points")
	if x==None:
		j=f"https://news.ycombinator.com/news?p={s}"
	if x<0:
		s=3
		j=f"https://news.ycombinator.com/news?p={s}"
		

	elif(x):
		s=int(x)
		j=f"https://news.ycombinator.com/news?p={s}"
	else:
		s=s+1
		j=f"https://news.ycombinator.com/news?p={s}"
	j=f"https://news.ycombinator.com/news?p={s}"
	res=requests.get(j)
	soup=BeautifulSoup(res.text,'html.parser') 
	links=soup.select(".titlelink")
	subtext=soup.select(".subtext")
	j=0
	k=0
	for i in links:
		href=links[j].get("href")
		vote=subtext[j].select('.score')
		if(len(vote)):
			points=vote[0].getText().replace('points','')
			points=int(points.replace('point',''))
			k=k+1
			m=int(y)
			if points>m:
				hn.append({"title":i.getText()})
				hn.append({"link":href})
				hn.append({"points":points})
		j=j+1
	print(hn)
	return render(request,'home.html',{"l":hn})
