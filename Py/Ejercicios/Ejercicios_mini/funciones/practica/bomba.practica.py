i=5

def callback(i):
    if i == 0:
        print("¡¡BUM!!")
    else:
        print(i)
        i -= 1
        callback(i)
    
callback(i)