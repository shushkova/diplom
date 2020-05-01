#!/usr/bin/python
# -*- coding: utf-8 -*-
from types import SimpleNamespace as Namespace

import glob
import pandas as pd
import numpy as np
import collections
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib
import matplotlib.style
matplotlib.style.use('ggplot')
import seaborn
import operator
import math
import seaborn as sns

def LoadTrain(data_csv):
    files = glob.glob("/home/varykha/gpn_diplom/data*.csv")
    for file in files:
        tmp = pd.read_csv(file, sep=';')
        data_csv = pd.concat([tmp, data_csv], ignore_index=True)
    #data = FilterRowsOperator(data_csv)
    #tmp = pd.read_csv("/home/varykha/gpn_diplom/data1.csv", sep=';')
    data_csv = pd.concat([tmp, data_csv], ignore_index=True)
    data = FilterRowsOperator(data_csv)
    # print(data)
    return data
    # data1 = data1[['Идентификатор обращения', 'Автор', 'Сообщения']]


def FilterRowsOperator(data_csv):
    data_csv = data_csv[['Идентификатор обращения', 'Автор', 'Сообщения']]
    data_csv.head()
    value_list = data_csv['Автор'].str.contains('Оператор*')

    value = []
    for i in range(0, len(value_list)):
        if value_list[i] is True:
            value.append(i)

    v = data_csv.index.isin(value)
    data_csv = data_csv[['Идентификатор обращения', 'Автор', 'Сообщения']][v]
    return data_csv


def CousinDist(df_chavo, data_csv):
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(df_chavo['response'])
    print(X_train_counts.shape)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    print(X_train_tfidf.shape)

    res = [0] * len(data_csv)
    k = 0;
    p = 0
    res2 = [0] * len(data_csv)

    for index, i in data_csv.iterrows():
        res[k] = np.amax(cosine_similarity(count_vect.transform([data_csv['Сообщения'][index]]), X_train_tfidf))
        if res[k] > 0:
            res2[p] = res[k]
            p = p + 1
        k = k + 1
    print(np.amax(res))
    print(np.amax(res2))
    d = pd.DataFrame(res)
    print(d.describe())
    #sns.kdeplot(s).figure.savefig('cos1.png')
    #s = pd.Series(res)
    res_around = np.around(res, decimals=4)
    dict_my = collections.Counter(res_around)
    s = pd.Series(res)
    s.plot.kde().figure.savefig('1cos.1.png')
    s.plot.hist(alpha=0.6).figure.savefig('1hist.1.png')

    #s2 = pd.Series(res2)
    #res_around2 = np.around(res2, decimals=4)
    dict_my2 = collections.Counter(res_around2)
    #s2 = pd.Series(dict_my2)
    #s2.plot.kde().figure.savefig('1cos1.2.png')
    #s2.plot.hist(alpha=0.6).figure.savefig('1hist.2.png')

    d.plot.kde().figure.savefig('1cos.png')
    return d


def ReturnLabel(df_chavo, theme_label, response):
    find = pd.DataFrame(df_chavo.loc[df_chavo['response'] == response])
    result = pd.DataFrame()
    # print(find)
    merged_inner = pd.DataFrame(columns=['label', 'theme', 'response'])
    for i in range(0, 4):
        theme_i = 'theme' + str(i)
        left = pd.DataFrame(find[[theme_i, 'response']])
        left.rename(columns={theme_i: 'theme'}, inplace=True)
        # print(left)
        right = pd.DataFrame(theme_label[['label', 'theme']], columns=['label', 'theme'])
        temp = pd.merge(left, right, on='theme', how='inner')
        # print(result[result[['theme', 'label']]])
        result = pd.concat([temp, result], ignore_index=True)
    print(result)
