"""

*** EX 14.1 ***
    Write a function called sed that takes as arguments
    a patten string, a replacement string, and two filenames ;
    it should read the first file and write the contents into the second file
    If the pattern string appears anywhere in the file,
    it should be replaced w/ the replacement string.

    If an error occurs while opening, reading, writing or closing files,
    your program should catch the exception, print an error message, and exit.


"""


def sed(file_name1, file_name2, pattern_str, replace_str):
    try:
        fin = open(file_name1)
    except:
        print("Error")
        return

    try:
        fout = open(file_name2, 'w', encoding='UTF-8')
    except:
        print("Error")
        return

    for line in fin.readlines():
        try:
            fout.write(line.replace(pattern_str, replace_str))
        except:
            print("Error")
            return

    try:
        fin.close()
    except:
        print("Error")
        return
    try:
        fout.close()
    except:
        print("Error")
        return


def main():
    sed("99 bottles of beer.txt", "99 bottles of orange juice.txt", "beer", "orange juice")


if __name__ == "__main__":
    main()
