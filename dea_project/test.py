# loading force_dict for long run
import pickle
with open('force_dict_4.pickle', 'rb') as f:
        force_dict = pickle.load(f)
        print(len(force_dict))


from path import path
dict_for_NN=path(force_dict,1.6,4,4) #mass =1, l=,b=


# saving to pickle file
# with open('dict_for_NN_4_one_output_pts.pickle', 'wb') as f:
#     pickle.dump(dict_for_NN, f)




