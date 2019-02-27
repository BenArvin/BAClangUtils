#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os, re
from BAClangUtils.ShellUtil import ShellUtil

class RawTokenUtil(object):
    def __init__(self):
        super(RawTokenUtil, self).__init__()
    
    def __resolveLine(self, lineContent):
        if lineContent == None or isinstance(lineContent, str) == False or len(lineContent) < 1:
            return None

        if re.match("^unknown ('|\"){1,1}(.*)?$", lineContent, re.S) != None:
            return None

        tmpLineContent = lineContent
        uncleanContent = None
        uncleanContentFinds = re.finditer('\[UnClean=(.|\s)*?\]', tmpLineContent)
        for findItem in uncleanContentFinds:
            uncleanContent = tmpLineContent[findItem.start()+10: findItem.end()-2]
            break
        
        tmpLineContent = tmpLineContent.replace('[StartOfLine]', '')
        if uncleanContent != None:
            tmpLineContent = re.sub('\[UnClean=(.|\s)*?\]', '', tmpLineContent)
        
        blankIndexs = []
        blanksRegFinds = re.finditer('( |\t)', tmpLineContent)
        for blankItem in blanksRegFinds:
            blankIndexs.append(blankItem.start())

        lineClass = tmpLineContent[0: blankIndexs[0]]

        locationTmp = tmpLineContent[blankIndexs[len(blankIndexs) - 1] + 1 : len(tmpLineContent) - 1]
        colonIndexs = []
        colonFinds = re.finditer(':', locationTmp)
        for colonItem in colonFinds:
            colonIndexs.append(colonItem.start())
        locationLine = int(locationTmp[colonIndexs[0] + 1: colonIndexs[1]])
        locationColumn = int(locationTmp[colonIndexs[1] + 1: len(locationTmp) - 1]) - 1

        tmpLineContent = tmpLineContent[blankIndexs[0]: blankIndexs[len(blankIndexs) - 1]]
        tmpLineContent = re.sub('^(\t| )*?(\'|\"){1,1}', '', tmpLineContent)
        tmpLineContent = re.sub('(\'|\"){1,1}(\t| )*?$', '', tmpLineContent)

        result = {}
        result['content'] = tmpLineContent
        result['unCleanContent'] = uncleanContent if uncleanContent != None else tmpLineContent
        result['class'] = lineClass
        result['line'] = locationLine
        result['column'] = locationColumn
        return result
    
    def parse(self, sourcePath):
        if sourcePath == None or isinstance(sourcePath, str) == False or len(sourcePath) == 0:
            return None, None
        if os.path.exists(sourcePath) == False or os.path.isdir(sourcePath) == True:
            return None, None

        cmdResult = ShellUtil.runShell('clang -Xclang -dump-raw-tokens ' + sourcePath)

        if cmdResult == None:
            return None, None
        cmdResultOutput = cmdResult['output']
        cmdResultError = cmdResult['error']

        lineRegExpress = '(.|\n|\s)*?Loc=<(.)*?:[0-9]*?:[0-9]*?>\\n'
        
        outputResult = []
        if cmdResultOutput != None:
            outputLineFinds = re.finditer(lineRegExpress, cmdResultOutput)
            for lineItem in outputLineFinds:
                lineContent = cmdResultOutput[lineItem.start(): lineItem.end()]
                resultTmp = self.__resolveLine(lineContent)
                if resultTmp != None:
                    outputResult.append(resultTmp)

        errorResult = []
        if cmdResultError != None:
            errorLineFinds = re.finditer(lineRegExpress, cmdResultError)
            for lineItem in errorLineFinds:
                lineContent = cmdResultError[lineItem.start(): lineItem.end()]
                resultTmp = self.__resolveLine(lineContent)
                if resultTmp != None:
                    errorResult.append(resultTmp)

        return outputResult, errorResult