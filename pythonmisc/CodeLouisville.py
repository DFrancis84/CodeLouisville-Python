# def word_count(string):
# 	string = string.lower()
#     word_dict = {}
#     word_list = string.split()
#     for sel_word in word_list:
#         count = 0
#         for word in word_list:
#             if sel_word == word:
#                 count += 1
#             word_dict[sel_word] = count
#     return word_dict

def word_count(string):
    dic = {}
    array = string.lower().split()
    for each in array:
        dic[each] = array.count(each)

    return dic


print(word_count("What would you do if you did what you did"))
