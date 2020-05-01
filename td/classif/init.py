#!/usr/bin/python
# -*- coding: utf-8 -*-
from data_preparaion import AddLabel
from data_preparaion import Create_Df
from data_preparaion import Unroll
from cosin import LoadTrain, ReturnLabel, CousinDist
import json
import pandas as pd

if __name__ == "__main__":
    theme_label = pd.DataFrame(columns=['label', 'theme'])
    # создадим числовые метки
    f = open("chavo_cor.json", 'r', encoding="utf-8")
    data = json.load(f)
    AddLabel(data, 100, 10, theme_label)
    theme_label = theme_label.drop_duplicates(subset='theme', keep="last").sort_values(by='theme').reset_index()
    # не совсем корректный (not all labels)
    print(theme_label)
    with open('chavo_cor_label.json', 'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False)

    f1 = open("chavo_cor_label.json", 'r', encoding="utf-8")
    data = json.load(f1)
    labels = [] * 1000
    Unroll(data, labels, [] * 6, 0, 0)

    max_depth = 4

# формируем заголовки для будущего dataframe (завсят от глубины вложенности json), пока что 4
    column = []
    for i in range(0, max_depth + 1):
        column.append('theme' + str(i))
    column.append('response')
    df_chavo = pd.DataFrame(columns=column)
    Create_Df(labels, max_depth, df_chavo)
     #print(labels)
     # print(df_chavo)
     # считываем переписку
    data_csv = pd.DataFrame()
    data_csv = LoadTrain(data_csv)
    CousinDist(df_chavo, data_csv)
     #response = "Список актуальных акций Вы можете посмотреть, нажав значок «Акции» внизу экрана."
     #ReturnLabel(df_chavo, theme_label, response)
