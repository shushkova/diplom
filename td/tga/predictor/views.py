from django.shortcuts import render
from.apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView


class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            # get sound from request
            question = request.GET.get('question')

            # vectorize sound
            vector = PredictorConfig.vectorizer.transform([question])
            # predict based on vector
            prediction = PredictorConfig.predictor.predict(vector)[0]
            # build response
            response = {'message': prediction}  # return response
            return JsonResponse(response)
