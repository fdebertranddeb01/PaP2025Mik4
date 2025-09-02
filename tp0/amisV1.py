

if __name__ == '__main__':
    print('coucou3')
    #max = int(input("entrez max : "))
    max = 500
    for n in range(1,max+1) :
        sn = 1
        i = 2
        while i <= n//2:
            if n % i == 0:
                sn = sn + i
            i = i + 1
        for m in range(1,max+1) :
            sm = 1
            i = 2
            while i <= m//2:
                if m % i == 0:
                    sm = sm + i
                i = i + 1
            if sm == n and sn == m :
                print(f"{n} et {m} sont amis")