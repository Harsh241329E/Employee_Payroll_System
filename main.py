import json
employees = []
def load_employees():
     global employees
     with open("employees.json","r") as file:
          employees = json.load(file)
def save_employees():
     with open("employees.json","w") as file:
        json.dump(employees,file,indent=4)
def add_employee():
      name = input("Enter employee name: ")
      emp_id = int(input("Enter employee id: "))
      salary = float(input("Enter Salary : "))
      employee = {
           "name" : name,
           "salary": salary,
           "id" : emp_id
    }
      employees.append(employee)
      save_employees()
      input("Employee Added and saved successfully")
def view_employee():
      for employee in employees:
         print(f'{employee["id"]} : {employee["name"]}')
      input("\nPress Enter to Continue")
def search_employee():
      search_name = input("Enter employee name: ")
      for employee in employees:
           if employee["name"] == search_name:
                print("="*4+" Employee FOUND "+"="*4)
                print("ID:",employee["id"])
                print("Name:",employee["name"])
                print("Salary:",employee["salary"])
                input("\nPress Enter to Continue")
                return
           else:
                continue
      input("Employee Not Found \nPress Enter to continue")
def record_attendance():
      emp_id= int(input("Enter Employee ID: "))
      working_day = int(input("Enter Working Days: "))
      present_day = int(input("Enter Present Days: "))
      if(present_day<=working_day):
           absent_day = working_day - present_day
      
           for employee in employees:
                if employee["id"] == emp_id:
                    employee["working_day"] = working_day
                    employee["present_day"] = present_day
                    employee["absent_day"] = absent_day
                    save_employees()
                    print("Attendance Recorded Successfully")
      else:
         print("Enter valid present day")
def generate_sal():
        
        emp_id= int(input("Enter Employee ID: "))
        for employee in employees:   
         if employee["id"] == emp_id:
            if "working_day" not in employee or "present_day" not in employee:
                 print("Please record Attendance First")
                 return
            if employee["working_day"]<=0:
                 print("Working day must be greater than 0")
                 return
             
            print("Name: ",employee["name"])
            print("Working Day: ",employee["working_day"])
            print("Present Day: ",employee["present_day"])
            salary = employee["salary"] / employee["working_day"] * employee["present_day"]
            employee["month_salary"] = round(salary, 2)
            save_employees()
            print("Salary Generated : ",salary)
            print("SAVED SUCCESSFULLY")
def salary_details():
      for employee in employees:
           print("Name : ",employee["name"])
           print("\nSalary : ",employee["salary"])
           print("\nNet Salary : ",employee["month_salary"])
def update_employee():
      emp_id = int(input("Enter Employee ID : "))
      for employee in employees:
           if employee["id"] == emp_id:
                print("Employee Found : ",employee["name"])
                print("1. Update Name")
                print("2. Update Salary")
                choice = int(input("Enter what to update : "))
                if choice == 1:
                     employee["name"] = input("Enter new name: ")
                elif choice == 2:
                        new_salary = float(input("Enter New Salary: "))
                        if new_salary < 0:
                                    print("Salary cannot be negative")
                                    return
                        employee["salary"] = new_salary
                else:
                     print("Invalid choice")
                     return
                save_employees()
                print("Employee updated Successfully")
                return                 
def delete_employee():
      for employee in employees:
            print(f'{employee["id"]} : {employee["name"]}')
      emp_id = int(input("Enter Employee ID : "))
      for employee in employees:    
            if emp_id == employee["id"]:
                confirm = input("Do you want to delete : yes/no : ")
                if confirm.lower() == "yes":
                     employees.remove(employee)
                     save_employees()
                     print("Employee Removed")
                else:
                 print("Deletion cancelled.")
      return
      print("Employee ID not found.")

load_employees()
def main():
 while(1):
    print("====EMPLOYEE PAYROLL SYSTEM====")
    print("1.ADD EMPLOYEE")
    print("2.View Employees")
    print("3.Search Employee")
    print("4.Record Attendance")
    print("5.Generate Salary")
    print("6.View Salary Details")
    print("7.Update Employee")
    print("8.Delete Employee")
    print("9.Exit")
    choice = int(input("Choose an Option : "))
    if(choice==1):
        add_employee()
    elif(choice==2):
        view_employee()
    elif(choice==3):
        search_employee()
    elif(choice==4):
        record_attendance()
    elif(choice==5):
         generate_sal()
    elif(choice==6):
        salary_details()
    elif(choice==7):
        update_employee()
    elif(choice==8):
        delete_employee()
    elif(choice==9):
        break
    else:
        print("ENTER A VALID CHOICE")

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nKeyboard interrupt. Exited cleanly.")

    except Exception:
        import traceback
        print("\nUnexpected error occurred:")
        traceback.print_exc()