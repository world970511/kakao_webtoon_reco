from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .models import AllData
import pandas as pd
from random import randint

# Create your views here.
def intro(request):
    return render(request, 'intro.html')

#데이터 선택
def select(request):
    page = request.GET.get('page', '1')  # 페이지
    webtoons=AllData.objects.all().order_by('?')#전체 데이터 가져오기- 랜덤
    paginator = Paginator(webtoons, 150)  # 페이지당 150개씩 보여주기
    try:
        webtoon=paginator.page(page)
    except PageNotAnInteger:
        webtoon = paginator.page(1)
    except EmptyPage:
        webtoon = paginator.page(paginator.num_pages)
    if request.method == "POST":#체크된 데이터 가져오기
        selected_webbtoon_id_list = list(map(int,request.POST.getlist('selected')))
        reco(selected_webbtoon_id_list,webtoons)#추천
        return redirect('reco:result')
    return render(request, 'select.html',{'webtoon':webtoon})    

#추천
def reco(idList,all_data):
    recommendWebtoons=[]
    selected_data=AllData.objects.filter(id__in=idList)
    all_df = pd.DataFrame(list(all_data.values()))
    selected_df=pd.DataFrame(list(AllData.objects.filter(id__in=idList).values()))
    print(selected_df)


#추천 출력
def result(request):
    all_data=AllData.objects.all()
    print(all_data)
    return render(request, 'result.html',{'all_data':all_data[:10]})