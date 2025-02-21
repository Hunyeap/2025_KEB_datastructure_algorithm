def bubble_sort(a_list):
    list_length = len(a_list) -1
    for i in range(list_length):
        no_swap = True #flag 설정
        for j in range(list_length-i):
            if a_list[j] > a_list[j+1]:
                a_list[j],a_list[j+1] = a_list[j+1], a_list[j]
                no_swap = False
        if no_swap:
            return a_list
    return a_list

a_list = [12, 14, 1, 5]
print(bubble_sort(a_list))