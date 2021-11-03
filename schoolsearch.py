import gen_sets
import search_cmd

def commandline(students):
    while(13):
        command = input("Enter Search:")
        command = command.split(' ')

        if command[0] == "S:" or command[0] == "Student:":
            search_cmd.stln(students, command)
        elif command[0] == "T:" or command[0] == "Teacher:":
            search_cmd.tln(students, command)
        elif command[0] == "B:" or command[0] == "Bus:":
            search_cmd.bus(students, command)
        elif command[0] == "G:" or command[0] == "Grade:":
            search_cmd.grade(students, command)
        elif command[0] == "A:" or command[0] == "Average:":
            search_cmd.average(students, command)
        elif command[0] == "I:" or command[0] == "Info:":
            search_cmd.info(students, command)
        elif command[0] == "C:" or command[0] == "Class:":
            search_cmd.classroom(students, command)
        elif command[0] == "E:" or command[0] == "Enroll:":
            search_cmd.enrollment(students, command)
        elif command[0] == "D:" or command[0] == "Data:":
            search_cmd.analytics(students, command)
        elif command[0] == "Q:" or command[0] == "Quit:":
            print("Exiting Search...")
            break

        else:
            print("Command '{}' not recognized".format(command[0]))


if __name__ == '__main__':
    students = []
    students = gen_sets.generate_sets("list.txt", "teachers.txt")
    commandline(students)
