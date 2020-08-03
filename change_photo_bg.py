from removebg import RemoveBg
import os
import sys

rmbg = RemoveBg('yGvc1A92w5wszi6j1oW11S9S',"error.log")
path = '%s/pictures'%os.getcwd() 

for pic in os.listdir(path):    
    rmbg.remove_background_from_img_file("%s/%s" %(path,pic))
# 这里注意：win系统和Linux系统的路径斜杠不一样，如果是Linux要用/，而win系统要用\ 


