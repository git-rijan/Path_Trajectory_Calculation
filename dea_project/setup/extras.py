import numpy as np

def int_points(l,b,del_x,del_y,r):
    M=int(l/del_x)
    N=int(b/del_y)
    interior_pts=[]
    for i in range (2,M-1):
        for j in range (2,N-1):
            interior_pts.append((round(i*del_x,1),round(j*del_y,1)))

    return interior_pts

def mesh_1(obj,l,b,del_x,del_y,r,bndry_circle_pts_y_cord):
    x_list=[round(i/10,1) for i in range(0,int(round(10*obj[0])),int(round(10*del_x)))]

    y_1=[round(i/10,1) for i in range(0,int(round(10*obj[1])),int(round(10*del_y)))]
    y_2=bndry_circle_pts_y_cord
    y_3=[round(i/10,1) for i in range(int(round(10*(obj[1]+del_y))),int(10*(b+del_y)),int(round(10*del_y)))]

    y_list=list(set(y_1+y_2+y_3))
    y_list.sort()

    my_lst=[]
    for i in range(len(y_list) - 1):
        for j in range(len(x_list) - 1):
            tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
            tri2 = [(x_list[j+1], y_list[i]), (x_list[j+1], y_list[i+1]), (x_list[j], y_list[i+1])]
            my_lst.append(tri1)
            my_lst.append(tri2)
    return my_lst

def mesh_2(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord):
    x_list=bndry_circle_pts_x_cord

    y_list=[round(i/10,1) for i in range(0,int(round(10*obj[1])),int(round(10*del_y)))]

    my_lst=[]
    for i in range(len(y_list) - 1):
        for j in range(len(x_list) - 1):
            tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
            tri2 = [(x_list[j+1], y_list[i]), (x_list[j+1], y_list[i+1]), (x_list[j], y_list[i+1])]
            my_lst.append(tri1)
            my_lst.append(tri2)
    return my_lst

def mesh_3(obj,l,b,del_x,del_y,r,bndry_circle_pts_y_cord):
    x_list=[round(i/10,1) for i in range(int(round(10*(obj[0]+del_x))),int(round(10*(l+del_x))),int(round(10*del_x)))]

    y_1=[round(i/10,1) for i in range(0,int(round(10*obj[1])),int(round(10*del_y)))]
    y_2=bndry_circle_pts_y_cord
    y_3=[round(i/10,1) for i in range(int(round(10*(obj[1]+del_y))),int(10*(b+del_y)),int(round(10*del_y)))]

    y_list=list(set(y_1+y_2+y_3))
    y_list.sort()

    my_lst=[]
    for i in range(len(y_list) - 1):
        for j in range(len(x_list) - 1):
            tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
            tri2 = [(x_list[j+1], y_list[i]), (x_list[j+1], y_list[i+1]), (x_list[j], y_list[i+1])]
            my_lst.append(tri1)
            my_lst.append(tri2)
    return my_lst


def mesh_4(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord):
    x_list=bndry_circle_pts_x_cord

    y_list=[round(i/10,1) for i in range(int(round(10*(obj[1]+del_y))),int(round(10*(b+del_y))),int(round(10*del_y)))]

    my_lst=[]
    for i in range(len(y_list) - 1):
        for j in range(len(x_list) - 1):
            tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
            tri2 = [(x_list[j+1], y_list[i]), (x_list[j+1], y_list[i+1]), (x_list[j], y_list[i+1])]
            my_lst.append(tri1)
            my_lst.append(tri2)

    return my_lst


def mesh_5(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord,bndry_circle_pts_y_cord):
    x_list=bndry_circle_pts_x_cord[0:4]
    y_list=bndry_circle_pts_y_cord[0:4]

    my_lst=[]
    k=0
    for i in range(len(y_list) - 1):
        for j in range(len(x_list)-1-k):
            if j == range(len(x_list)-1-k)[-1]:
                tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
                my_lst.append(tri1)
            else:
                tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
                my_lst.append(tri1)
                tri2 = [(x_list[j+1], y_list[i]), (x_list[j+1], y_list[i+1]), (x_list[j], y_list[i+1])]
                my_lst.append(tri2)
        k=k+1
    return my_lst

def mesh_6(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord,bndry_circle_pts_y_cord):
    x_list=bndry_circle_pts_x_cord[3:7]
    x_list.reverse()
    y_list=bndry_circle_pts_y_cord[0:4]

    my_lst=[]
    k=0
    for i in range(len(y_list) - 1):
        for j in range(len(x_list)-1-k):
            if j == range(len(x_list)-1-k)[-1]:
                tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
                my_lst.append(tri1)
            else:
                tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
                my_lst.append(tri1)
                tri2 = [(x_list[j+1], y_list[i]), (x_list[j+1], y_list[i+1]), (x_list[j], y_list[i+1])]
                my_lst.append(tri2)
        k=k+1
    return my_lst

def mesh_7(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord,bndry_circle_pts_y_cord):
    x_list=bndry_circle_pts_x_cord[0:4]
    # x_list.reverse()
    y_list=bndry_circle_pts_y_cord[3:7]
    y_list.reverse()

    my_lst=[]
    k=0
    for i in range(len(y_list) - 1):
        for j in range(len(x_list)-1-k):
            if j == range(len(x_list)-1-k)[-1]:
                tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
                my_lst.append(tri1)
            else:
                tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
                my_lst.append(tri1)
                tri2 = [(x_list[j+1], y_list[i]), (x_list[j+1], y_list[i+1]), (x_list[j], y_list[i+1])]
                my_lst.append(tri2)
        k=k+1
    return my_lst

def mesh_8(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord,bndry_circle_pts_y_cord):
    x_list=bndry_circle_pts_x_cord[3:7]
    x_list.reverse()
    y_list=bndry_circle_pts_y_cord[3:7]
    y_list.reverse()

    my_lst=[]
    k=0
    for i in range(len(y_list) - 1):
        for j in range(len(x_list)-1-k):
            if j == range(len(x_list)-1-k)[-1]:
                tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
                my_lst.append(tri1)
            else:
                tri1 = [(x_list[j], y_list[i]), (x_list[j+1], y_list[i]), (x_list[j], y_list[i+1])]
                my_lst.append(tri1)
                tri2 = [(x_list[j+1], y_list[i]), (x_list[j+1], y_list[i+1]), (x_list[j], y_list[i+1])]
                my_lst.append(tri2)
        k=k+1
    return my_lst


