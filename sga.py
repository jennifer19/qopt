#!/usr/bin/python

import framework
import sys
import random

class SGA(framework.GA):
    """ The Simple Genetic Algorithm
    Roulette Wheel Selection, 1-point crossover, 1-point mutation
    """

    def __init__(self):
        framework.GA.__init__(self)
        print 'SGA constructor'
        self.Pc = 0.9
        self.Pm = 0.05

    def initialize(self):
        self.population = []
        for i in xrange(self.popsize):
            ind = framework.Individual()
            ind.genotype = ''.join([random.choice(('0','1')) for locus in xrange(self.chromlen)])
            self.population.append(ind)

    def operators(self):
        print 'selection'
        self.population = framework.RouletteSelection(self.population)
        #elitism
        # self.population.pop()
        # self.population.append(self.best)
        print 'crossover'
        self.population = framework.OnePointCrossover(self.population, self.Pc)
        print 'mutation'
        self.population = framework.OnePointMutation(self.population, self.Pm)

if __name__ == '__main__':
    import knapsack
    k = knapsack.Evaluator()
    k.file = 'data/knapsack1.txt'

    sga = SGA()
    sga.evaluator = k
    sga.run()
