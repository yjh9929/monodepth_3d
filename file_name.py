import os
from glob import glob

f = open("dataset_full.txt", 'w')

#f_path = 'monodepth2/kitti_data/'
filenames = glob('monodepth2/kitti_data/**/**/image_02/**/**.jpg')

for filename in filenames:
    data = filename+"\n"
    f.write(data)

print("finished")

f.close()