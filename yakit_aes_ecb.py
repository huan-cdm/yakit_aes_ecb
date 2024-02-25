#!/usr/bin/env python3
import json
def print_dict_with_double_quotes(d):  
    json_str = json.dumps(d, ensure_ascii=False)  
    print(json_str)  
rule_file = open("./dicc.txt", encoding='utf-8')  
dict_user = {"username": "admin", "password": ""}  
  
for line in rule_file:  
    dict_user["password"] = line.strip()  
    print_dict_with_double_quotes(dict_user)  
rule_file.close()
