import math
import numpy as np

def points_on_circle(center, radius):
    points = []
    for i in range(0,360,30):
        angle = 2 * math.pi * i / 360
        x = round(center[0] + radius * math.cos(angle),3)
        y = round(center[1] + radius * math.sin(angle),3)
        points.append((x, y))
    return points

def setup(l,b,del_x,del_y,r,v_left,v_right,P,loc):
    from setup.extras import int_points,mesh_1,mesh_2,mesh_3,mesh_4,mesh_5,mesh_6,mesh_7,mesh_8
    from setup.solution_k import global_dict,k_global
    from setup.solution_f import f_global,val_dict
    from setup.csv_codes import dictionary_to_csv,force_to_csv
    from setup.solution_fdm import f_x,f_y,dp_dx,dp_dy,pressure,force
    from plots import plot_triangles,combine,velo_plot

    force_dict={}

    interior_pts=int_points(l,b,del_x,del_y,r)

    for obj in interior_pts:
        print(obj)

        bndry_circle_pts=points_on_circle(obj,r)

        bndry_circle_pts_y_cord=list(set([i[1] for i in bndry_circle_pts ]))
        bndry_circle_pts_y_cord.sort()

        bndry_circle_pts_x_cord=list(set([i[0] for i in bndry_circle_pts ]))
        bndry_circle_pts_x_cord.sort()

        mesh_lst_1=mesh_1(obj,l,b,del_x,del_y,r,bndry_circle_pts_y_cord)
        mesh_lst_2=mesh_2(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord)
        mesh_lst_3=mesh_3(obj,l,b,del_x,del_y,r,bndry_circle_pts_y_cord)
        mesh_lst_4=mesh_4(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord)

        mesh_lst_5=mesh_5(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord,bndry_circle_pts_y_cord)
        mesh_lst_6=mesh_6(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord,bndry_circle_pts_y_cord)
        mesh_lst_7=mesh_7(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord,bndry_circle_pts_y_cord)
        mesh_lst_8=mesh_8(obj,l,b,del_x,del_y,r,bndry_circle_pts_x_cord,bndry_circle_pts_y_cord)

        mesh=mesh_lst_1+mesh_lst_2+mesh_lst_3+mesh_lst_4+mesh_lst_5+mesh_lst_6+mesh_lst_7+mesh_lst_8
        plot_triangles(mesh, filename='mesh_png/'+'mesh_'+str(obj)+'.png')

        # print(mesh)

        glob_dict=global_dict(mesh) # {():1}
        # print(len(mesh))

        K_glob=k_global(mesh,glob_dict)
        np.savetxt('K_csv/'+'K_'+str(obj)+'.csv',K_glob,delimiter=',')

        F_glob=f_global(mesh,glob_dict,v_left,v_right,l)
        np.savetxt('F_csv/'+'F_'+str(obj)+'.csv',F_glob,delimiter=',')

        try:
            u=np.linalg.solve(K_glob,F_glob)
        except: # K might be singular matrix, in that cas error so skip if error happens
            continue

        value_dict= val_dict(u,glob_dict)
        dictionary_to_csv(value_dict,'u_csv/'+'u_'+str(obj)+'.csv')
        # print(value_dict)

        v_x_dict=f_x(obj,l,b,del_x,del_y,value_dict,bndry_circle_pts_y_cord)
        dictionary_to_csv(v_x_dict,'v_x_csv/'+'v_x_'+str(obj)+'.csv')

        v_y_dict=f_y(obj,l,b,del_x,del_y,value_dict,bndry_circle_pts_x_cord)
        dictionary_to_csv(v_y_dict,'v_y_csv/'+'v_y_'+str(obj)+'.csv')

        combine_v_dict=combine(v_x_dict,v_y_dict)
        velo_plot(combine_v_dict,obj,l,b)

        dv_x_dx_dict=f_x(obj,l,b,del_x,del_y,v_x_dict,bndry_circle_pts_y_cord)
        dictionary_to_csv(dv_x_dx_dict,'dv_x_dx_csv/'+'dv_x_dx_'+str(obj)+'.csv')

        dv_x_dy_dict=f_y(obj,l,b,del_x,del_y,v_x_dict,bndry_circle_pts_x_cord)
        dictionary_to_csv(dv_x_dy_dict,'dv_x_dy_csv/'+'dv_x_dy_'+str(obj)+'.csv')

        dv_y_dx_dict=f_x(obj,l,b,del_x,del_y,v_y_dict,bndry_circle_pts_y_cord)
        dictionary_to_csv(dv_y_dx_dict,'dv_y_dx_csv/'+'dv_y_dx_'+str(obj)+'.csv')

        dv_y_dy_dict=f_y(obj,l,b,del_x,del_y,v_y_dict,bndry_circle_pts_x_cord)
        dictionary_to_csv(dv_y_dy_dict,'dv_y_dy_csv/'+'dv_y_dy_'+str(obj)+'.csv')

        dp_dx_dict=dp_dx(v_x_dict,v_y_dict,dv_x_dx_dict,dv_x_dy_dict)
        dictionary_to_csv(dp_dx_dict,'dp_dx_csv/'+'dp_dx_'+str(obj)+'.csv')

        dp_dy_dict=dp_dy(v_x_dict,v_y_dict,dv_y_dx_dict,dv_y_dy_dict)
        dictionary_to_csv(dp_dy_dict,'dp_dy_csv/'+'dp_dy_'+str(obj)+'.csv')

        press_dict=pressure(obj,l,b,del_x,del_y,dp_dx_dict,dp_dy_dict,bndry_circle_pts,P)
        dictionary_to_csv(press_dict,'pressure_csv/'+'pressure_'+str(obj)+'.csv')

        force_lst=force(press_dict,r)
        force_to_csv(obj,force_lst,'force_csv/'+'force.csv')

        force_dict[obj]=force_lst
        # appending to force_dict {obj:[f_x,f_y]}

    return force_dict





























