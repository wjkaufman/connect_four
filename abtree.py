from math import *

class ABTree:
    '''
    Class for performing ab-pruning on a tree
    
    have it initialize with some depth and a starting node
    then it can proliferate to some depth d according to
    some function
    
    then have it do ab pruning and return best branch
    '''
    
    def __init__(self):
        self.val # value of curent node
        self.children = [] # children branches
    
    def makeChildren(self, depth, func):
        '''
        creates more children from current node value
        using output of func (a list)
        '''
        if depth > 0:
            self.children = []
            for i in func(self.val):
                child = ABTree()
                child.val = i
                child.makeChildren(depth-1, func)
                self.children.append()
        else:
            return 0
    
    def getBest(self, isMax, evalFunc, alpha = -1e99, beta = +1e99):
        '''
        pick the best child node to go to
        alpha: the lower bound for trying to maximize
        beta: the upper bound for trying to minimize
        
        basically, why explore a branch with lower result (when maximizing) when you're guaranteed a better result on another branch?
        '''
        if len(self.children) == 0:
            return evalFunc(self.val)
        else:
            if isMax: # pick branch that maximizes 
                for c in self.children:
                    v = evalFunc(c.val)
                    alpha = max(alpha, v)
                    
            else: # pick branch that minimizes
                
                
            
        
