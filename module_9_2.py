first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']



print('Результат обработки первого списка:',[len(elem_list) for elem_list in first_strings if len(elem_list) >= 5])

print('Результат обработки первого списка:',[(elem_first_list, elem_second_list) for elem_first_list in first_strings
                                            for elem_second_list in second_strings
                                            if len(elem_first_list) == len(elem_second_list)])

print({elem_list: len(elem_list) for elem_list in (first_strings + second_strings) if len(elem_list) % 2 == 0})
