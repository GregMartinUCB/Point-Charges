# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 13:24:28 2014

@author: Greg Martin
"""

import numpy as np
import matplotlib as plt
from math import factorial

class E():
    cube=np.array([[1.,1.,1.],[-1.,1.,1.],[1.,-1.,1.],[1.,1.,-1.],[-1.,-1.,1.],
                  [1.,-1.,-1.],[-1.,1.,-1.],[-1.,-1.,-1.]]  )
    
    
    def field(self,point):
        eField=0.
        for i in range(8):
           r=point-self.cube[i]
           eField+= (r/np.linalg.norm(r))/(r.dot(r))
           #print eField
        
        return eField
        
    
    
Q=E()
print Q.field([.01,0,0])
print Q.field([.01,.01,0])
print Q.field([.01,0.1,0.1])