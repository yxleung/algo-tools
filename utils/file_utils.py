#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def add_line_nu(inputFile, outputFile, separator=' '):
    with open(outputFile, mode='w', encoding='UTF-8') as output:
        with open(inputFile, encoding='UTF-8') as input:
            index = 0
            for line in input:
                attrs = line.split(separator)
                result = attrs[0] + separator + attrs[1] + separator + str(index) + '\n'
                index += 1;
                output.write(result)
                if index % 1000000 == 0:
                    print(index)


def add_line_nu_with_path(path, separator=' '):
    for parent, dirnames, filenames in os.walk(path, followlinks=True):
        for fn in filenames:
            file = os.path.join(parent, fn)
            add_line_nu(file, file + '.out', separator)
