#PR-2 Boichuk Juliia
def prime_num_generator():
    n = 2
    while True:
        prime = True

        if prime:
            yield n

        for i in range(2, int(n//2)+1):
            if n % 1 == 0:
                prime = False
                break

        n +=1
