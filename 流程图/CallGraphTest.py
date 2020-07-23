# -*- coding: utf-8 -*-
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

import TempTest


def testNum(key):
    TempTest.testStr(key)
    print("testNum is :", key)


g = GraphvizOutput(output_file=r'./trace.png')
with PyCallGraph(output=g):
    TempTest.testStr("111")
    testNum(222)