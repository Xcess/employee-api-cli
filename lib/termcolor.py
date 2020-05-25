#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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