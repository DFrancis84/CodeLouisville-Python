def stringcases(string):
    upper = string.upper()
    lower = string.lower()
    titlecase = string.title()
    reverse = string[::-1]

    return upper, lower, titlecase, reverse

print(stringcases("What is up man?"))