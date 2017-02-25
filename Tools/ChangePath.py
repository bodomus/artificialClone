import sys
import os
import re




def parse_path_variable():

    pythonre = r'\\python2.'
    check = re.compile(pythonre)

    l = os.environ['PATH']
    paths = l.split(os.pathsep)
    for el in paths:
        m = check.match(el)
        print('path is %s', el)




parse_path_variable()
