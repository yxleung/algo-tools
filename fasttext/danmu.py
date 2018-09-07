# -*- coding: utf-8 -*-


import fastText as ft


def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))


#
# model = ft.train_supervised(input='/data/liangyuxin/data/danmu_train_set/train.set', label='__label__', wordNgrams=2,
#                             epoch=25, loss="hs")

# model.save_model('/data/liangyuxin/code/danmu_model/model/danmu_model_01.bin')

# ftz_model = model.quantize(input='/data/liangyuxin/data/danmu_train_set/train.set', retrain=True, qnorm=True,
#                            cutoff=100000)
# ftz_model.save_model('/data/liangyuxin/code/danmu_model/model/danmu_model_01.ftz')

load_clsf = ft.load_model('/data/liangyuxin/code/danmu_model/model/danmu_model_01.bin')

# result1 = load_clsf.test('/data/liangyuxin/data/danmu_test_set/test.set')
# result2 = load_clsf.test('/data/liangyuxin/data/danmu_test_set/test.set')

# print_results(*result1)
# print_results(*result2)