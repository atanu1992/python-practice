num = 20
try:
    result = num/2
except ValueError: # This is catch proper value or not
    print('\nThis is not a valid number')
except ZeroDivisionError: # This is catch Zero divisible errors
    print('\nZero division error')
except Exception as ex:  # This is catch all types of errors, Exception is parent class exception
    print(ex)
else:
    print('\nElse :- If try run successfully, then this code will also run, '
          '\n if there is exception, it will not run.')
finally:
    print('\nFinally :- It will run at last, if there is error or no error, '
          '\nit will run always. Execution complete here')