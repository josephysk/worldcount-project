from django.http import HttpResponse
from django.shortcuts import render
import operator

#def homepage(request):
#	return render(request,'home.html')

#def homepage(request):
#	return render(request,'home.html', {'hithere':'This is me'})

def homepage(request):
	return render(request,'home.html')

def eggs(request):
 	return HttpResponse('Eggs are great')

def dogs(request):
	return HttpResponse('<h1>DOGS</h1>')

def aboutus(request):
	return render(request,'aboutus.html')

def count(request):
	fulltext = request.GET['fulltext']
#	print(fulltext)
#	return render(request,'count.html',{'fulltext':fulltext})

	wordlist = fulltext.split()

	worddictionary =  {}

	for word in wordlist:
		if word in worddictionary:
			#Increase
			worddictionary[word] += 1
		else:
			#add to the dictionary
			worddictionary[word] = 1


#	return render(request, 'count.html',{'fulltext':fulltext})

	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})