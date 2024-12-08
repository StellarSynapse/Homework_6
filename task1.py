string = input("Enter some string, please: ")

str_list = string.split(" ")




new_dict = {}

for i in str_list:
    if str_list.count(i)==1:
        new_dict.update({i:str_list.count(i)})
    else:
        new_dict.update({str_list[str_list.index(i)]:str_list.count(i)})
        break
print(new_dict)
print(str_list)