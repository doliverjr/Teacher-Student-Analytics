#File for searching through students

#Input: lname, students
#    lname = last name of student to lookup
#    students = list of students jsons
#
#output: matching
#    matching = list of matching students jsons

def search_ln_student(lname, students):
    matching = []
    for student in students:
        if student['StLastName'] == lname:
            matching.append(student)

    return matching


# Input: lname, students
#    lname = last name to lookup
#    students = list of students jsons
#
#output: matching
#    matching = list of matching students jsons
def search_ln_teacher(lname, students):
    matching = []
    for student in students:
        if student['TLastName'] == lname:
            matching.append(student)

    return matching


#Input: bus, students
#    bus = bus route to lookup
#    students = list of students jsons
#
#output: matching
#    matching = list of matching students jsons
def search_bus(bus, students):
    matching = []
    for student in students:
        if student['Bus'] == bus:
            matching.append(student)

    return matching


def find_teacher(grade, students):
    matching = []
    for student in students:
        if student['Grade'] == grade:
            LNTeach = student['TLastName']
            FNTeach = student['TFirstName']
            teacher = {'TLastName': LNTeach, 'TFirstName': FNTeach}

            if teacher not in matching:
                matching.append(teacher)

    return matching


#Input: grade, students
#    grade = grade to lookup
#    students = list of students jsons
#
#output: matching
#    matching = list of matching students jsons
def search_grade(grade, students, hl=None):
    matching = []
    min = 4.0
    max = 0

    if hl=="T" or hl=="Teach":
        matching = find_teacher(grade, students)
    else:
        for student in students:
            if student['Grade'] == grade:
                if hl is None:
                    matching.append(student)
                elif hl == "H" or hl == "High":
                    if (float(student['GPA']) > max):
                        matching = []
                        max = float(student['GPA'])
                        matching.append(student)
                    elif (float(student['GPA']) == max):
                        matching.append(student)

                elif hl == "L" or hl == "Low":
                    if (float(student['GPA']) < min):
                        matching = []
                        min = float(student['GPA'])
                        matching.append(student)
                    elif (float(student['GPA']) == min):
                        matching.append(student)

    return matching


#Input: grade, students
#    grade = grade to lookup
#    students = list of students jsons
#
#output: [grade, gpa]
def avg_gpa(grade, students):
    num_student = 0
    total = 0
    avg = 0
    for student in students:
        if student['Grade'] == grade:
            num_student += 1
            total += float(student['GPA'])

    try:
        avg = round(total/num_student, 2)
    except ZeroDivisionError:
        avg = 0

    return [grade, avg]


#Input:students
#    students = list of students jsons
#
#output: number of students by grade
def num_student_grade(students):
    num = [0, 0, 0, 0, 0, 0, 0]
    for student in students:
        num[student['Grade']] +=1

    return num


def num_student_class(students):
    enroll = {}
    for student in students:
        key = student['Classroom']
        if key in enroll:
            enroll[key] += 1
        else:
            enroll[key] = 1

    return enroll


def classroom(classroom, students, t=None):
    matching = []
    teachers = []

    if t is None:
        for student in students:
            if student['Classroom'] == classroom:
                matching.append(student)

    else:
        for student in students:
            if student['Classroom'] == classroom:
                if student['TLastName'] not in teachers:
                    matching.append(student)
                    teachers.append(student['TLastName'])

    return matching


def data_teacher(students):
    gpa_teacher = {}
    num_student_teach = {}

    for student in students:
        teacher = student['TLastName']
        gpa = float(student['GPA'])
        if teacher not in gpa_teacher:
            gpa_teacher[teacher] = gpa
            num_student_teach[teacher] = 1
        else:
            gpa_teacher[teacher] += gpa
            num_student_teach[teacher] += 1

    for teach in gpa_teacher:
        if gpa_teacher[teach]:
            gpa_teacher[teach] /= num_student_teach[teach]

    return gpa_teacher


def data_bus(students):
    gpa_bus = {}
    num_student_bus = {}

    for student in students:
        bus = student['Bus']
        gpa = float(student['GPA'])
        if bus not in gpa_bus:
            gpa_bus[bus] = gpa
            num_student_bus[bus] = 1
        else:
            gpa_bus[bus] += gpa
            num_student_bus[bus] += 1

    for bus in gpa_bus:
        if gpa_bus[bus]:
            gpa_bus[bus] /= num_student_bus[bus]

    return gpa_bus

