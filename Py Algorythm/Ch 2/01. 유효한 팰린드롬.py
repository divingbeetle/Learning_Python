"""

    01. 유효한 팰린드롬
        주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

"""


def is_palindrome(word):
    return True if len(word) in (0, 1) else word[0] == word[-1] and is_palindrome(word[1:-1])


clean_str = "".join([letter for letter in input().lower() if letter.isalpha() or letter.isdigit()])
print(is_palindrome(clean_str))
