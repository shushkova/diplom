from django.shortcuts import render
from.apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import pandas as pd


class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            # get sound from request
            question = request.GET.get('question')

            # vectorize sound
            # vector = PredictorConfig.vectorizer.transform([question])
            # predict based on vector
            # prediction = PredictorConfig.predictor.predict(vector)[0]
            chavo = PredictorConfig.chavo
            res = PredictorConfig.classifier.predict(question, k=1)
            prediction = chavo[chavo.themes == res[0][0][9:]].iloc[0,2]
            score = res[1][0]
            # build response
            if score < 0.3:
                prediction = 'Вопрос не относится к тематике помощника'
            response = {'message': str(prediction)} # return response
            print(response)
            return JsonResponse(response)
