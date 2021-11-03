# Input: fname
#    fname = file name of students
#
# output: students
#    students = list of students as a dictionary
def generate_students(fname):
    students = []
    with open(fname, 'r') as f:
        for line in f:
            cur_student = line[:-1].strip().split(',')
            students.append({'StLastName': cur_student[0],
                             'StFirstName': cur_student[1],
                             'Grade': int(cur_student[2]),
                             'Classroom': int(cur_student[3]),
                             'Bus': int(cur_student[4]),
                             'GPA': cur_student[5],
                             'TFirstName': 0,
                             'TLastName': 0})

    return students


# Input: fname
#    fname = file name of teachers
#
# output: teachers
#    teachers = list of teachers as a dictionary
def generate_teachers(fname):
    teachers = []
    with open(fname, 'r') as f:
        for line in f:
            curr_teacher = line[:-1].strip().split(',')
            teachers.append({'TLastName': curr_teacher[0],
                             'TFirstName': curr_teacher[1],
                             'Classroom': int(curr_teacher[2])})

    return teachers

def search_teacher(teachers, room):
    TLast = ""
    TFirst = ""

    for teacher in teachers:
        if teacher['Classroom'] == room:
            TLast = teacher['TLastName']
            TFirst = teacher['TFirstName']

    return [TLast, TFirst]


def combine_student_teacher(students, teachers):
    combined = []
    for student in students:
        teacher = search_teacher(teachers, student['Classroom'])
        student['TLastName'] = teacher[0]
        student['TFirstName'] = teacher[1]


def generate_sets(studentf, teacherf):
    teachers = []
    students = []

    try:
        students = generate_students(studentf)
        teachers = generate_teachers(teacherf)
    except Exception as e:
        print("Error generating dictionaries\n\t{}".format(e))
        exit(1)

    combine_student_teacher(students, teachers)

    return students
