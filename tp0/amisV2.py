

if __name__ == '__main__':
    print('coucou3')
    #max = int(input("entrez  max : "))
    max = 500
    for n in range(1,max+1) :
        sn = 1
        i = 2
        while i <= n//2:
            if n % i == 0:
                sn = sn + i
            i = i + 1
        sm = 1
        i = 2
        while i <= sn//2:
            if sn % i == 0:
                sm = sm + i
            i = i + 1
        if sm == n :
            print(f"{n} et {sn} sont amis")