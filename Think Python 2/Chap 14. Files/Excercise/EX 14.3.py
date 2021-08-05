"""

*** EX 14.3 ***
    In a Large collection of MP3 files, there may be more than one copy of the song,
    stored in different directories or w/ different file names.
    The goal of this exercise is to search for duplicates

   1. Write a program that searches a directory and all of its subdirectories recursively
   and returns a list of complete paths for all files with a given suffix (like .mp3)

   2. To recognize duplicates, you can use md5sum to compute a "checksum" for each files
   If two files have the same checksum, they probably have the same contents

   3. To double-check, you can use the Unix Command diff

"""
import os


def find_paths_for(root_dir, suffix):
    """Finds the name of all files w/ given suffix in root directory and its subdirectories.

    :param root_dir: string name of directory
    :param suffix: filename extension in string
    :return: list of file name
    """
    res = []
    for (roots, dir, files) in os.walk(root_dir):
        for file in files:
            if file.endswith(suffix):
                res.append(os.path.join(roots, file))

    return res


def get_md5(filename): # TODO: Using subprocess module to get the md5 hash
    """ computes the MD5 checksum of the contents of a file
    """
    if not os.path.isfile(filename):
        print("Error:", filename, "is not a file.")
        return

    cmd = "certutil -hashfile " + '"%s"' % filename + " md5"
    fp = os.popen(cmd)
    res_text = fp.read()
    fp.close()
    res_list = res_text.split()
    md5 = res_list[res_list.index('해시:') + 1]

    return md5


def map_duplicates(checklist, func):
    """map elements in the checklist with same return value for the function

    :return: dictionary, {return value: [elemet1, elemen2 ...]}
    """
    res = {}
    for item in checklist:
        check_value = func(item)
        res.setdefault(check_value, []).append(item)

    return res


def print_duplicates(file_list):
    duplicate_map = map_duplicates(file_list, get_md5)
    for hash, duplicate_files in duplicate_map.items():
        if len(duplicate_files) > 1:
            print("These {0} files are duplicates".format(len(duplicate_files)))

            gen = ((path.split("\\")[-1], path) for path in duplicate_files)
            for (filename, path) in gen:
                print("Filename: {0} in {1}".format(filename, path))


def main():
    mp3_list = (find_paths_for(os.getcwd(), 'mp3'))
    print_duplicates(mp3_list)


if __name__ == "__main__":
    main()
