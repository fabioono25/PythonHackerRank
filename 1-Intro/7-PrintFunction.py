if __name__ == '__main__':
    n = int(input())

    out = ''
    for x in range(n+1):
        out += str(x)
    
    print(out[1:])

    #outra alternativa
    print(*range(1,n+1),sep='')