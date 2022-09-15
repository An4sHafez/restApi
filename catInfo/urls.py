from django.urls import path
from . import views

urlpatterns = [
    path('catLst/', views.Cat_list),
    path('catAdd/',views.CatAdd),
    path('GetCat/<int:in_question_id>/',views.GetCat),
    path('updateCat/<int:in_question_id>/',views.updateCat),
    path('delCat/<int:in_question_id>/',views.delCat),
    
]
