
def binary_search(list,n):
    low=0
    upper=len(list)-1
    

    while low<=upper:
        mid=(low+upper)//2
        if list[mid]<n:
            low=mid+1
        elif list[mid]>n:
            upper=mid-1
        else:
            return mid
    return -1

list=[34,3,2,66,7,78987]
list.sort()
n=78987
res=binary_search(list,n)
if res!=-1:
    print('element is found:'+str(res))
else:
    print('element is not found')

