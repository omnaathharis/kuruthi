
# coding: utf-8

# In[1]:


import os
import glob
import pandas
import shutil


# In[2]:


result = [i for i in glob.glob('*.csv')]
print (result)


# In[3]:


data = pandas.read_csv(result[0])
imaglst = data['ATTR_1']
print (imaglst[1:len(imaglst)])


# In[7]:


n=int(input('no:'))
dir_dst = input('enter the full output folder location :')
li=[]
for i in range(n):
    li.append(input('enter the full image folder location :'))
    
    
    


# In[21]:



for i in imaglst[1:]:
    for a in li:
        if(os.path.isfile(os.path.join(a,i))):
            shutil.copy(os.path.join(a, i), dir_dst)
    
       
        
            
                
        

