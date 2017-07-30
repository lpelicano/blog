from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post


def post_create(request):
	return HttpResponse("Hello")


def post_detail(request, pk):
	instance = get_object_or_404(Post, pk=pk)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)


def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"

	}
	return render(request, "index.html", context)


def post_update(request):
	return HttpResponse("Hello")


def post_delete(request):
	return HttpResponse("Hello")
