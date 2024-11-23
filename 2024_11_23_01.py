fav_inv = {
    'lihua':{'place':'england','fav_num':6},
    'BOWEN':{'place':'DPRK','fav_num':3}
    }

for name , fav_thing in fav_inv.items():
    print(f"{name} like {fav_thing['place']},favnum is {fav_thing['fav_num']}")

"""
错误案例
fav_inv = {
    'lihua':{'place':'england','fav_num':6},
    'BOWEN':{'place':'DPRK','fav_num':3}
    }

for name , fav_thing in fav_inv:
    print(f'{name} like {fav_thing['place']},favnum is {fav_thing['fav_num']} ')
 
"""
