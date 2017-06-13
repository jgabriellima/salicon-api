
# coding: utf-8

# In[1]:

#get_ipython().magic(u'reload_ext autoreload')
#get_ipython().magic(u'autoreload 2')
#get_ipython().magic(u'matplotlib inline')
from salicon.salicon import SALICON
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import cv2
import scipy.misc

# In[2]:

dataDir='..'
dataType='train2014examples'
annFile='%s/annotations/fixations_%s.json'%(dataDir,dataType)


# In[3]:

# initialize COCO api for instance annotations
salicon=SALICON(annFile)


# In[4]:

# get all images 
save_dir = '../gt_examples/'
imgIds = salicon.getImgIds();
print len(imgIds)
for each in range(0, len(imgIds)):
    img = salicon.loadImgs(imgIds[each])[0]
# load and display image
    I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
# load and display instance annotations
#plt.imshow(I)
    annIds = salicon.getAnnIds(imgIds=img['id'])
    anns = salicon.loadAnns(annIds)
    sal_map = salicon.buildFixMap(anns)
    print img['file_name']
    scipy.misc.imsave(save_dir + img['file_name'], sal_map)


# In[ ]:



