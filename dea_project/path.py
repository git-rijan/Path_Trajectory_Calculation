def eliminate(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        if len(value) >= 1: # 2 if no of output points is 2
            new_dictionary[key] = value
    return new_dictionary


def eliminate_key_value_pairs(d, l, b):
    new_dict = {}
    for key, value in d.items():
        # Check if any tuple in the value list violates the conditions
        if any(x > l or y > b for x, y in value):
            continue
        else:
            new_dict[key] = value
    return new_dict

def eliminate_duplicates(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_list = [key] + value
        i = 0
        while i < len(new_list) - 1:
            if new_list[i] == new_list[i+1]:
                break
            i += 1
        else:
            new_dict[key] = value
    return new_dict

def path(force_dict,m,l,b):
    # m=mass
    acc_dict={(x, y): [f_x/m, f_y/m] for (x, y), [f_x, f_y] in force_dict.items()}

    my_dict={}
    for key,value in acc_dict.items():
        del_t=0.7 # 1 sec
        v_x,v_y=0,0
        x_initial,y_initial=key[0],key[1]
        accn_x=value[0]
        accn_y=value[1]

        my_lst=[]
        for i in range(1): # output no of points = 1
            x_new=x_initial+(v_x*del_t)+(0.5*(accn_x*del_t**2))
            y_new=y_initial+(v_y*del_t)+(0.5*(accn_y*del_t**2))
            v_x_new=v_x+(accn_x*del_t)
            v_y_new=v_x+(accn_y*del_t)
            tple=(round(x_new,1),round(y_new,1))

            tple_new=tple
            my_lst.append(tple_new)

            v_x=v_x_new
            v_y=v_y_new
            x_initial=tple_new[0]
            y_initial=tple_new[1]

            try:
                accn_x=acc_dict[(x_initial,y_initial)][0]
                accn_y=acc_dict[(x_initial,y_initial)][1]
            except:
                break
        my_dict[key]=my_lst

    my_dict=eliminate(my_dict) # if less than 2 elements in value list , eliminate that key,value pair
    print(len(my_dict))
    my_dict=eliminate_key_value_pairs(my_dict,l,b) # if any value in list is greater than l or b eliminate that key,value pair
    print(len(my_dict))
    my_dict=eliminate_duplicates(my_dict)
    print(len(my_dict))

    return my_dict

