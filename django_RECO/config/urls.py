from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reco/',include('reco.urls'))
]
#이미지 출력
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#404페이지
handler404 = 'reco.views.page_not_found'
