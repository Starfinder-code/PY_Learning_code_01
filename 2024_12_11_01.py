def re_set (input_list,output_list):
    while output_list:
        outlist = output_list.pop()
        input_list.append(outlist)

haha = []
aha = ['aa','b','c']
re_set(haha,aha)
print(haha)
print(aha)




