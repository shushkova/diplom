from django.apps import AppConfig
from django.apps import AppConfig
from django.conf import settings
import os
import pickle
import fasttext
import pandas as pd


class PredictorConfig(AppConfig):
    name = 'fasttext'
    # path = os.path.join(settings.MODELS, 'ft_classification0.8.bin')
    # load models into separate variables
    # Or load pre-trained classifier
    classifier = fasttext.load_model(settings.MODELS + '/ft_classification0.8.bin')
    chavo = pd.read_csv(settings.MODELS + '/chavo.csv')
    # predictor = classifier.predict()
    # To predict k-best labels from texts
    # predictor = classifier.predict(texts, k=3)
    # these will be accessible via this class
    # with open(path, 'rb') as pickled:
    #    data = pickle.load(pickled)
    # predictor = data['predictor']
    # vectorizer = data['vectorizer']





