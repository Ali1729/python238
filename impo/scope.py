x =10
from firstfile import fun1,a
from logging import *


import openpyxl

def fun5():
    print("fun5")
    
    
def fun1():
    x = 30
    a =600
    # def sum(x,y):
    #     print("inside sum")
    #     print(x+y)
        
    def fun4():
        global a
        print("innerfun",x)
        print("inner is taking from frist",a)
        
    print("outer fun",x)
    fun4()
    
    # fun5()
    
fun1()


# Scopes
# local - inside same function
# Enclosing= 
# Global 
# Builting

# LEGB
import pyexcel