def organize_list_alpha(string):
    word= string.split("-")
    word.sort()
    return "-".join(word)


string= "goku-vegeta-trunks-krillin"
resultado= organize_list_alpha(string)
print(organize_list_alpha(string))