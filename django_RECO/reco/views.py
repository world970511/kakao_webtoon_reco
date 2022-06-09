from asyncio.windows_events import NULL
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AllData
import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class saveList:
    def setdata(self,li):
        self.li=li

# 시작
def intro(request):
    return render(request, 'intro.html')

#404페이지
def page_not_found(request, exception):
    return render(request, 'reco/404.html', {})

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
        saveList.setdata=list(map(int,request.POST.getlist('selected')))
        return redirect('reco:result')
    return render(request, 'select.html',{'webtoon':webtoon})    

#추천
def reco(idList,all_data):
    #전체 데이터 호출
    all_df = pd.DataFrame(list(all_data.values()))

    #데이터 백터화
    tfidf_vector = TfidfVectorizer()
    tfidf_matrix = tfidf_vector.fit_transform(all_df['key_word']+' '+all_df['genre']+' '+all_df['desc_noun']).toarray()
    tfidf_matrix_feature = tfidf_vector.get_feature_names()
    items = pd.DataFrame(tfidf_matrix, columns=tfidf_matrix_feature, index = all_df.title)
    
    #유저 데이터
    watch=np.array(all_df['id'].apply(lambda x: 1 if x in idList else 0))
    user_pref=pd.DataFrame([np.dot(watch.T,items)], columns=tfidf_matrix_feature, index = ['user'])
    
    #코사인 계산
    cosine=pd.DataFrame(cosine_similarity(user_pref, items), columns= all_df.id, index = ['user'])
    sorted_user_predictions = cosine.iloc[0].sort_values(ascending=False).reset_index()
    sorted_user_predictions=sorted_user_predictions[~sorted_user_predictions['id'].isin(idList)]

    #10개 추천
    reco=sorted_user_predictions.head(10)
    recommendWebtoons=reco['id'].values.tolist()
    return recommendWebtoons


#추천 출력
def result(request):
    webtoons=AllData.objects.all()
    selected_webbtoon_id_list=saveList.setdata
    recommendWebtoons=reco(selected_webbtoon_id_list,webtoons)#추천 결과
    RecoWebtoons=AllData.objects.filter(id__in=recommendWebtoons)
    saveList.setdata=[]
    return render(request, 'result.html',{'all_data':RecoWebtoons})

    