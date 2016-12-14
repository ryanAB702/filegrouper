import os

from filetypes import *

class FileGrouper(object):
    def __init__(self, dir="", prefix_len=5, types=[]):
        self.directory = dir
        self.prefix_len = prefix_len
        self.type_map = {}

        for filetype in types:
            self.type_map[filetype.typename] = filetype.comp_func

        self.groups = []
        self.walk_directory()

    def walk_directory(self):
        curr_group = FileGroup(self.type_map.keys())

        while not curr_group.full:
            for root, dirs, files in os.walk(self.directory):
                for file in files:
                    if self.group_full(curr_group):
                        curr_group.full = True
                        self.groups.append(curr_group)
                        curr_group = FileGroup(self.type_map.keys())
                    if file.startswith("."):
                        continue
                    if curr_group.empty:
                        if not self.prefix_in_groups(file[:self.prefix_len]):
                            curr_group.prefix = file[:self.prefix_len]
                    if curr_group.prefix_match(file):
                        if not self.group_full(curr_group):
                            self.add_file(curr_group, os.path.join(root, file))
                        else:
                            curr_group.full = True
                            self.groups.append(curr_group)
                            curr_group = FileGroup(self.type_map.keys())

        print


    def group_full(self, group):
        found_empty = False
        group_vars = vars(group)
        for x in self.type_map.keys():
            if not group_vars[x]:
                found_empty = True
        if found_empty:
            return False
        return True

    def add_file(self, group, file):
        for type, func in self.type_map.items():
            if func(file):
                vars(group)[type] = file
                group.empty = False
                return

    def prefix_in_groups(self, prefix):
        for group in self.groups:
            if group.prefix == prefix:
                return True
        return False


class FileGroup(object):
    def __init__(self, file_types=[], prefix=""):
        for x in file_types:
            setattr(self, x, "")

        self.prefix = prefix
        self.full = False
        self.empty = True

    def prefix_match(self, input):
        if input[:len(self.prefix)] == self.prefix:
            return True
        return False




