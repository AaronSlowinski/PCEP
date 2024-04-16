def walk (stop, start=1):
    print (start, end=' ')
    if start +1 < stop:
        walk(stop, start +1)
        
walk (3)
#prints 1,2
