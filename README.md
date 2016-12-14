# filegrouper


filegrouper is a library for picking out files in a directory that belong together.
These files can be of different types, but share a relation by their prefix. The library
returns a collection of FileGroup objects with all the types of files with a common prefix
as member variables.


For example, if you have a folder filled with clan and lena5min.csv files, you can use filegrouper
to return a collection of objects storing the paths to all the groups of clan and lena files.

e.g.:

```python

input_dir = "some_folder"

grouper = FileGrouper(dir=input_dir,
                          prefix_len=5,
                          types=[
                                silences,
                                lena5min,
                                clan
                            ])


# member variables of each "group" object are dynamically
# generated from the "types" provided in the FileGrouper
# constructor

for group in grouper.groups:
    print group.clan
    print group.lena5min
    print group.silences


```




## install

```
$:  python setup.py install
```