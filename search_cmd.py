import search
import print_search

def invalid_argument(extra=None):
    if extra is None:
        print("Invalid Arguments Added")
    else:
        print("Invalid argument: '{}'".format(extra))


def search_st_ln(lname, students, extra=None):
    if extra is None or extra == "B" or extra == "Bus":
        st_result = search.search_ln_student(lname, students)
        print_search.print_st_ln(st_result, extra)
    else:
        invalid_argument(extra)


def search_t_ln(tname, students):
    teacher_result = search.search_ln_teacher(tname, students)
    print_search.print_t_ln(teacher_result)


def search_bus(bus, students):
    try:
        bus_result = search.search_bus(int(bus), students)
        print_search.print_bus(bus_result)
    except Exception as e:
        print("Bus Error: {}".format(e))


def search_grade(grade, students, hl=None):
    try:
        grade_result = search.search_grade(int(grade), students, hl)
        print_search.print_grade(grade_result, hl)
    except Exception as e:
        print("Grade Search Error: {}".format(e))


def search_gpa(grade, students):
    try:
        gpa_result = search.avg_gpa(int(grade), students)
        print_search.print_gpa(gpa_result[0], gpa_result[1])
    except Exception as e:
        print("GPA error: {}".format(e))


def search_num_students(students):
    num_student = search.num_student_grade(students)
    print_search.print_num_student(num_student)


def search_class(classroom, students, teach=None):
    try:
        class_result = search.classroom(int(classroom), students, teach)
        print_search.print_classroom(class_result, teach)
    except Exception as e:
        print("Classroom error: {}".format(e))


def search_enrollment(students):
    enroll = search.num_student_class(students)
    print_search.print_num_student_class(enroll)


def search_analytics(students, type):
    results = []
    if type == "G":
        for i in range(7):
            results.append(search.avg_gpa(i, students))

        print_search.print_gpa_data(results)

    elif type == "T":
        result = search.data_teacher(students)
        print_search.print_teach_data(result)

    elif type == "B":
        results = search.data_bus(students)
        print_search.print_bus_data(results)


def stln(students, command):
    num_command = len(command)
    if num_command == 1:
        print("Please Include Student Last Name and Optional B[us] flag")
    elif num_command == 2:
        search_st_ln(command[1], students)
    elif num_command == 3:
        search_st_ln(command[1], students, command[2])
    else:
        invalid_argument()


def tln(students, command):
    num_command = len(command)
    if num_command == 1:
        print("Please Include Teacher Last Name")
    elif num_command == 2:
        search_t_ln(command[1], students)
    else:
        invalid_argument()


def bus(students, command):
    num_command = len(command)
    if num_command == 1:
        print("Please Include Bus Route")
    elif num_command == 2:
        search_bus(command[1], students)
    else:
        invalid_argument()


def grade(students, command):
    num_command = len(command)
    if num_command == 1:
        print("Please Include Grade Level and optional H[igh]/L[ow] or T[each] <LastName> Value")
    elif num_command == 2:
        search_grade(command[1], students)
    elif num_command == 3:
        if command[2] == "H" or command[2] == "High":
            search_grade(command[1], students, command[2])
        elif command[2] == "L" or command[2] == "Low":
            search_grade(command[1], students, command[2])
        elif command[2] == "T" or command[2] == "Teach":
            search_grade(command[1], students, command[2])
        else:
            invalid_argument(command[2])

    else:
        invalid_argument()


def average(students, command):
    num_command = len(command)
    if num_command == 1:
        print("Please Include Class")
    elif num_command == 2:
        search_gpa(command[1], students)
    else:
        invalid_argument()


def info(students, command):
    if len(command) == 1:
        search_num_students(students)
    else:
        invalid_argument()


def classroom(students, command):
    if len(command) == 1:
        print("Please Include Class")
    elif len(command) == 2:
        search_class(command[1], students)
    elif len(command) == 3:
        if command[2] == "T" or command[2] == "Teach":
            search_class(command[1], students, command[2])
        else:
            invalid_argument(command[2])
    else:
        invalid_argument()


def enrollment(students, command):
    if len(command) == 1:
        search_enrollment(students)
    else:
        invalid_argument()


def analytics(students, command):
    if len(command) == 1:
        print("Please include G/T/B flag")
    if len(command) == 2:
        search_analytics(students, command[1])
    else:
        invalid_argument()
