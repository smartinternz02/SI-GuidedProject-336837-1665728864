# -*- coding: utf-8 -*-
"""Forest_Cnn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17_XhUQEa_K7NaJbNcfCs2nvTACqvXgzJ
"""

import numpy as np#used for numerical analysis
import tensorflow #open source used for both ML and DL for computation
from tensorflow.keras.models import Sequential #it is a plain stack of layers
from tensorflow.keras import layers #A layer consists of a tensor-in tensor-out computation function
#Dense layer is the regular deeply connected neural network layer
from tensorflow.keras.layers import Dense,Flatten
#Faltten-used fot flattening the input or change the dimension
from tensorflow.keras.layers import Conv2D,MaxPooling2D #Convolutional layer
#MaxPooling2D-for downsampling the image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

test_datagen=ImageDataGenerator(rescale=1./255)

x_train=train_datagen.flow_from_directory(directory=r'/content/drive/MyDrive/forest fire/Dataset/train_set',target_size=(64,64),batch_size=32,class_mode='categorical')

x_test=test_datagen.flow_from_directory(directory=r'/content/drive/MyDrive/forest fire/Dataset/test_set',target_size=(64,64),batch_size=32,class_mode='categorical')

print(x_train.class_indices)

from collections import Counter as c
c(x_train.labels)

model=Sequential()

model.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(32))
model.add(Dense(2,activation='softmax'))

model.summary()

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

len(x_train)

model.fit(x_train,steps_per_epoch=len(x_train),validation_data=x_test,validation_steps=len(x_test),epochs=10)

model.save('forest.h5')

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
model = load_model("forest.h5")

img = image.load_img(r"/content/drive/MyDrive/forest fire/Dataset/train_set/forest/with_fire (1).gif",target_size= (64,64))#loading of the image
x = image.img_to_array(img)#image to array
x = np.expand_dims(x,axis = 0)
preds=model.predict(x)
pred=np.argmax(preds,axis=1)
preds

img

index=['Forest','With Fire']
result=str(index[pred[0]])
result

img = image.load_img(r"/content/drive/MyDrive/forest fire/Dataset/train_set/with fire/with fire (105).jpg",target_size= (64,64))#loading of the image
x = image.img_to_array(img)#image to array
x = np.expand_dims(x,axis = 0)#changing the shape
#pred = model.predict_classes(x)#predicting the classes
#pred
preds=model.predict(x)
pred=np.argmax(preds,axis=1)
preds

img

index=['Forest','With Fire']
result=str(index[pred[0]])
result

img = image.load_img(r"/content/drive/MyDrive/forest fire/Dataset/test_set/forest/1170x500_Ireland_web.jpg",target_size= (64,64))#loading of the image
x = image.img_to_array(img)#image to array
x = np.expand_dims(x,axis = 0)#changing the shape
preds=model.predict(x)
pred=np.argmax(preds,axis=1)
index=['Forest','With Fire']
result=str(index[pred[0]])
result

img

index=['Forest','With Fire']
result=str(index[pred[0]])
result

