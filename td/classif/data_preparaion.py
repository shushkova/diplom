#!/usr/bin/python
# -*- coding: utf-8 -*-
from types import SimpleNamespace as Namespace
import pandas as pd


# создаем метки класса, тут же формируем dataframe [label, theme]
# создаем метки класса
def AddLabel(data, count, n, df):
    # присваем метку
    cnt = count
    tmp = 0
    for i in range(0, len(data)):
        tmp = tmp + 1
        try:
            val = cnt + tmp
            df.loc[-1] = [data[i]['theme'], val]
            df.index = df.index + 1
            data[i].update({"label": val})
            AddLabel(data[i]['questions'], (val) * n, n * 10, df)
        except:
            val = cnt + tmp
            data[i].update({"label": val})
    return

# вытаскиваем метки для каждого объекта
def Unroll(data, labels, temp, n, m):
    for i in range(0, len(data)):
        try:
            while len(str(data[i]['label'])) <= len(str(temp[-1])):
                temp = temp[:-1]
            temp.append(data[i]['label'])
        except:
            temp.append(data[i]['label'])
        try:
            Unroll(data[i]['questions'], labels, temp, n, m)
            temp = temp[:-2]
        except:
            temp.append(data[i]['response'])
            labels.append(temp)
            temp = temp[:-2]


# формирование dataframe [номер темы1, номер темы2, номер темы3,сообщение]
def Create_Df(data, max_depth, df_chavo):
    cnt = 0
    for line in data:
        tmp_cnt = 0
        tmp = [] * 5
        for obj in line:
            if isinstance(obj, int) and tmp_cnt <= max_depth:
                tmp.append(obj)
                tmp_cnt = tmp_cnt + 1
            elif isinstance(obj, int) is False and tmp_cnt <= max_depth:
                while tmp_cnt <= max_depth:
                    tmp.append('None')
                    tmp_cnt = tmp_cnt + 1
                tmp.append(obj)
        df_chavo.loc[-1] = tmp
        df_chavo.index = df_chavo.index + 1
        cnt = cnt + 1
    return
