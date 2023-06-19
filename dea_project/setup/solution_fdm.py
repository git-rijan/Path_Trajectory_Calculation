import numpy as np
import math

def f_x(obj,l,b,del_x,del_y,value_dict,bndry_circle_pts_y_cord):
    bndry_circle_pts_y_cord_copy=bndry_circle_pts_y_cord.copy()
    my_dict={}

    y_1=[round(i/10,1) for i in range(0,int(round(10*obj[1])),int(round(10*del_y)))]
    y_3=[round(i/10,1) for i in range(int(round(10*(obj[1]+del_y))),int(10*(b+del_y)),int(round(10*del_y)))]
    y=y_1+y_3

    for ele in y:
        new_dict={key[0]:value for key,value in value_dict.items() if key[1] == ele}
        sorted_dict = {k: v for k, v in sorted(new_dict.items())}
        x_list=np.array(list(sorted_dict.keys()))
        z_list=np.array(list(sorted_dict.values()))
        dz_dx=np.gradient(z_list,x_list)
        my_dict.update({(x,ele):z for x,z in zip(x_list,dz_dx)})

    bndry_circle_pts_y_cord_copy.pop(-1)
    bndry_circle_pts_y_cord_copy.pop(0)

    for ele in bndry_circle_pts_y_cord_copy:
        new_dict={key[0]:value for key,value in value_dict.items() if key[1] == ele and key[0] < obj[0] }
        sorted_dict = {k: v for k, v in sorted(new_dict.items())}
        x_list=np.array(list(sorted_dict.keys()))
        z_list=np.array(list(sorted_dict.values()))
        dz_dx=np.gradient(z_list,x_list)
        my_dict.update({(x,ele):z for x,z in zip(x_list,dz_dx)})

    for ele in bndry_circle_pts_y_cord_copy:
        new_dict={key[0]:value for key,value in value_dict.items() if key[1] == ele and key[0] > obj[0] }
        sorted_dict = {k: v for k, v in sorted(new_dict.items())}
        x_list=np.array(list(sorted_dict.keys()))
        z_list=np.array(list(sorted_dict.values()))
        dz_dx=np.gradient(z_list,x_list)
        my_dict.update({(x,ele):z for x,z in zip(x_list,dz_dx)})

    return my_dict

def f_y(obj,l,b,del_x,del_y,value_dict,bndry_circle_pts_x_cord):
    my_dict={}
    bndry_circle_pts_x_cord_copy=bndry_circle_pts_x_cord.copy()

    x_1=[round(i/10,1) for i in range(0,int(round(10*obj[0])),int(round(10*del_x)))]
    x_3=[round(i/10,1) for i in range(int(round(10*(obj[0]+del_x))),int(10*(l+del_x)),int(round(10*del_x)))]
    x=x_1+x_3

    for ele in x:
        new_dict={key[1]:value for key,value in value_dict.items() if key[0] == ele}
        sorted_dict = {k: v for k, v in sorted(new_dict.items())}
        y_list=np.array(list(sorted_dict.keys()))
        z_list=np.array(list(sorted_dict.values()))
        dz_dy=np.gradient(z_list,y_list)
        my_dict.update({(ele,y):z for y,z in zip(y_list,dz_dy)})

    bndry_circle_pts_x_cord_copy.pop(-1)
    bndry_circle_pts_x_cord_copy.pop(0)

    for ele in bndry_circle_pts_x_cord_copy:
        new_dict={key[1]:value for key,value in value_dict.items() if key[0] == ele and key[1] < obj[1] }
        sorted_dict = {k: v for k, v in sorted(new_dict.items())}
        y_list=np.array(list(sorted_dict.keys()))
        z_list=np.array(list(sorted_dict.values()))
        dz_dy=np.gradient(z_list,y_list)
        my_dict.update({(ele,y):z for y,z in zip(y_list,dz_dy)})

    for ele in bndry_circle_pts_x_cord_copy:
        new_dict={key[1]:value for key,value in value_dict.items() if key[0] == ele and key[1] > obj[1] }
        sorted_dict = {k: v for k, v in sorted(new_dict.items())}
        y_list=np.array(list(sorted_dict.keys()))
        z_list=np.array(list(sorted_dict.values()))
        dz_dy=np.gradient(z_list,y_list)
        my_dict.update({(ele,y):z for y,z in zip(y_list,dz_dy)})

    return my_dict

def dp_dx(v_x,v_y,dv_x_dx,dv_x_dy):
    rho=100
    my_dict={}

    for key in v_x.keys():
        val=(-1)*rho*((v_x[key]*dv_x_dx[key])+(v_y[key]*dv_x_dy[key]))
        my_dict[key]=val

    return my_dict

def dp_dy(v_x,v_y,dv_y_dx,dv_y_dy):
    rho=100
    my_dict={}

    for key in v_x.keys():
        val=(-1)*rho*((v_x[key]*dv_y_dx[key])+(v_y[key]*dv_y_dy[key]))
        my_dict[key]=val

    return my_dict

def pressure(obj,l,b,del_x,del_y,dp_dx_dict,dp_dy_dict,bndry_circle_pts,P):
    my_dict={}

    new_dict={key[0]:value for key,value in dp_dx_dict.items() if key[1] == obj[1] and key[0] > obj[0]}
    sorted_dict = {k: v for k, v in sorted(new_dict.items())}
    sorted_dict.popitem()
    # print(sorted_dict)

    for key in reversed(sorted_dict.keys()):
        P=P-(sorted_dict[key]*del_x)
    # print(P)

    for i in range(len(bndry_circle_pts)):
        if i==0:
            my_dict.update({bndry_circle_pts[i]:P})
        else:
            P=P-((dp_dx_dict[bndry_circle_pts[i]]*del_x)+(dp_dy_dict[bndry_circle_pts[i]]*del_y))
            my_dict.update({bndry_circle_pts[i]:P})

    return my_dict

def force(press_dict,r):
    length=(r*math.pi)/6
    force_arr=np.array([0,0])
    theta=0
    for key,value in press_dict.items():
        F = value*length
        force_arr=force_arr+np.array([1*F*math.cos(theta),-1*F*math.sin(theta)])
        theta=theta+((math.pi)/6)
    return force_arr.tolist()












