def features(n):
    i = 1000
    while i > 0:
        print(n)
        i -= 1

def soManyFeatures(daList):
    if type(daList) is not list:
        raise TypeError

    for item in daList:
        print(item)

    print('aal don!')
