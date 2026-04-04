from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func, and_
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sql:///finalPracDB.db")

Base = declarative_base()

# Creating models for 'Department' and 'Employee'

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Float)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="employees")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Inserting of the data into the tables

d1 = Department(name= "IT")
d2 = Department(name = "HR")
d3 = Department(name = "Finance")

employeesTab = [
    Employee(name="Ram", salary= 500000, department = d1),
    Employee(name = "Shyam", salary = 60000, department = d1),
    Employee(name = "Hari", salary = 40000, department = d2),
    Employee(name="Sita", salary=70000, department=d1),
    Employee(name="Gita", salary=30000, department=d2),
    Employee(name="John", salary=90000, department=d3),

]

session.add_all([d1, d2, d3])
session.add_all(employeesTab)
session.commit()


# Task 1: Basic querying
# Print all employees with department names

allEmployees = session.query(Employee.name, Department.name).join(Department).all()

for emp_name, dept_name in allEmployees:
    print(emp_name, "->", dept_name)


# Task 2: Filter + Joining

employee = (
             session.query(Employee.name, Employee.salary).join(Department)
             .filter(and_(Department.name == 'IT', Employee.salary > 50000 ))
             .all()
             
           )

for emp_name, emp_salary in allEmployees:
    print(f"{emp_name} has the salary of {emp_salary}")


# Task 3: Group By
# Count Employees in each department

empIneachDepart = (
            session.query(Department.name, func.count(Employee.id))
            .join(Department)
            .group_by(Department.id)
            .all()
)

for dept_name, count in empIneachDepart:
    print(f"{dept_name} has {count} employees")


# Task 4:
# Departments with more than 2 employees

moreThanTwo = (
               session.query(Department.name, 
               func.count(Employee.id)).label("Employee Count")
               .join(Employee)
               .group_by(Department.id)
               .having(func.count(Employee.id) > 2)
               .all()
               )

for dept, count in moreThanTwo:
    print(f"{dept} has {count} employees")


