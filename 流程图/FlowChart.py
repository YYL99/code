# -*- coding: utf-8 -*-
def main():
    for i in range(0, 5):
        if i == 4:
           continue
        else:
            print(i,end="")
    print('\n')
    for j in range(6, 10):
        print(j)


if __name__ == '__main__':
    from pycallgraph import PyCallGraph
    from pycallgraph.output import GraphvizOutput

    with PyCallGraph(output=GraphvizOutput()):
        main()
