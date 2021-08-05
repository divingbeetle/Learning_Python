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
    res = []
    for (roots, dir, files) in os.walk(root_dir):
        for file in files:
            if file.endswith(suffix):
                res.append(os.path.join(roots, file))

    return res


def get_md5(filename):
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
    res = {}
    for item in checklist:
        check_value = func(item)
        res.setdefault(check_value, []).append(item)

    return res


def print_duplicates(file_list):
    gen = ((path.split("\\")[-1], path) for path in file_list)

    print("These {0} files are duplicates".format(len(file_list)))

    for (filename, path) in gen:
        print("Filename: {0} in {1}".format(filename, path))


def main():
    mp3_list = (find_paths_for(os.getcwd(), 'mp3'))
    duplicate_files = map_duplicates(mp3_list, get_md5)

    for key, value in duplicate_files.items():
        if len(value) > 1:
            print_duplicates(value)


if __name__ == "__main__":
    main()
