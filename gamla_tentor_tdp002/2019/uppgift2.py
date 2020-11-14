import re


word_list = []
with open("ordlista.txt", "r") as f:
    for word in f:
        match1 = None
        match2 = None
        match1 = re.search(r"[A-Z a-z].+", word)
        if match1 != None:
            match2 = re.search(r".*[A-z a-z]", match1.group(0))
        if match2 != None:
            word_list.append(match2.group(0).upper())


for item in word_list:
    print(item)
