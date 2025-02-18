#!/usr/bin/env python

def add(a, b):  
  return eval("%s + %s" % (a, b))

result = add(input("a="), input('b='))
print("The result is %d." % result)
