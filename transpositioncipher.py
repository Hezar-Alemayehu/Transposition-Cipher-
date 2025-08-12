key = "ok"
text_to_decrypt = "welcometomychannels"
key_len = len(key)
remain = len(text_to_decrypt)% key_len
real_to_add = key_len- remain
full_text = text_to_decrypt + "x"*real_to_add
lst = []
for i in range(0, len(full_text),2):
    chunk = full_text[i:i+2]
    lst.append(list(chunk))
print(lst)
lst_key = list(enumerate(key))
sorted_by_letter = sorted(lst_key, key= lambda x: x[1])
final_order = [i[0] for i in sorted_by_letter]
print(final_order)
final_lst = []
for i in range(len(lst)):
    for j in final_order:
        final_lst.append(lst[i][j])

final_string = "".join(final_lst)
print(final_string)

