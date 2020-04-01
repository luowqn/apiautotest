#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:luowq
# Data: 2020/3/29 22:01
from Config import Configure
from Signalway import  SwLog,SwExcel
from Common import  TestCase,TestModule,CASE_TYPE_CASE
import glob
import os

gConf = None
gLog = None
gTestCases = []
gPwd = os.path.dirname(os.path.abspath(__file__))

def RunTestCase():
    global  gTestCases,gPwd
    for infile in glob.glob(os.path.join(gPwd+'/testCases/','testcase*.py')):
          os.remove(infile)
    with open(gPwd + '/testCaseTemplate/testCase.py',encoding='utf-8') as f:
         testCaseTemplate = f.read()
    with open(gPwd + '/testCaseTemplate/testModule.py',encoding='utf-8')  as f:
         testModuleTemplate = f.read()

    for i,testCase in enumerate(gTestCases):
        with open(gPwd + '/TestCases/testcase%d.py' % i, 'w', encoding='utf-8') as f:
            tempFilterVars = {}
            tempGetVars = {}
            for j,testModule in enumerate(testCase.testModules):
                filterGetVars = {}
                getVars = []

                if testModule.filterVars:
                    tempFilterVars = {i.split('.')[0]:i.split('.')[1] for i in testModule.filterVars.split('\n') if i}
                if  testModule.getVars:
                    tempGetVars = {i.split('.')[0]:i.split('.')[1] for i in testModule.getVars.split('\n') if i}

                if testModule.getVars:
                    for i  in tempGetVars:
                        if i in tempFilterVars:
                            filterGetVars[tempFilterVars.get(i)] = tempGetVars.get(i)
                        else:
                            getVars.append(tempGetVars.get(i))
                # vars = {"seq1": i+1, "seq2": j + 1, "testMethodDoc": testModule.name, "url": testModule.reqUrl,"bodyfile": testModule.bodyFile,
                #         "no":testModule.no,"respAssertions": ','.join("'" + respAssertion + "'" for respAssertion in respAssertions),
                #         "respOps":','.join("'"+respOp+"'"for respOp in respOps)}
            #     testModuleFile = testModuleTemplate % vars
            #     vars.update(**{"testModule":testModuleFile})
            #     testCaseFile = testCaseTemplate%vars
            # f.write(testCaseFile)


def InitTestCase():
    global  gLog,gConf,gTestCases
    try:
        excel = SwExcel(1,gConf.testCasesFile)
        datas = excel.getRowsToDict()
        varsName = []
        case = None
        for index, d in enumerate(datas):
            if index == 0:
                varsName = [d[i].value for i in range(0, len(d))]
            else:
                data = dict(zip(varsName, [d[i].value for i in range(0, len(d))]))
                caseType = data['type']
                if caseType in CASE_TYPE_CASE:
                    case = TestCase(data["no"],data["name"])
                    gTestCases.append(case)
                else:
                    module = TestModule(**data)
                    case.testModules.append(module)
        print(case)
    except Exception as ex:
        raise ex


def InitLog():
    global  gLog
    gLog =  SwLog('expresswayTestTool.log','INFO')

def InitConf():
    global  gConf
    gConf = Configure('config.yml')