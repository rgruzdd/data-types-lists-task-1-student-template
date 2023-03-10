from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    # TODO: Add your code here
    new_list = []
    for i in str_list:
        new_list.append(i)
        if new_list.count(i) > 1:
            new_list.pop()
        new_list.sort()
    return new_list
my_list = ('red', 'white', 'black', 'red', 'green', 'black')

sort_unique_elements(my_list)
