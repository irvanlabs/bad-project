from django.shortcuts import render

# Create your views here.
def index(self):
	context = {
		'judul':'Slamet Web',
		'author': 'Peter Slamet',
		'page':'Blog',
	}

	return render(self, "blog/index.html", context)