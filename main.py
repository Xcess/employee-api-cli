from lib.termcolor import TerminalColors
from lib.employee import Employee
from lib.api import JSONApi
import argparse


def _init():
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
    parser.add_argument(
        "-a",
        "--show-employees",
        action="store_true",
        help="Show all employees (Disables interactive mode).",
    )
    args = parser.parse_args()

    terminal_colors = TerminalColors()
    if args.no_color:
        terminal_colors.disable()

    return args, terminal_colors


def show_employees(employees):
    for e in employees:
        print(e)


def main():
    args, terminal_colors = _init()

    api_handler = JSONApi()
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

    if args.show_employees:
        show_employees(employees)
        return

    print(
        f"{terminal_colors.BLUE}To see all employees enter 'y' otherwise press enter to exit ...\n{terminal_colors.ENDC}"
    )

    if input().lower() == "y":
        for e in employees:
            print(e)


if __name__ == "__main__":
    main()
