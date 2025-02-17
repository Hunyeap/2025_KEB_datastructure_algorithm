import csv
import random

try:
    with open("KSEB_students.csv", 'r', encoding="euc-kr") as fp:
        student_list = fp.readlines()
        student_list.remove("이상혁\n")
        student_list.remove("조윤하\n")
        student_list.remove("김철중\n")
        student_list.remove("김현민\n")
        student_list.remove("김찬빈\n")
        for i in range(3):
            random_pick = random.choice(student_list)
            print(random_pick, end = '')
            student_list.remove(random_pick)
        #print(student_list[random.randint(0, len(student_list) - 1)])
except FileNotFoundError as err:
    print(err)