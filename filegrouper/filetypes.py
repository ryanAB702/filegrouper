class FileType(object):
    '''
    Initialize FileType class for 14 different types of files;
    Incoorporates functions below when used in filegrouper.py
    Takes 2 parameters: 1st - string name to call files of the desired type
                        2nd - the type of file to look for (one of the comp_functions below)
    '''
    def __init__(self, typename, comp_func):
        self.typename = typename
        self.comp_func = comp_func

def audio_bl_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if the file is a basic level audio file; false otherwise
    '''
    if input.endswith(".csv"):
        if "audio" in input:
            return True
    return False

def video_bl_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if file is basic level video file; false otherwise
    '''
    if input.endswith(".csv"):
        if "video" in input:
            return True
    return False

def lena5min_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if file is a lena5min.csv file; false otherwise
    '''
    if input.endswith("lena5min.csv"):
        return True
    return False

def silences_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if file is silence.txt file; false otherwise
    '''
    if input.endswith("silences.txt"):
        return True
    return False

def video_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if file is "video".mp4 file; false otherwise
    '''
    if input.endswith(".mp4"):
        return True
    return False

def audio_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if "audio".wav file and not scrubbed; false otherwise
    '''
    if input.endswith(".wav"):
        if "scrubbed" not in input:
            return True
    return False

def audio_scrubbed_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if "audio".wav file and is scrubbed; false otherwise
    '''
    if input.endswith(".wav"):
        if "scrubbed" in input:
            return True
    return False

def opf_not_final_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if .opf file and is not final; false otherwise
    '''
    if input.endswith(".opf"):
        if "consensus_final" not in input:
            return True
    return False

def opf_final_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if .opf file and is final; false otherwise
    '''
    if input.endswith(".opf"):
        if "consensus_final" in input:
            return True
    return False

def clan_silences_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if .cha file with "silence"; false otherwise
    '''
    if input.endswith(".cha"):
        if "silences" in input:
            return True
    return False

def clan_final_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if .cha file final but not merged (final clan); false otherwise
    '''
    if input.endswith(".cha"):
        if "_final" in input and "_merged" not in input:
            return True
    return False

def clan_merged_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if .cha file merged but not final (merged clan); false otherwise
    '''
    if input.endswith(".cha"):
        if "newclan_merged" in input and "final" not in input:
            return True
    return False

def clan_merged_final_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if .cha file, merged and final (final merged clan); false otherwise
    '''
    if input.endswith(".cha"):
        if "newclan_merged" in input and "final" in input:
            return True
    return False

def video_personal_info_comp_func(input):
    '''
    :param input: Input is a filename to be analyzed
    :return: True if personal_info.csv video file; false otherwise
    '''
    if input.endswith("personal_info.csv"):
        return True
    return False


opf_not_final = FileType("opf_not_final", opf_not_final_comp_func)
opf_final = FileType("opf_final",opf_final_comp_func)
audio_scrubbed = FileType("audio_scrubbed", audio_scrubbed_comp_func)
audio = FileType("audio", audio_comp_func)
video_file = FileType("video", video_comp_func)
audio_bl = FileType("audio_bl", audio_bl_comp_func)
video_bl = FileType("video_bl", video_bl_comp_func)
silences = FileType("silences", silences_comp_func)
lena5min = FileType("lena5min", lena5min_comp_func)
clan_silences = FileType("clan_silences", clan_silences_comp_func)
clan_final = FileType("clan_final", clan_final_comp_func)
newclan_merged = FileType("newclan_merged", clan_merged_comp_func)
newclan_merged_final = FileType("newclan_merged_final", clan_merged_final_comp_func)
video_personal_info = FileType("video_personal_info", video_personal_info_comp_func)
