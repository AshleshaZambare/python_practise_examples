
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

vow_list = ['a', 'e', 'i', 'o', 'u']
l = []
for i in sequence:
    if i in vow_list:
        l.append(i)
print(l)

#using filer

filtered_list = [ele for ele in filter(lambda letter: letter in vow_list , sequence)]
filtered_list = set(filter(lambda letter: letter in vow_list , sequence))
print(filtered_list)
