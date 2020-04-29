from django.shortcuts import render

# Create your views here.
def index(self):
	context = {
		'judul':'Slamet Web',
		'author': 'Peter Slamet',
		'page':'About',
	}
	return render(self, 'about/index.html', context)