#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fastText as ft

def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))


model = ft.train_supervised(input='/mnt/d/NLP/danmu/train.csv', label='__label__')
#
# model.save_model('d:/NLP/danmu/model/danmu_model.bin')
#
# # model.quantize(input='C:/tmp/danmu/dataset/train.csv', retrain=True, qnorm=True,
# #                cutoff=100000)
# # model.save_model('D:/NLP/fasttext_demo/model/news_model.ftz')
#
#
# # load_clsf = ft.load_model('D:\\NLP\\fasttext_demo\\model\\news_fasttext.model')
#
# result = model.test('c:/tmp/danmu/dataset/a.txt')
#
# print_results(*result)
