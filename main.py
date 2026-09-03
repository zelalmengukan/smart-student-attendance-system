def add_students():
    students = []
    num_students = int(input("How many students are in the class?: "))
    
    for i in range(num_students):
        name = input(f"Enter name for student #{i + 1}: ")
        students.append(name)
        
    return students


def take_attendance(students):
    present = []
    absent = []
    
    for student in students:
        status = input(f"Is {student} present? (Y/N): ")
        if status == "Y" or status == "y":
            present.append(student)
        else:
            absent.append(student)
            
    return present, absent


def generate_report(present, absent):
    total = len(present) + len(absent)
    
    print("\n--- ATTENDANCE REPORT ---")
    print("Total Students:", total)
    print("Present Count:", len(present))
    print("Absent Count:", len(absent))
    
    print("\nPresent Students:")
    for student in present:
        print("-", student)
        
    print("\nAbsent Students:")
    for student in absent:
        print("-", student)


# Run Application
student_list = add_students()
present_list, absent_list = take_attendance(student_list)
generate_report(present_list, absent_list)
