list1 = input("Enter the first list (comma seperated): ").split(",")
list2 = input("Enter the second list (comma seperated): ").split(",")
intersection = []
#looping through elements in list 1
for element in list1:
    #if element is also in list 2, add element to the intersection list.
    if element in list2 and element not in intersection:
        intersection.append(element)
print("The intersection of the two list are:", intersection)
