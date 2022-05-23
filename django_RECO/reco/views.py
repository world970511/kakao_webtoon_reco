from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import AllData
import pandas as pd


# Create your views here.
def intro(request):
    return render(request, 'intro.html')

#데이터 선택
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
    if request.method == "POST":
        selected_webbtoon_id_list = request.POST.getlist('selected') 
        print(map(int,selected_webbtoon_id_list)) 
        reco(selected_webbtoon_id_list,webtoons)
    return render(request, 'select.html',{'webtoon':webtoon})    

#추천
def reco(idList,all_data):
    selected_data=AllData.objects.filter(id__in=idList)
    all_df = pd.DataFrame(list(all_data))
    selected_df=pd.DataFrame(list(AllData.objects.filter(id__in=idList)))
    selected_data.to_csv('test.csv')
    return redirect('reco:result')

#추천 출력
def result(request):
    all_data=AllData.objects.all()
    return render(request, 'result.html',{'all_data':all_data[:10]})