#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


class JSONApi:
    def get_json(self, url):
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
