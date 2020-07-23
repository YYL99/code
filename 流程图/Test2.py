# -*- coding: utf-8 -*-
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import Config
from pycallgraph import GlobbingFilter


class Banana:

    def eat(self):
        pass


class Person:

    def __init__(self):
        self.no_bananas()

    def no_bananas(self):
        self.bananas = []

    def add_banana(self, banana):
        self.bananas.append(banana)

    def eat_bananas(self):
        [banana.eat() for banana in self.bananas]
        self.no_bananas()


def main():
    graphviz = GraphvizOutput()
    graphviz.output_file = 'basic.png'
    config = Config()
    config.max_depth = 5  # 控制最大追踪深度

    with PyCallGraph(output=graphviz, config=config):
        person = Person()
        for a in range(10):
            person.add_banana(Banana())
        person.eat_bananas()


if __name__ == '__main__':
    main()