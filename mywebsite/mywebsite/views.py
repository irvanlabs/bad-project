from django.shortcuts import render

def index(request):
	context = {
		'judul':'Slamet Web',
		'author': 'Peter Slamet',
		'page':'Home',
	}

	return render(request, 'index.html',context)