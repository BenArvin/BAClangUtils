#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os, subprocess, shlex

class ShellUtil(object):

    @classmethod
    def runShell(cls, cmd):
        if cmd == None or isinstance(cmd, str) == False or len(cmd) < 1:
            return None
        output, error = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1).communicate()
        return {'output': output.decode(encoding='utf-8'), 'error': error.decode(encoding='utf-8')}