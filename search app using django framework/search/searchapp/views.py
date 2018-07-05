from django.shortcuts import render
from django.http import HttpResponse
import requests
from django import template
from .forms import searchForm

# Create your views here.

# method to render display page for search
def disp(request): 
	return render(request,"index.html",{})


#method which request data from apache solr, parse the data and render the result page

def search_author(request):
	name=request.POST['search'] #getting the content of text box user input
	
	r  = requests.get("http://localhost:8983/solr/search/select?q=name:{0}&wt=json".format(name)) #building url and requesting from apache solr
	
	r=r.json() #getting the data in json form from the url

	data=r.get('response') #getting the response part from the result which consist documents
    
	n=[]
	
	if(data.get("numFound")==0):   # checking whether result has documents in it or no documents
		return render(request,"sresult.html",{"result":{}}) # if no documents return 0 documents 

	adet=data.get("docs") #getting the docs from the results

	for row in adet:	  #getting all authors name from result and addding to list
		n.extend(row.get("name"))
	 
	result=dict((map(reversed, enumerate(n))))	 #converting to dictionary as result needs to be in dictionayry	
	
	return render(request,"sresult.html",{"result":result }) #rendering the results in sresult.html
		

def get_author(request):
	if request.method=="POST":
		form=searchForm(request.Form)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

	else:
		form=searchForm()
	return render(request,'index.html',{'form':form})

