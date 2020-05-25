from lib.employee import Employee


def test_employee_print():
    e1 = Employee(10, "Shahriar E", 123456, 23)
    assert e1.__str__() == "10| Shahriar E               | Salary: 123456  | Age: 23"
    e2 = Employee(8, "Alex Ferguson", 7000000, 9)
    assert e2.__str__() == "08| Alex Ferguson            | Salary: 7000000 | Age: 9"

