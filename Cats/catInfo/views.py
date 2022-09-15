
from .models import Cat
from.serializers import CatsSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# get all
@api_view(['GET'])
def Cat_list(request):
       cats =Cat.objects.all()
       selize=CatsSerializer(cats, many =True)  
       return JsonResponse(selize.data, safe=False)

 # add       
@api_view(['POST'])
def CatAdd(request):
       selize=CatsSerializer(data=request.data)
       if selize.is_valid():
           selize.save()
       return Response(selize.data,status=status.HTTP_201_CREATED)


 # get by id      
@api_view(['GET'])
def GetCat(  request, in_question_id ):
     if test_requst(in_question_id):
      selize=CatsSerializer(Cat.objects.get(pk=in_question_id ))  
      return Response(selize.data)
     else: 
      return Response(status=status.HTTP_404_NOT_FOUND)  


 # update     
@api_view(['PUT'])
def updateCat(  request, in_question_id ):
    
      if  test_requst(in_question_id)  :
        selize=CatsSerializer(Cat.objects.get(pk=in_question_id ), data=request.data)
        if selize.is_valid():
           selize.save()  
           return Response(selize.data,status=status.HTTP_200_OK)
        return Response( selize.errors,status=status.HTTP_400_BAD_REQUEST)   
      else:  
       return Response(status=status.HTTP_404_NOT_FOUND)   



 # delete       
@api_view(['DELETE'])
def delCat(request, in_question_id ):

 if test_requst(in_question_id):
     Cat.objects.get(pk=in_question_id ).delete()
     return  Response(status=status.HTTP_202_ACCEPTED)
 else:    
  return Response(status=status.HTTP_404_NOT_FOUND)
      


  # test for good requset    
def test_requst(in_question_id):
     try:
       cats =Cat.objects.get(pk=in_question_id )
     except Cat.DoesNotExist:
        return False
     return True   
