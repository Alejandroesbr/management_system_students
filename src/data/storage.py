import csv

class DataCSV:
    def __init__(self, students):
        self.students = students
        
    def saveCsv(self, path,):
        try:
            if not self.students:
                print("Empty data.")
                return
            
            with open(path, 'w', newline='', encoding='utf-8') as archive:
                writer = csv.DictWriter(archive,fieldnames=["id","name","age","course","state"])
                writer.writeheader()
                writer.writerows(self.students)

            print(f"Students data is save in {path}")
        except PermissionError:
            print("Error: Archive block or without permission.")

    def loadCsv(self, path):
        validStudents = []
        errors = 0
        
        try:
            with open(path, mode='r', encoding='utf-8') as archive:
                reader = csv.DictReader(archive)
                
                if reader.fieldnames != ['id','name','age', 'course', 'state']:
                    print("Error: invalid value.")
                    return None

                for row in reader:
                    try:
                        if not all(row.values()): raise ValueError
                        
                        id = int(row['id'])
                        name = row['name'].strip()
                        age = int(row['age'])
                        course = (row['course'])
                        state = (row['state'])

                        if id < 0 or age < 0: raise ValueError
                        
                        validStudents.append({
                            'id': id,'name': name,'age': age, 'course': course, 'state': state
                        })
                    except (ValueError, TypeError, KeyError):
                        errors += 1

            if errors > 0:
                print(f"Warning: {errors} in rows invalid.")
            return validStudents

        except FileNotFoundError:
            print(f"Error: not found {path}.")
        except Exception as e:
            print(f"Error unexpected: {e}")
        return None
    
    def manageCVS(self, path):
        newStudent = self.loadCsv(path)
        if newStudent is None:
            return

        opcion = input("¿Overwrite actual data? (Y/N): ").strip().upper()
        
        if opcion == 'S':
            self.students = newStudent
            print(f"Data overwrited in {len(newStudent)}.")
        else:

            for new in newStudent:
                found = False
                for actual in self.students:
                    if actual['name'].lower() == new['nombre'].lower():
                        actual['age'] += new['age']
                        actual['id'] = new['id']
                        actual['course'] = new['course']
                        actual['state'] = new['state']
                        found = True
                        break
                if not found:
                    self.students.append(new)
            print(f"Resumen: Fusión completada.")