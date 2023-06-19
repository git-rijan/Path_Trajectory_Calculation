l,b,=1,1
del_x,del_y,r=0.1,0.1,0.1
M=int(l/del_x)
N=int(b/del_y)

vel_left=[2/100,3/100]
vel_right=[5/100,6/100]

P=100000

loc=(0.5,0.5)

from setup.setup import setup

force_dict=setup(l,b,del_x,del_y,r,vel_left,vel_right,P,loc)
# print(force_dict)

# saving force _dict long nights run so
# import pickle
# with open('force_dict_4.pickle','wb') as f:
#     pickle.dump(force_dict,f)


