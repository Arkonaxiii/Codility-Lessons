def fizzbuzz():    
   
    for i in range(1,21):
        msg = ''
        if i%3 == 0:
            msg += "Fizz"
        if i%5 == 0:
            msg += "Buzz"
        print msg or str(i)
