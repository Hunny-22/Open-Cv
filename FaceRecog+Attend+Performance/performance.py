import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset= pd.read_csv("Data.csv")
store=dict({})
for i in dataset.columns:
    store.update({i:np.array(dataset[i])})
l1=store['Subject']
del store['Subject']
name=input("Student name from database: ")
for i in store:
    if(i==name):
        l2=store[name]
ypos=np.arange(len(l1))
plt.xticks(ypos,l1)
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title(name)
for index,value in enumerate(l2):
    plt.text(value,index,str(value))
plt.barh(l1,l2)
plt.show()
