
# coding: utf-8

# In[9]:


import cv2


# In[10]:


camera = cv2.VideoCapture(0)
file_name = "photo.png"
res,camera_capture = camera.read()
cv2.imwrite(file_name, camera_capture)
del(camera)
img = cv2.imread(file_name)


# In[11]:


cv2.startWindowThread()
cv2.imshow("",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


# In[13]:


img=cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(100,100,200),2)
img =cv2.rectangle(img,(img.shape[1]//5,img.shape[0]//5),(img.shape[1]*4//5,img.shape[0]*4//5),(200,100,100),2)


# In[14]:


cv2.startWindowThread()
cv2.imshow("",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

