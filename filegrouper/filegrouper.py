import os

from filetypes import *
import filetypes

class FileGrouper(object):
    def __init__(self, dir="", prefix_len=5, types=[]):
        '''
        :param dir: Directory in which the user is working
        :param prefix_len: Equals 5 since two digits for subject number, one underscore, and two digits for month
        :param types: List of the file types being checked for (types found in filetypes.py)
        '''

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
        '''
        :return: Does not return any value; navigates the files
        Sets and updates variables to their correct values (pref; curr_group; gurr_group.prefix; groups
        '''

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
                    if not self.group_full(curr_group):
                        self.add_file(curr_group, os.path.join(root, file))

    def outliers(self):
        '''
        :return: Returns a list of the file groups that dont have the correct number of files (too many or too few)
        Correct number of files determined by the number of files in the majority of the groups (mode group size)
        '''
        return [x for x in self.groups.values() if x.outliers_extra or not self.group_full(x)]

    def group_full(self, group):
        '''
        :param group: Takes filegroup object as a parameter
        :return: Boolean function True if the group from the parameter is full (correct number of files) and False if
        the group is not full (too few files based on the desired number).
        '''
        found_empty = False
        group_vars = vars(group)
        for x in self.type_map.keys():
            if not group_vars[x]:
                found_empty = True
        if found_empty:
            return False
        else:
            group.full = True
        return True

    def add_file(self, group, file):
        '''
        :param group: takes a file group object as one parameter (for files to be added to)
        :param file: takes specific file as second parameter
        :return: Does not return a value; updates variables such as vars(group) and group.empty based on input file
        '''
        for type, func in self.type_map.items():
            if func(file):
                vars(group)[type] = file
                group.empty = False
                self.group_full(group)
                return

    def prefix_in_groups(self, prefix):
        '''
        :param prefix: the subjectNumber_Month that precedes the file names,
        indicating which subject the file has information about (format: ##_##).
        :return: True if the prefix already has a group started in self;
        False if it is the first file being analyzed with that specific prefix.
        '''
        for group in self.groups:
            if group.prefix == prefix:
                return True
        return False


class FileGroup(object):
    '''
    Initialize the FileGroup class.  Classes based on prefixes for the files in question.
    file_types list contains the types of files in question (from filetypes.py module)
    '''
    def __init__(self, file_types=[], prefix=""):
        for x in file_types:
            setattr(self, x, "")

        #Initialize variables (prefix; full; empty; outlier_extra) to their desired values.
        self.prefix = prefix
        self.full = False
        self.empty = True
        self.outliers_extra = []

    def prefix_match(self, input):
        '''
        :param input: file to compare against self
        :return: True if the input file has the same prefix as self, and is therefore of the same FileGroup;
                 Returns false otherwise.
        '''
        if input[:len(self.prefix)] == self.prefix:
            return True
        return False
