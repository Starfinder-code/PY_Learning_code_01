#first
foods = []
bools = True
while bools:
    things = input('please input the things you need!')
    thing_s = things.title()
    if thing_s != 'Quit' :
        foods.append(things)
    else:
        print(foods)
        break


#second
xunhuan = True
while xunhuan:
    years = input('please input your years!\n')
    years = int(years)
    if years >= 18:
        print('you need pay for 30 yuan\n')
    elif years < 18 and years >= 12:
        print('you need pay for 15 yuan\n')
    elif years < 12 and years >= 0:
        print('you need pay for 5 yuan\n')
    else:
        break

#third
sanwi_needs = ['vege','bread','met']
sanwi_added = []
res = True
while sanwi_needs:
    wait_for_add = sanwi_needs.pop()
    print(f'{wait_for_add} has been added in it')
    sanwi_added.append(wait_for_add)
print(sanwi_added)




        