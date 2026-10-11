# Employee Payroll System

A menu-driven Employee Payroll System built using Python. It allows users to manage employee records, record attendance, and calculate salaries based on attendance.

## Features

- Add, view, search, update, and delete employee records.
- Record working days, present days, and absent days.
- Calculate salary based on attendance.
- View employee salary details.
- Store employee data using JSON for persistence.

## Technologies Used

- Python
- JSON

## Project Structure

```text
Employee_Payroll_System/
├── main.py
├── employees.json
└── README.md
```

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/Harsh241329E/Employee_Payroll_System.git
cd Employee_Payroll_System
```

**2. Run the application**

Make sure `employees.json` exists in the project directory, containing `[]` or fictional sample employee records.

```bash
python main.py
```

## Salary Calculation

The net salary is calculated using:

`Net Salary = (Base Salary / Working Days) × Present Days`

## About

This project was created for learning Python programming, functions, data structures, file handling, and JSON-based data storage.

**Author:** Harsh
