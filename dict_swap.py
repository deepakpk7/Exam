d={1:"One",2:"Two",3:"Three"}
def num(d):
    # d1={}
    # for i in d:
    #     d1[d[i]]=i
    # return d1
    
    return {value:key for key,value in d.items()}

print(num(d))