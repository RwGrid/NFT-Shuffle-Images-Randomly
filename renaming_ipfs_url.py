import glob
import json
import os
import re

print(" > Please give me the path of all_json_shuffled folder of json, to rename ipfs :", end='')
folder_path = input("")
print(" > Please give me the cid of the ipfs :", end='')
ipfs_cid = input("")

sub_dir_file_paths = glob.glob(str(folder_path) + "/*")
all_json=[]
sub_dir_file_paths.sort(key=lambda f: int(re.sub('\D', '', f)))
for i,file in enumerate(sub_dir_file_paths):
    with open(file,'r') as fp:
        xx=json.load(fp)
        xx['image']=str(xx['image']).replace("was_replaced",ipfs_cid)
        xx['image']=str(xx['image']).replace("img_index",str(i))
        all_json.append(xx)
print("> give me  new json folder NAME with ipfs name :")
ipfs_png_folder=input()
try:
    os.mkdir(ipfs_png_folder)
except:
    pass
for i,v in enumerate(all_json):
    with open(ipfs_png_folder + '/' + str(i) + '.json', 'w') as fp:

        json.dump(v, fp, indent=4)