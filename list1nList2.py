def intersection(list1, list2):
    result = []
    #looping through elements in list1
    for element in list1:
        #checking if the elements are also in list2
        #if yes, then we append the element to result!
        if element in list2:
            result.append(element)
    return result
#asking input from the user seperated by commas.
list1 = input("Enter the first list (comma seperated): ").split(",")
list2 = input("Enter the first list (comma seperated): ").split(",")
print(intersection(list1,list2))