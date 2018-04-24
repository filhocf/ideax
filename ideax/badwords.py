import json
import os


class Badword(object):
    blacklist = []

    def __init__(self, datafile=None):
        if datafile:
            self.blacklist = self.load_json(datafile)

    def load_json(self, file):
        with open(file) as f:
            data = json.load(f)
        return [item.lower() for item in data]

    def search_badwords(self, txt):
        txt = txt.lower()
        if set(self.blacklist) & set(txt.split()):
            return True
        return False
