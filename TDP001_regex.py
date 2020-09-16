#! /usr/bin/env python3
import re
# ================================================================================
# TDP003 uppgift 3 de1 tom del3
# ================================================================================
f = open("test_string.txt", "r")

print(f)
print()

content = f.read()

print(content)

print("Matchade objekter för Liu-ID:")
liu_list = re.findall(r"[a-z A-Z]{4,5}\d{2,3}", content)

print(liu_list)
print()

print("Matchade objekter för datum:")
date_list = re.findall(r"\d{4}-\d{2}-\d{2}", content)
print(date_list)
print()


print("Matchade giltiga datum:")
valid_date_list = re.findall(r"\d{4}-[0-1]\d-[0-3]\d", content)
print(valid_date_list)
print()
f.close()
