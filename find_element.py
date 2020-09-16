#! /usr/bin/env python3
import re
# ================================================================================
# TDP001uppgift 3 del 4
# ================================================================================
with open("Minblogg.html", "r") as f:
    print(f)
    content = f.read()
    print()
    element = re.findall(r"<.+>", content)
    filtered_list = []
    for i in element:
        filtered_element = re.search(r"\w+", i)
        if filtered_element.group(0) != "":
            filtered_list.append(filtered_element.group(0))
    
    final_filtered_list = list(set(filtered_list))

    print("Elements")
    print("="*10)
    number = 1
    for i in final_filtered_list:
        print("{0}. {1}".format(number, i))
        number += 1
