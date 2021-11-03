#File for printing search results
import collections

def print_st_ln(students, bus=None):
    print("--Student LN Results--")
    if len(students):
        if bus:
            for student in students:
                print("{}, {}, {}".format(student['StLastName'],
                                              student['StFirstName'],
                                              student['Bus']))
        else:
            for student in students:
                print("{}, {}, {}, {}, {}, {}".format(student['StLastName'],
                                                  student['StFirstName'],
                                                  student['Grade'],
                                                  student['Classroom'],
                                                  student['TLastName'],
                                                  student['TFirstName']))
    else:
        print("No Results Found")


def print_t_ln(students):
    print("--Teacher LN Results--")
    if len(students):
        for student in students:
            print("{}, {}".format(student['StLastName'], student['StFirstName']))
    else:
        print("No Results Found")


def print_bus(students):
    print("--Bus Results--")
    if len(students):
        for student in students:
            print("{}, {}, {}, {}".format(student['StLastName'],
                                          student['StFirstName'],
                                          student['Grade'],
                                          student['Classroom']))
    else:
        print("No Results Found")


def print_grade(students, hl=None):
    print("--Grade Results--")

    if hl is None:
        if len(students):
            for student in students:
                print("{}, {}".format(student['StLastName'], student['StFirstName']))
        else:
            print("No Results Found")
    elif hl=="Teach" or hl=="T":
        if len(students):
            for teacher in students:
                print("{}, {}".format(teacher['TLastName'], teacher['TFirstName']))
        else:
            print("No Results Found")

    else:
        if len(students):
            for student in students:
                print("{}, {}, {}, {}, {}, {}".format(student['StLastName'],
                                                  student['StFirstName'],
                                                  student['GPA'],
                                                  student['TLastName'],
                                                  student['TFirstName'],
                                                  student['Bus']))
        else:
            print("No Results Found")


def print_gpa(grade, gpa):
    print("--GPA Results--")
    print("{}, {}".format(grade, gpa))


def print_num_student(num):
    print("--Number of Students Results--")
    for grade in range(7):
        print("{}: {}".format(grade, num[grade]))


def print_classroom(students, teach=None):
    print("--Classroom Results--")
    if teach is None:
        for student in students:
            print("{}, {}".format(student['StLastName'], student['StFirstName']))
    else:
        for student in students:
            print("{}, {}".format(student['TLastName'], student['TFirstName']))


def print_num_student_class(classes):
    print("--Enrollment Results--")
    od  = collections.OrderedDict(sorted(classes.items()))

    for classroom, number in od.items():
        print("Classroom {}: {}".format(classroom, number))


def print_gpa_data(results):
    print("--GPA by Grade--")
    for grade in results:
        print("Grade: {}, GPA: {}".format(grade[0], grade[1]))


def print_teach_data(results):
    od = collections.OrderedDict(sorted(results.items()))
    print("--GPA by Teacher--")
    for teacher, gpa in od.items():
        print("Teacher: {}, GPA: {}".format(teacher, round(gpa, 2)))\


def print_bus_data(results):
    od = collections.OrderedDict(sorted(results.items()))
    print("--GPA by Bus--")
    for bus, gpa in od.items():
        print("Bus: {}, GPA: {}".format(bus, round(gpa, 2)))
