sum=0
def returnSum(myDict):
    d=myDict
    for k,v in myDict.items():
        sum=0
        for i in range(0,len(v)):
            sum=sum+v[i]
            d.update({k:sum})
    return d

dict = {'a': [1,2,3], 'b': [4,5,6], 'c': [7,8,9]}
print("Sum :", returnSum(dict))


