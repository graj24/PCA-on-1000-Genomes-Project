# -*- coding: utf-8 -*-
"""finalMiniProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujyj4Ah5orf91-D_4eoGLnKesKb7AFV-
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np            #all the required import statements
import pandas as pd
import matplotlib as plt
# %matplotlib inline
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt

raw_data = pd.read_csv('p1dataset2021.txt', header=None,delim_whitespace=True)  # loading rawdata as a csv
df = raw_data.iloc[:,3:]                                                        # extracting the important data (the one required to perform PCA, rest of the 3 features have been cropped)
mode = df.mode()                                                                # extracted the mode of the data

for i in range(len(df.index)):  #rows  0 - 994                                  #conveting the data into binary data
    for j in range(3, df.shape[1]+3):  #col 3 - 10103
        if mode._get_value(0,j)==df._get_value(i,j):
            df._set_value(i,j,0)
        else:
            df._set_value(i,j,1)

df.shape                                                                        #checking the shape of the matrix which is 995*10101

population_type = raw_data.to_numpy()[:,2:3]                #storing the population-type vector   
gender_list = raw_data.to_numpy()[:,1:2]                    #storing the gender vector   
y = population_type

sdata = preprocessing.scale(df)                             # standardizing the data

pca = PCA(n_components=2)                                   # declaring PCA with 2 components
pca.fit(sdata)                                              #performing pca.fit on the data
pca.components_                                             #got PCA components
print(pca)
print(pca.components_.shape)

Z = pca.transform(sdata)                                #transforming the PCA data and storing it in Z
print(Z.shape)                                                 #checking the shape of the PCA which is 995*2 since we needed 2 components
print(Z)
data_pc1_pc2 = Z                                         #data that will be used for plotting PC1 and PC2

ppntype = list()                            #creating a list to store the distinct population type values, this is done to set the legend
for i in y.tolist():                          #using a for loop to get the distinct values
    if i[0] in ppntype:
        continue
    else:
        ppntype.append(i[0])
populationlist= list()                      #creating a new list to store all the population_type values in a proper list
for i in y.tolist():                        #for loop to store all the values of ppntype in a single list
  populationlist.append(i[0])
print(populationlist)

data_pc1_pc2 = pd.DataFrame(data=data_pc1_pc2,columns=["PC1","PC2"])        # making a dataframe for easier plotting and visualization
data_pc1_pc2['target']=populationlist                                       #appending target(population type) to the data
data_pc1_pc2

fig = plt.figure(figsize = (8,8))               #plotting of the data
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)  
targets = ppntype                               #setting targets to ppntype which contains the distinct values of population type i.e. contains 7 values
colors = ['r', 'g', 'b','black','orange','cyan','pink']  #setting different colors for different population type
for target, color in zip(targets,colors):                       #for loop for scatter plot
    indicesToKeep = data_pc1_pc2['target'] == target
    ax.scatter(data_pc1_pc2.loc[indicesToKeep, 'PC1']
               , data_pc1_pc2.loc[indicesToKeep, 'PC2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

pca_2 = PCA(n_components=3)                                   # declaring PCA with 3 components
pca_2.fit(sdata)                                              #performing pca.fit on the data
pca_2.components_                                             #got PCA components

Z1 = pca_2.transform(sdata)                                #transforming the PCA data and storing it in Z
print(Z1.shape)                                                 #checking the shape of the PCA which is 995*3 since we needed 3 components
print(Z1)
data_pc1_pc3 = Z1                                   #data that will be used for plotting PC1 and PC3

gender = list()                            #creating a list to store the distinct population type values, this is done to set the legend
for i in gender_list.tolist():                          #using a for loop to get the distinct values
    if i[0] in gender:
        continue
    else:
        gender.append(i[0])
gender_all= list()                      #creating a new list to store all the population_type values in a proper list
for i in gender_list.tolist():                        #for loop to store all the values of ppntype in a single list
  gender_all.append(i[0])
print(gender)
print(gender_all)

data_pc1_pc3 = pd.DataFrame(data=data_pc1_pc3,columns=["PC1","PC2","PC3"])        # making a dataframe for easier plotting and visualization
data_pc1_pc3['target']=gender_all                                       #appending target(population type) to the data
data_pc1_pc3

fig = plt.figure(figsize = (8,8))               #plotting of the data
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 3', fontsize = 15)
ax.set_title('2 Component PCA (PC1 and PC3)', fontsize = 20)  
targets = gender                               #setting targets to ppntype which contains the distinct values of population type i.e. contains 7 values
colors = ['r', 'b']  #setting different colors for different population type
for target, color in zip(targets,colors):                       #for loop for scatter plot
    indicesToKeep = data_pc1_pc3['target'] == target
    ax.scatter(data_pc1_pc3.loc[indicesToKeep, 'PC1']
               , data_pc1_pc3.loc[indicesToKeep, 'PC3']
               , c = color
               , s = 50)
ax.legend(["1 - Male","2 - Female"])
ax.grid()

abs_pc3 = np.absolute(pca_2.components_[2])
abs_pc3
print(len(abs_pc3))
x_range = pca_2.components_[2].shape[0]
x_range = np.arange(1,x_range+1)

fig = plt.figure(figsize = (8,8))               #plotting of the data
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Nucleobase Index', fontsize = 15)
ax.set_ylabel('Abs Principal Component 3', fontsize = 15)
ax.set_title('Nucleobase Index vs Abs of PC3', fontsize = 20)  
ax.scatter(x_range, abs_pc3, s = 50)
ax.grid()