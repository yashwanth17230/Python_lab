def mergesort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0

        while i<len(l)and j<len(r):
            if l[i]<=r[j]:
                arr[k]=l[i]
                i=i+1
                k=k+1
            
            else:
                arr[k]=r[j]
                j=j+1
                k=k+1
            
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1

        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1

def printlist(arr):
    for i in range (len(arr)):
        print(arr[i],end=" ")
    print()

if  __name__ =="__main__":
    
    arr=[12,11,13,5,99]
    print("given array is")
    printlist(arr)
    mergesort(arr)
    print("sorted array")
    printlist(arr)
           
    
