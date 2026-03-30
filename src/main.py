from services import functionsCRUD
import utils.validation as val
from data.storage import DataCSV

def main_menu():

    crud = functionsCRUD()
    dataStudent = DataCSV(crud.students)
    archivePath = "src/data/DataCSV.csv"

    while True:
        print("Menu")
        print("1. register Student")
        print("2. list students")
        print("3. search student")
        print("4. update student")
        print("5. remove student")
        print("6. save csv")
        print("7. load csv")
        print("8. exit")

        option = input("Choose your option: ")

        match option:

            case "1":
                print("\nRegister the information of the student:")
                student_id = val.requestData("Student ID: ", val.validationInt)
                student_name = val.requestData("Student name: ", val.validationString)
                student_age = val.requestData("Student age: ", val.validationInt)
                student_course = val.requestData("Student course: ", val.validationString)
                student_state = val.requestData("Student state: ", val.validationString)
                crud.registerStudent(student_id,student_name,student_age,student_course,student_state)
            
            case "2":
                crud.listStudent()
            
            case "3":
                search_name = input("Enter the name of the student to search: ")
                crud.searchStudent(search_name)
            
            case "4":
                search_name = input("Enter the name of the student you want to: ")
                crud.updateStudent(search_name)
            
            case "5":
                search_name = input("Enter the name of the student you want to removed: ")
                crud.deleteStudent(search_name)

            case "6":
                dataStudent.students = crud.students
                dataStudent.saveCsv(archivePath)
            
            case "7":
                dataStudent.students = crud.students
                dataStudent.manageCVS(archivePath)
                crud.students = dataStudent.students


            case "8":
                print("leaving the system")
                exit()

if __name__ == "__main__":
    # Ensure the script only runs if executed directly
    main_menu()