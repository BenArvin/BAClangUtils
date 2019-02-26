#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
sys.path.append('../')

from BAClangUtils.RawTokenUtil import RawTokenUtil

if __name__ == '__main__':
    util = RawTokenUtil()
    output, error = util.parse('~/Desktop/TestProject/TestProject/ViewController.m')
    print('output: ' + str(output))
    print('error: ' + str(error))