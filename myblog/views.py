import urllib2
import json
from django.shortcuts import render
from myblog.models import Article
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage


# Create your views here.
def index(request):
	results = Article.objects.all()
	paginator = Paginator(results, 2)
	page_num = request.GET.get('page')
	try:
		results = paginator.page(page_num)
	except PageNotAnInteger:
		results = paginator.page(1)
	except EmptyPage:
		results = paginator.page(paginator.num_pages)
	results_id = [str(i.id) for i in results]
	ds_url = "http://api.duoshuo.com/threads/counts.json?short_name=gary-qiu&threads={0}".format(','.join(results_id))
	headers = {
		'Content-Type': 'application/json; charset=UTF-8',
	}
	r = urllib2.Request(ds_url, headers)
	ds_result = json.load(urllib2.urlopen(ds_url)).get('response')

	return render(request, 'blog/index.html', locals())


def blog_detail(request, blog_id):
	result = Article.objects.filter(id=blog_id).first()
	return render(request, 'blog/blog.html', locals())
