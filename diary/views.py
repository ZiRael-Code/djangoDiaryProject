import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from diary.dtos.request import Create_Diary_Request
from diary.dtos.request.Create_Diary_Request import CreateDiaryRequest
from diary.services.DiaryService import DiaryService


# def indexs(request):
#     return render(request, "../templates/hello.html")
#
#
# def greet_me(request, name):
#     return HttpResponse(f"let explore django...{name}")
#
#
# @csrf_exempt
# def texting_url(request):
#     if request.method == "POST":
#         body = request.body.decode("utf-8")
#         json_data = json.loads(body)
#
#         first_name = json_data["first_name"]
#         last_name = json_data["last_name"]
#
#         response_data = {
#             'message': 'Data received successfully!',
#             'first_name': first_name,
#             'last_name': last_name
#         }
#
#         return JsonResponse(response_data)
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)
#

globals()
diaryService = DiaryService()


@csrf_exempt
def create_diary(request):
    if request.method == "POST":
        body = request.body.decode("utf-8")
        json_data = json.loads(body)

        username = json_data["username"]
        password = json_data["password"]

        req = CreateDiaryRequest(username, password)
        diary = diaryService.createDiary(req)

        return JsonResponse(diary)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

