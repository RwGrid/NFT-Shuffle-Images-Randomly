import glob
import json
import os
import re
import shutil
from random import random
from random import choice
print(" > Please give me the path of all_json folder of json :", end='')
jsonn_path = input("")
print(" > Please give me the path of all_img folder of imgs :", end='')
imgg_path = input("")
cc=os.listdir(jsonn_path)
length_of_img=len(cc)
all_indexes=[i for i,v in enumerate(cc)]
to_exclude=[]
sub_dir_file_paths_json = glob.glob(str(jsonn_path) + "/*")
sub_dir_file_paths_img = glob.glob(str(imgg_path) + "/*")
sub_dir_file_paths_json.sort(key=lambda f: int(re.sub('\D', '', f)))
sub_dir_file_paths_img.sort(key=lambda f: int(re.sub('\D', '', f)))
try:
    os.mkdir('all_json_shuffled')
except:
    pass
try:
    os.mkdir('all_imgs_shuffled')
except:
    pass
for index,file_pat in enumerate(sub_dir_file_paths_json):
    sdf=0
    rand=choice([i for i in range(0,len(sub_dir_file_paths_json)) if i not in to_exclude])
    #rand=choice(list(set([x for x in range(0, length_of_img)]) - set(to_exclude)))
    shutil.copyfile(sub_dir_file_paths_json[index],
                    'all_json_shuffled' + '/' +str(rand)  + '.json')
    shutil.copyfile(sub_dir_file_paths_img[index],
                    'all_imgs_shuffled' + '/' +str(rand)+ '.png')
    to_exclude.append(rand)
czxc=0