"""
Names of Group 8 Members
1. Kuete Nkwentamo Valdes UBa22E0294
2.Bongnteh Romarick Ndzelen UBa22E0276
3.Bongkiyung Pelane Tardzenyuy UBa22E0275
4.Awankem Benjamin UBa22E0269
5.Mokia Liticia Nyaven UBa22E0301
6.Betanga Calmin UBa22E0273
7.Awah Hope UBa22E0267
"""

My_List = input("Enter a list of Strings:  ").split(",")
#we then compare the first and second element 
for i in range(len(My_List)):
    for j in range(i+1, len(My_List)):
        #check if the first is greater than the second, then swapp
        if My_List[i] > My_List[j]:
            My_List[i], My_List[j] = My_List[j], My_List[i]
print(My_List )