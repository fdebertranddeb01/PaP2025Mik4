import time

def sommeDiv(n : int) -> int :
    res = 1
    i = 2
    while i*i < n :
        if n % i == 0:
            res = res + i
            res = res + n // i
        i = i + 1
    if i*i == n :
        res = res + i
    return res

if __name__ == '__main__':
    print('coucou3')
    #max = int(input("entrez  max : "))
    max = 5000
    start = time.time()
    for n in range(1,max+1) :
        if sommeDiv(sommeDiv(n)) == n :
            print(f"{n} et {sommeDiv(n)} sont amis")
    print(f"temps d'execution : {time.time() - start} s")

