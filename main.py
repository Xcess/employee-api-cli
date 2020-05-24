from helper import Employee, EmployeesAPI, GetChar, TerminalColors
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Fetches data from employee API and displays some stats"
    )
    parser.add_argument(
        "-c", "--no-color", action="store_true", help="Disable colored output."
    )
    parser.add_argument(
        "-u",
        "--url",
        default="http://dummy.restapiexample.com/api/v1/employees",
        help="API URL. (Should be compatible with the original employee API",
    )
    args = parser.parse_args()

    terminal_colors = TerminalColors()
    if args.no_color:
        terminal_colors.disable()

    api_handler = EmployeesAPI()
    employees_json = api_handler.get_json(args.url)

    employees = []
    employees_count = 0
    for e in employees_json["data"]:
        employees_count += 1
        employees.append(
            Employee(
                e["id"], e["employee_name"], e["employee_salary"], e["employee_age"]
            )
        )

    average_age = 0
    average_salary = 0

    for e in employees:
        average_age += e.age
        average_salary += e.salary

    average_age = average_age / employees_count
    average_salary = average_salary / employees_count

    print(
        f"Average employee age: {terminal_colors.RED}{average_age:.2f}{terminal_colors.ENDC}"
    )
    print(
        f"Average employee salary: {terminal_colors.RED}{average_salary:.2f}{terminal_colors.ENDC}\n"
    )

    print(
        f"{terminal_colors.BLUE}To see all employees press 'y' ...\n{terminal_colors.ENDC}"
    )

    if GetChar().lower() == "y":
        for e in employees:
            print(e)


if __name__ == "__main__":
    main()
