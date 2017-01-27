import os

from filetypes import *
import filetypes

class FileGrouper(object):
    def __init__(self, dir="", prefix_len=5, types=[]):
        self.directory = dir
        self.prefix_len = prefix_len
        self.type_map = {}
        self.outlier_dict = dict() #String (prefix) : list[file if type not in types or group already full]
        #For each prefix; do you already have a group with that prefix
        #Is the file already in the group

        for filetype in types:
            self.type_map[filetype.typename] = filetype.comp_func

        #self.groups = []
        self.groups = dict()
        self.walk_directory()


    def walk_directory(self):
        #curr_group = FileGroup(self.type_map.keys())

        #while not curr_group.full:
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.startswith("."):
                    continue
                pref = file[:self.prefix_len]
                if pref not in self.groups:
                    self.groups[pref] = FileGroup(self.type_map.keys())
                curr_group = self.groups[pref]
                curr_group.prefix = pref
                if pref in self.groups:
                    if self.group_full(curr_group):
                        curr_group.outliers_extra.append(file)
                        curr_group.full = True
                    if not self.group_full(curr_group):
                        self.add_file(curr_group, os.path.join(root, file))

        print self.groups
        print [x for x in self.groups.values() if x.outliers_extra or not self.group_full(x)]

    def outliers(self):
        return [x for x in self.groups.values() if x.outliers_extra or not self.group_full(x)]

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
        self.outliers_extra = []

    def prefix_match(self, input):
        if input[:len(self.prefix)] == self.prefix:
            return True
        return False




