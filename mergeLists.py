def merge(a, b):
    num = min(len(a), len(b))
    result = [None]*(num*2)
    result[::2] = a[:num]
    result[1::2] = b[:num]
    result.extend(a[num:])
    result.extend(b[num:])
    return result



def main():
    a = (1,2,4,5,2,5,2,9)
    b = (3,5,2,6,3,7,4,7,3)
    print(merge(a,b))



main()
