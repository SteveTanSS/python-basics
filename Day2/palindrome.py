import string

def palindrome_checker(passedString):
    editted_text = remove_special(passedString)
    if (editted_text == editted_text[::-1]):
        return "Y"
    else:
        return "N"


def remove_special(text):
    editted_text = "".join(i.lower() for i in text if i in string.ascii_letters)
    return editted_text


print(palindrome_checker("Stars"))
print(palindrome_checker("O, a kak Uwakov lil vo kawu kakao!"))
print(palindrome_checker("Some men interpret nine memos"))