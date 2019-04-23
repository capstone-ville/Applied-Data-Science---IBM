
# coding: utf-8

# In[ ]:


#Programa de Analítica Avanzada - APORTA
#Fernando Díaz Loo


# In[7]:


import pandas as pd 
import numpy as np
import sys


# In[86]:


def distancia(x,y):
    return(x-y)**2


# In[81]:


def get_dtw(s, t):
    M=len(s)
    N=len(t)
    matriz=np.full((M,N),np.inf)
    matriz[0,0]=distancia(s[0],t[0])
    
    for i in range(1,M):
        costo=distancia(s[i],t[0])
        matriz[i][0]=costo + matriz[i-1,0]
        
    for j in range(1,N):
        costo=distancia(s[0],t[j])
        matriz[0][j]=costo + matriz[0,j-1]
    
    for i in range(1, M):
        for j in range(1,N):
            costo=distancia(s[i],t[j])
            matriz[i][j]=costo + min (matriz[i-1,j],matriz[i,j-1],matriz[i-1,j-1])
    
    return matriz[M-1,N-1]


# In[114]:


with open("C:/Users/FERNANDO/Desktop/Train.txt","r") as file:
    train_series_aux = file.readlines()
with open("C:/Users/FERNANDO/Desktop/Test.txt","r") as file:
    test_series_aux = file.readlines()

train_series=[]
for item in train_series_aux: 
    train_series.append(item.split(" "))

test_series=[]
for item in test_series_aux: 
    test_series.append(item.split(" "))


# In[135]:


train_movimientos=[]
for item in train_series: 
    train_movimientos.append(float(item[0]))
train_acelerometro_aux=[]
for item in train_series: 
    new_item=[]
    for element in item:
        new_item.append(float(element))
    train_acelerometro_aux.append(new_item)
train_acelerometro=[]
for item in train_acelerometro_aux: 
    train_acelerometro.append(item[1:len(item)])
    
test_movimientos=[]
for item in test_series: 
    test_movimientos.append(float(item[0]))
test_acelerometro_aux=[]
for item in test_series: 
    new_item=[]
    for element in item:
        new_item.append(float(element))
    test_acelerometro_aux.append(new_item)
test_acelerometro=[]
for item in test_acelerometro_aux: 
    test_acelerometro.append(item[1:len(item)])


# In[142]:


test_acelerometro


# In[159]:


def predictions(test_acelerometro,train_acelerometro,train_movimientos):
    
    predicciones_test=[]
   
    for acelerometro_test in test_acelerometro:
        min_dtw=sys.maxsize
        min_index=0
        
        for acelerometro_train in train_acelerometro: 
            dtw=get_dtw(acelerometro_test,acelerometro_train)
            if dtw < min_dtw:
                min_dtw=dtw
                min_train=acelerometro_train
        predicciones_test.append(train_movimientos[train_acelerometro.index(min_train)])
    return predicciones_test


# In[160]:


prueba1=test_acelerometro[0:5]
prueba2=train_acelerometro[0:5]
prueba3=train_movimientos[0:5]


# In[161]:


prueba=predictions(prueba1,prueba2,prueba3)


# In[162]:


print(prueba)


# In[163]:


movimiento_predictions=predictions(test_acelerometro,train_acelerometro,train_movimientos)


# In[164]:


#Cálculo de Accuracy
num_correctos=0
for prediccion,categoria in zip(movimiento_predictions,test_movimientos):
    if prediccion==categoria:
        num_correctos=num_correctos+1
        
accuracy=num_correctos/len(test_movimientos)
print(accuracy)

