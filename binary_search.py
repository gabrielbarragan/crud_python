import random

def binary_search(element, list, start, end):
    
    if start > end:
        return False

    middle = (end+start) // 2

    if element == list[middle]:
        return True

    elif element > list[middle]:
        return binary_search(element, list, middle+1, end )

    else:
        return binary_search(element, list, start, middle-1 ) 

if __name__=='__main__':
    # numbers_list = sorted([ random.randint(0,100) for i in range(15)])
    numbers_list = [4, 5, 10, 22, 34, 55, 60, 62, 73, 80, 99 ]
    
    target= int(input('Please input the number to search: '))

    found = binary_search(target, numbers_list, 0, len(numbers_list)-1)
    if found:
        print(f'The number {target} is in list {numbers_list}')
    else:
        print(f'The number {target} is not in list {numbers_list}')
    
