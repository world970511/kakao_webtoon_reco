from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import AllData

# Create your views here.
def intro(request):
    return render(request, 'intro.html')

#여기부터 작성할 것
def select(request):
    page = request.GET.get('page', '1')  # 페이지
    webtoons=AllData.objects.all()
    paginator = Paginator(webtoons, 15)  # 페이지당 10개씩 보여주기
    try:
        webtoon=paginator.page(page)
    except PageNotAnInteger:
        webtoon = paginator.page(1)
    except EmptyPage:
        webtoon = paginator.page(paginator.num_pages)
    if request.POST: 
        selected_webbtoon_id_list = list(map(int, request.POST.getlist('selected')))
        print(selected_webbtoon_id_list)
    return render(request, 'select.html',{'webtoon':webtoon})    


#추천 적용
def result(request):
    return render(request, 'result.html')