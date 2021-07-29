import random

def binary_search(element, list, start, end):
    
    if start > end:
        return [-1,-1]

    middle = (end+start) // 2

    if element == list[middle]:
        position = middle
        return [element, position]

    elif element > list[middle]:
        return binary_search(element, list, middle+1, end )

    else:
        return binary_search(element, list, start, middle-1 ) 

if __name__=='__main__':
    
    numbers_list = sorted([ random.randint(0,100) for i in range(15)])
    
    print(f' The list is {numbers_list}')

    target= int(input('Please input the number to search: '))

    found = binary_search(target, numbers_list, 0, len(numbers_list)-1)

    if found[1] > -1:
        print(f'The number: {found[0]}, is in position: {found[1]}')
    else:
        print(f'The number {target} is not in list {numbers_list}')
    
