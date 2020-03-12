from django.shortcuts import render

from blog.models import Post

def index(request):
	posts = Post.objects.filter(is_draft = False)[:3]
	data = { 'posts': posts }
	return render(request, 'homepage.html', data)

def mentions_legales(request):
	return render(request, 'mentions_legales.html')

def confidentialite_donnees(request):
	return render(request, 'confidentialite_donnees.html')

def custom_404(request, exception):
    response = render(request, "404.html")
    response.status_code = 404
    return response	