from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News

def index(request):
    query = request.GET.get('q', '')  # 获取查询参数，默认为空字符串
    print(f"Query: {query}")
    if query:
        news_list = News.objects.filter(title__icontains=query)
    else:
        news_list = News.objects.all()

    paginator = Paginator(news_list, 20)  # 每页显示 20 个项目
    page_number = request.GET.get('page')
    print(f"Page Number: {page_number}")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }

    return render(request, 'home/index.html', context)
