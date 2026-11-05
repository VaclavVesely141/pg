def my_range(start,stop,step):
    vysledek = []
    x =start
    while(x < stop):
        start += x
        vysledek.append(x)
        x += step
    return vysledek
def my_enum(iterable, start):
    vysledek = []
    for i in range(x+start,len(iterable[x])):
        vysledek.append(x+start, iterable[x])
        start +=1
    return vysledek

if __name__=="__main__":
    print(my_range(1,10,2))