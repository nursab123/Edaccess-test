'''def ounces_convert():
    grams = int(input())
    ounces = int(28.349 * grams)
    print(ounces)
ounces_convert()'''#task 1


'''def temperature_convert():
    F = int(input())
    C = (5/9)*(F-32)
    print(C)
temperature_convert()'''#task 2


'''def animal_counter():
    #x+y=heads
    #2x+4y=legs
    heads=35
    legs=94
    x=(4*heads-legs)//2
    y=heads-x
    print(x,y)
animal_counter()'''#task 3


'''def filter_prime(numbers):  
    def is_prime(n):  
        if n <= 1:    # not a prime number  
            return False  
        for i in range(2,n):  
            if n % i == 0:    # no remainder, then not prime  
                return False  
        return True   
    
    primes = []    # empty list to store prime numbers  
    for num in numbers:  
        if is_prime(num):  
            primes.append(num)  
    return primes  
print(filter_prime(['type a list of numbers here']))'''#task 4