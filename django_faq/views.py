from django.shortcuts import render
import json
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .analyzer import Analyzer
from . import models


@api_view(['POST'])
def insert(request):
    try:
        qanda_data = json.loads(request.body)
        qandaid = models.insert_qanda(qanda_data["question"], qanda_data["answer"])
        text = qanda_data["question"] + " " + qanda_data["answer"]
        filtered_tokens = Analyzer.Analyzer.analyze(text)
        models.insert_index(str(qandaid), filtered_tokens)
        response = JsonResponse({'message': "success."}, status=200, content_type='application/json')
        return response
    except Exception:
        response = JsonResponse({'message': 'failed to insert.'}, status=500, content_type='application/json')
        return response


@api_view(['POST'])
def update(request):
    try:
        fixed_qanda_data = json.loads(request.body)
        models.update_qanda(str(fixed_qanda_data["qandaid"]), fixed_qanda_data["question"], fixed_qanda_data["answer"])
        text = fixed_qanda_data["question"] + " " + fixed_qanda_data["answer"]
        filtered_tokens = Analyzer.Analyzer.analyze(text)
        models.insert_index(str(fixed_qanda_data["qandaid"]), filtered_tokens)
        models.unlock(str(fixed_qanda_data["qandaid"]))
        response = JsonResponse({'message': "success."}, status=200, content_type='application/json')
        return response
    except Exception:
        response = JsonResponse({'message': 'failed to update.'}, status=500, content_type='application/json')
        return response


@api_view(['GET'])
def search(request):
    try:
        word = request.GET.get("word")
        splited_words = word.split()
        if len(splited_words) == 1:  # 検索ワードが１つ
            searched_list = models.search_qanda(splited_words[0])
        else:  # 検索ワードがスペース挟んで複数
            searched_list = models.search_qanda2(splited_words)
        response = JsonResponse({'data': searched_list}, status=200, content_type='application/json')
        return response
    except Exception:
        response = JsonResponse({'message': 'failed to search.'}, status=500, content_type='application/json')
        return response


@api_view(['DELETE'])
def delete(request):
    try:
        qandaid = request.GET.get("qandaid")
        models.delete_qa_and_index(qandaid)
        response = JsonResponse({'message': "success."}, status=200, content_type='application/json')
        return response
    except Exception:
        response = JsonResponse({'message': 'failed to delete.'}, status=500, content_type='application/json')
        return response


@api_view(['POST'])
def lock(request):
    try:
        qandaid_data = json.loads(request.body)
        print(qandaid_data["qandaid"])
        models.lock(str(qandaid_data["qandaid"]))
        response = JsonResponse({'message': "success."}, status=200, content_type='application/json')
        return response
    except Exception:
        response = JsonResponse({'message': 'failed to lock.'}, status=500, content_type='application/json')
        return response


@api_view(['DELETE'])
def unlock(request):
    try:
        qandaid = request.GET.get("qandaid")
        models.unlock(qandaid)
        response = JsonResponse({'message': "success."}, status=200, content_type='application/json')
        return response
    except Exception:
        response = JsonResponse({'message': 'failed to unlock.'}, status=500, content_type='application/json')
        return response


@api_view(['GET'])
def check(request):
    try:
        qandaid = request.GET.get("qandaid")
        count = models.check(qandaid)
        response = JsonResponse({'data': count}, status=200, content_type='application/json')
        return response
    except Exception:
        response = JsonResponse({'message': 'failed to check.'}, status=500, content_type='application/json')
        return response