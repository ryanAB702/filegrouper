import sys

from filegrouper import *



if __name__ == "__main__":

    input_dir = sys.argv[1]

    grouper = FileGrouper(dir=input_dir,
                          prefix_len=5,
                          types=[clan_silences, newclan_merged_final, newclan_merged])

 #   print grouper.__dict__
