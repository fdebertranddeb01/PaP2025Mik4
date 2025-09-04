import time

def somme_div(n : int) -> int :
    sn = 1
    i = 2
    while i*i < n :
        if n % i == 0:
            sn = sn + i
            sn = sn + (n // i)
        i = i + 1
    if i*i == n :
        sn = sn + i
    return sn

if __name__ == '__main__':
    print('coucou3')
    #max = int(input("entrez  max : "))
    max = 1300
    start = time.time()
    for n in range(1,max+1) :
        sn = somme_div(n)
        sm = somme_div(sn)
        if sm == n :
            print(f"{n} et {sn} sont amis")
    print(f"temps d'execution : {time.time() - start} s")

