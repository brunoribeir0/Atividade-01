
# coding: utf-8

# In[61]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
from pandas import DataFrame , read_csv


# In[7]:


dataset=pd.read_csv(r"C:\Users\compu\Desktop\Iniciacao\teste.csv",sep='~')


# In[82]:


type(dataset)
dataset.count()


# In[38]:


dataset.head(5183)


# In[ ]:


#Exercicío 1 - No site do Cenipa não aparece nenhuma informação de ocorrências por ano para ser extraida


# In[39]:


#Atividade 2#
pd.value_counts(dataset['ocorrencia_uf'])


# In[80]:


uf=dataset['ocorrencia_uf'].value_counts()



# In[91]:


plt.figure()
sns.barplot(uf.index, uf.values) #O seaborn barplot seta o index como a primeira colula e o value os dados dessa
plt.title('Grafico de Ocorrencias por Estado')
plt.ylabel('Ocorrencias', fontsize=12)
plt.xlabel('Estados', fontsize=12)
plt.show()


# In[123]:


#Exercício 3 - Qual estado tem mais ocorrências?
df=pd.DataFrame(uf)
df.idxmax()
# df.max() como faze aparecer o valor junto?

