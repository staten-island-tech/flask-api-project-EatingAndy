def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("")
    else:
        print(result)
divide(10,0)