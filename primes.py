def getFactors(number):
    answer = []
    for i in range(1,number):
        if number % i == 0:
            answer.append(i)
    return (answer)

def isPrime(number):
    factors = getFactors(number)
    if len(factors) == 1:
        return True
    else:
        return False

working = True
while working:
    n = raw_input('Please enter a number to test, or e to exit')
    if n[0] == 'e' or 'E':
        working == False
    if n.isdigit():
        n= int(n)
        if isPrime(n):
            print ('{0} is a prime number'.format(n))
        else:
            print ('{0} is a composite number'.format(n))
            for j in getFactors(n):
                print('{0} is a factor of {1}'.format(j,n))
