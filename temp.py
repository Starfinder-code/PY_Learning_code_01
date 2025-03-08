list1 = ['A','B','C']
dict1 = {}
for i in range(3):
    order = int(input('你要把'+list1[i]+'放在第几位？（请输入数字1,2,3)'))
    dict1[order] = list1[i]
print(dict1)  

list1 = []
# 清空原本列表list1的元素
for i in range(1,4):
    list1.append(dict1[i])
print(list1)