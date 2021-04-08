# !/usr/bin/env python


def pyout(*args,**kwargs):
    if kwargs['end']:
        print(args[0]+kwargs['end'])   
    

if __name__ == '__main__':
    pyout('Hola', end='.', flush='*')
