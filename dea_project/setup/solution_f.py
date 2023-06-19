import numpy as np
import math

def val_dict(col_vector, input_dict):
    keys = list(input_dict.keys())
    values = col_vector.flatten().tolist()
    return {keys[i]: values[i] for i in range(len(keys))}

def Me_elemental(lst):
    new_array=[[1,lst[0][0],lst[0][1]],[1,lst[1][0],lst[1][1]],[1,lst[2][0],lst[2][1]]]
    return new_array

def Le_elemental(lst,glob_dict):# input:[(),(),()] output: local Le elemental matrix of order (3*len(glob_dict))
    a=np.zeros((3,len(glob_dict)))
    for i in range(0,3):
      u=glob_dict[lst[i]]
      a[i,u-1]=1
    return a

def f_global(mesh,glob_dict,v_left,v_right,l):
    f=np.zeros((len(glob_dict),1))

    new_lst=[]
    for obj in mesh:
        a=[ele[0] for ele in obj]
        if a.count(0) == 2:
            new_lst.append(obj)

    for obj in new_lst:
        a_1=obj[2][1]-obj[0][1]
        a_2=0.5*(obj[2][1]-obj[0][1])*(obj[2][1]+obj[0][1])
        arr=np.array([[a_1],[0],[a_2]])
        minus_q_bar=(1)*np.dot(np.array(v_left),np.array([-1,0]))
        me=Me_elemental(obj)
        me_inverse=np.linalg.inv(me)
        me_inverse_trans=np.transpose(me_inverse)
        le=Le_elemental(obj,glob_dict)
        le_trans=np.transpose(le)
        arr=minus_q_bar*arr
        f=f+np.matmul(le_trans,np.matmul(me_inverse_trans,arr))

    new_lst=[]
    for obj in mesh:
        a=[ele[0] for ele in obj]
        if a.count(l) == 2:
            new_lst.append(obj)

    for obj in new_lst:
        a_1=obj[1][1]-obj[0][1] # check careefully here
        a_2=0.5*(obj[1][1]-obj[0][1])*(obj[1][1]+obj[0][1])
        arr=np.array([[a_1],[l*a_1],[a_2]])
        minus_q_bar=(1)*np.dot(np.array(v_right),np.array([1,0]))
        me=Me_elemental(obj)
        me_inverse=np.linalg.inv(me)
        me_inverse_trans=np.transpose(me_inverse)
        le=Le_elemental(obj,glob_dict)
        le_trans=np.transpose(le)
        arr=minus_q_bar*arr
        f=f+np.matmul(le_trans,np.matmul(me_inverse_trans,arr))

    return f
