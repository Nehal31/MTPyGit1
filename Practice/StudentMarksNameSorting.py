'''


'''

roll_num = [1, 2, 3, 4, 5]
names = ['A', 'B', 'Y', 'X', 'P']
marks = [10, 42, 34, 18, 27]


def sort_by_name():
    global roll_num, names, marks
    zip_list = zip(names, roll_num, marks)
    sorted_zip_list = sorted(zip_list)
    print(sorted_zip_list)


def sort_by_roll():
    global roll_num, names, marks
    zip_list = zip(roll_num, names, marks)
    sorted_zip_list = sorted(zip_list)
    print(sorted_zip_list)


def sort_by_marks():
    global roll_num, names, marks
    zip_list = zip(marks, names, roll_num)
    sorted_zip_list = sorted(zip_list)
    print(sorted_zip_list)


if __name__ == '__main__':
    sort_by_name()
    sort_by_roll()
    sort_by_marks()