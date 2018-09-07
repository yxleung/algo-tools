#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


def count_lines(file):
    count = 0
    with open(file, 'rb') as f:
        while True:
            buffer = f.read(1024 * 512)
            if not buffer:
                break
            count += buffer.count('\n'.encode())
    return count


def merge_file(files, output):
    with open(output, mode='wb') as output:
        for file in files:
            with open(file, mode='rb') as f:
                while True:
                    buffer = f.read(1024 * 512)
                    if not buffer:
                        break
                    output.write(buffer)
            output.write('\n'.encode())


def write_test(file):
    with open(file, mode='w', encoding='utf-8') as output:
        for i in range(2000000):
            output.write('我操 __label__粗口\n')


def count_training_set():
    b = datetime.datetime.now()
    print('begin:', b)
    result = count_lines('d:/NLP/danmu/train.csv')
    e = datetime.datetime.now()
    print('end:', e)
    print('use time:', (e - b))
    print('total lines:', result)


if __name__ == '__main__':
    # b = datetime.datetime.now()
    # print('Begin:', b)
    # # result = count_lines('C:\\tmp\\danmu\\dataset\\illegal_raw.csv')
    # # print(result)
    # merge_file(['D:\\NLP\\danmu\\dataset\\legal\\legal.csv', 'D:\\NLP\\danmu\\dataset\\illegal\\illegal.csv'], 'D:\\NLP\\danmu\\dataset\\total_dataset.csv')
    # e = datetime.datetime.now()
    # print('End:', e)
    # print(e - b)

    # write_test('C:\\tmp\\danmu\\dataset\\b.txt')
    count_training_set()
