class FileType(object):
    def __init__(self, typename, comp_func):
        self.typename = typename
        self.comp_func = comp_func


def clan_comp_func(input):
    if input.endswith(".cha"):
        return True
    return False

def bl_comp_func(input):
    if input.endswith(".csv"):
        return True
    return False

def lena5min_comp_func(input):
    if input.endswith("lena5min.csv"):
        return True
    return False

def silences_comp_func(input):
    if input.endswith("silences.txt"):
        return True
    return False


clan_file = FileType("clan", clan_comp_func)
audio_bl = FileType("audio_bl", bl_comp_func)
silences = FileType("silences", silences_comp_func)
lena5min = FileType("lena5min", lena5min_comp_func)



