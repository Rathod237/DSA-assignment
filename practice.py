
"merge 2 list of strings 1st and last items  respectively"
def merge_list(list1, list2):
    
    merged_data=""
    j=len(list1)-1
    for i in range(len(list1)):
        str1=str2=""
        if list1[i]:
            str1 = list1[i]
        if list2[j]:
            str2 = list2[j]
        j=j-1
        merged_data+=str1+str2
        #if i<len(list1)-1:
        merged_data+=" "
    return merged_data

#Provide different values for the variables and test your program
list2=["ue", "is", "y", "he"]
list1=["T", "sk", None, "bl"]
merged_data=merge_list(list1,list2)
print(merged_data)