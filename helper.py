#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


class Employee:
    def __init__(self, id, name, salary, age):
        self.id = int(id)
        self.name = name
        self.salary = int(salary)
        self.age = int(age)

    def __str__(self):
        return "{:02d}| {:<25}| Salary: {:<8}| Age: {}".format(
            self.id, self.name, self.salary, self.age
        )


class EmployeesAPI:
    def get_json(self, url):
        r = requests.get(url)
        r.raise_for_status()
        return r.json()


class TerminalColors:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[93m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"

    def disable(self):
        self.BLUE = ""
        self.GREEN = ""
        self.RED = ""
        self.ENDC = ""
        self.BOLD = ""


def GetChar():
    try:
        # for Windows-based systems
        import msvcrt  # If successful, we are on Windows

        return msvcrt.getch()

    except ImportError:
        # For POSIX Compatible OSs
        import tty, sys, termios

        fd = sys.stdin.fileno()
        oldSettings = termios.tcgetattr(fd)

        try:
            tty.setcbreak(fd)
            answer = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

        return answer
