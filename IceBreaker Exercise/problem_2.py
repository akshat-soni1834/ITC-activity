def radiation(n):
    if (n<3*10**9):
        return ('Radio Waves')
    elif (3*10**9<=n<3*10**12):
        return ('Microwaves')
    elif (3*10**12<=n<4.3*10**14):
        return ('Infrared Light')
    elif (4.3*10**14<=n<7.5*10**14):
        return ('Visible light')
    elif (7.5*10**14<=n<3*10**17):
        return ('Ultraviolet Light')
    elif (3*10**17<=n<3*10**19):
        return ('X-Rays')
    elif (3*10**19<=n<10000000000000000000000000000000):
        return ('Infrared Light')
n=int(input())
print(radiation(n)) 