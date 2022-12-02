def selection_sort(number_list):
    for i in range(len(number_list)-1):
        smallest_i = i #inital value for smallest index
        print('\nCurrent positions:',number_list)
        print('Current number for comparisons:',number_list[i])

        for q in range(i+1, len(number_list)):
            if(number_list[q] < number_list[smallest_i]):
                print('    {current_num} is smaller than {smallest_num}, updating smallest index'.format(current_num = number_list[q], smallest_num = number_list[smallest_i]))
                smallest_i = q #found smaller value, assigning new smallest index
        
        #swapping larger number for smaller number
        print('Swapping {larger} and {smaller}'.format(larger = number_list[i], smaller = number_list[smallest_i] ))
        temp = number_list[i]
        number_list[i] = number_list[smallest_i]
        number_list[smallest_i] = temp

numbers = [2, 23, 3, 55, 51, 1, 0, 100, 70]
print('\nUnsorted:',numbers)         

selection_sort(numbers)
print('\nSorted:',numbers)