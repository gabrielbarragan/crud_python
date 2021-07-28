lista_multiplos_2 = [0,2,4,6,8,10]
lista_multiplos_3 = [0,3,6,9,12,15]

new_list = lista_multiplos_2 + lista_multiplos_3
new_list_2 = lista_multiplos_2*2
new_list_3 = list(range(0,100,4))

new_list.sort()
new_list_2.sort()
modifier= lambda numero: numero*2
modified_list= list(map(modifier, new_list_3)) 

print(modified_list)
print(new_list)
print(new_list_2)
print(new_list_3)
