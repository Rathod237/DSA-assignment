def find_decreasing_start(list1,start,end):
    
    #Remove pass and write your logic here
    while start<=end:
        mid=start+(end-start)//2 
        if (mid>0 and mid<end):
            if list1[mid]>list1[mid-1] and list1[mid]>list1[mid+1]:
                return mid+1 
            elif list1[mid-1]>list1[mid]:
                end=mid-1
            else:
                start=mid+1
        elif mid==0:
            if list1[0]>list1[1]:
                return 0+1  
            else:
                return 1 +1
        else:
            if mid==end:
                if list1[end]>list1[end-1]:
                    return end+1 
                else:
                    return end-1 +1 

#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
result=find_decreasing_start(list1,start,end)
print("The index position at which the increasing array starts decreasing is:",result)
