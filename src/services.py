
class functionsCRUD:

        def __init__(self): 
            self.students = []

        def registerStudent(self,student_id,student_name,student_age,student_course,student_state):
            student = {"id": student_id, "name": student_name, "age": student_age, "course": student_course, "state": student_state}
            self.students.append(student)
            print(f"successfully registered {student}")

        def listStudent(self):
            if not self.students:
                print("there are no registered students")
            else:
                for i, s in enumerate(self.students):
                    print(f"{i}.Students: {s['id']} | {s['name']} | {s['age']} | {s['course']} | {s['state']}")

        def searchStudent(self, student_name):
            searchName = student_name.strip().lower()
            for s in self.students:
                if s["name"].lower() == searchName:
                    print(f"Student found: {s['id']} | {s['name']} | {s['age']} | {s['course']} | {s['state']}")
                    return s
                
            print (f"Student not found")
            return None
        
        def updateStudent(self,student_name):
            studentFound = student_name.strip().lower()
            for s in self.students:
                if s["name"].lower() == student_name.strip().lower():
                    studentFound = s
                    break
            if not studentFound:
                print(f"Error: Student with the '{studentFound}' not found")
                return
            
            while True:
                try:

                    newID = int(input(f"new id for '{studentFound['id']}': "))
                    studentFound["name"] = newID
                    newName = str(input(f"new name for '{studentFound['name']}': "))
                    studentFound["name"] = newName
                    newAge = int(input(f"new age for '{studentFound['age']}': "))
                    studentFound["name"] = newAge
                    newCourse = str(input(f"new course for '{studentFound['course']}': "))
                    studentFound["name"] = newCourse
                    newState = str(input(f"new state for '{studentFound['state']}': "))
                    studentFound["name"] = newState
                    print("Student update")

                    break
                except ValueError:
                    print("Error: Introduce un número entero válido.")

        def deleteStudent(self,student_name):

            studentFound = None
            for s in self.students:
                if s["name"].lower() == student_name.strip().lower():
                    studentFound = s
                    break
            if not studentFound:
                print(f"Error: Student with the '{id}' not found")
                return
            
            self.students.remove(studentFound)
            print(f"the student {studentFound} has been removed")