import numpy as np

def global_dict(mesh):
   my_dict={}
   my_lst=list(set([item for lst in mesh for item in lst]))
   k=1
   for obj in my_lst:
      my_dict[obj]=k
      k=k+1
   return my_dict


def area_of_triangle(lst): # input:[(),(),()] output:area
    n_array=np.array([[lst[0][0],lst[0][1],1],[lst[1][0],lst[1][1],1],[lst[2][0],lst[2][1],1]])
    det = np.linalg.det(n_array)
    area=0.5*det
    return area

def B_elemental(lst): # input:[(),(),()] output: B elemental matrix of order (2*3)
    n_array=np.array([[lst[1][1]-lst[2][1],lst[2][1]-lst[0][1],lst[0][1]-lst[1][1]],[lst[2][0]-lst[1][0],lst[0][0]-lst[2][0],lst[1][0]-lst[0][0]]])
    div=2*area_of_triangle(lst)
    n_array=n_array/div
    return n_array


def k_elemental(lst): # input:[(),(),()] output: local k elemental matrix of order (3*3)
    array_1=B_elemental(lst)
    array_2=np.transpose(array_1)
    array_3=np.matmul(array_2,array_1)

    area=area_of_triangle(lst)
    array_3=area*array_3
    return array_3


def Le_elemental(lst,glob_dict):# input:[(),(),()] output: local Le elemental matrix of order (3*338)
    a=np.zeros((3,len(glob_dict)))
    for i in range(0,3):
      u=glob_dict[lst[i]]
      a[i,u-1]=1
    return a


def k_global(mesh,glob_dict):
   k=np.zeros((len(glob_dict),len(glob_dict)))

   for obj in mesh:
      le=Le_elemental(obj,glob_dict)
      le_trans=np.transpose(le)
      ke=k_elemental(obj)
      k=k+np.matmul(le_trans,np.matmul(ke,le))

   return k

