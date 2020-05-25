#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
