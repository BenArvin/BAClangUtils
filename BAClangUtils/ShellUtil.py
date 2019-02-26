#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os, subprocess, shlex

class ShellUtil(object):

    @classmethod
    def runShell(cls, cmd):
        if cmd == None or isinstance(cmd, str) == False or len(cmd) < 1:
            return None
        
        cmdOutput = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)

        output = cmdOutput.stdout.read().decode(encoding='utf-8')
        cmdOutput.stdout.close()

        error = cmdOutput.stderr.read().decode(encoding='utf-8')
        cmdOutput.stderr.close()

        cmdOutput.wait()
        return {'output': output, 'error': error}