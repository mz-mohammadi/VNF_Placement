# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 10:48:25 2022

@author: mareed
"""
from cvxopt.glpk import ilp
import numpy as np
from cvxopt import matrix
from solution import solution
from dijkstra import dijkstra
import pandas as pd

dim=10
N=47
N_V=93

x=matrix(np.zeros(N_V*N_V*(dim-1),dtype=float))

"""xfile="x_OTE.csv" 
x_file=open(xfile, 'r')"""

"""lines_stor_VNF=[]
for line in x_file:
    lines_stor_VNF.append(line)
    
x=[]
for line in lines_stor_VNF:
    x.append(float(line))
"""
"""for i in range(N_V*N_V*(dim-1)):
    x[i]=float(x_file.read())
    x_file.readlines()

x_file.close()"""

x2=pd.read_csv(r"C:\A New Drive\uni\PHD\05. Dissertation\Implemetation\Python_Codes\ILP\unique_code\ILP_VNFP\x_OTE.csv")

x=matrix(np.zeros((N*N*(dim-1))))#x
for i in range(N*N*(dim-1)):
    x[i]=float(x2.iloc[i,0])
        
c2=pd.read_csv(r"C:\A New Drive\uni\PHD\05. Dissertation\Implemetation\Python_Codes\ILP\unique_code\ILP_VNFP\c_file.csv")

c=matrix(np.zeros((N*N*(dim-1))))#x
for i in range(N*N*(dim-1)):
    c[i]=float(c2.iloc[i,0])

print("del:",c.T*x)

#R=matrix(np.zeros((3*N_V,N_V*dim)))#G=R*L:(3N_V) X (N_V*dim)
R2=matrix(np.zeros((3*N,N*dim)))#G=R*L:(3N_V) X (N_V*dim)
h=matrix(np.zeros(3*N))
#L=matrix(np.zeros((dim*N_V*N_V*N_V*(dim-1))))
L2=matrix(np.zeros((dim*N,N*N*(dim-1))))
A2=matrix(np.zeros((dim*N+dim,N*N*(dim-1))))
AP=matrix(np.zeros((dim,N*dim)))#َAP:E

#AP2=pd.read_csv(r"C:\A New Drive\uni\PHD\05. Dissertation\Implemetation\Python_Codes\ILP\unique_code\ILP_VNFP\AP_file.csv")

#for i in range(dim):
#   for j in range(N*dim):
#       AP[i,j]=float(AP2.iloc[i,j])

#test=pd.read_csv(r"C:\A New Drive\uni\PHD\05. Dissertation\Implemetation\Python_Codes\ILP\unique_code\ILP_VNFP\test_file.csv")
#print("test:",test.iloc[0,0],test.iloc[2,2])


R=pd.read_csv(r"C:\A New Drive\uni\PHD\05. Dissertation\Implemetation\Python_Codes\ILP\unique_code\ILP_VNFP\R_file.csv")

for i in range(3*N):
    for j in range(N*dim):
        R2[i,j]=float(R.iloc[i,j])

L=pd.read_csv(r"C:\A New Drive\uni\PHD\05. Dissertation\Implemetation\Python_Codes\ILP\unique_code\ILP_VNFP\L3_file.csv")

for k in range(2):
    for i in range(dim*N):
        if k==0:
            for j in range(10919):#N*N*(dim-1)):
                L2[i,j]=float(L.iloc[2*i,j])
        else:
            for j in range(8962):#N*N*(dim-1)):
                L2[i,10919+j]=float(L.iloc[2*i+1,j])
                
A=pd.read_csv(r"C:\A New Drive\uni\PHD\05. Dissertation\Implemetation\Python_Codes\ILP\unique_code\ILP_VNFP\A5_file.csv")

for k in range(2):
    for i in range(dim*N+dim):
        if k==0:
            for j in range(10919):#N*N*(dim-1)):
                A2[i,j]=float(A.iloc[2*i,j])
        else:
            for j in range(8962):#N*N*(dim-1)):
                A2[i,10919+j]=float(A.iloc[2*i+1,j])
                
G=R2*L2
T=G*x
b=A2*x

P_file="h_OTE_file"+".csv"
PFile=open(P_file, 'a')
for i in range(3*N):
    PFile.writelines([str(T[i])])
PFile.close()

P_file="b_OTE2_file"+".csv"
PFile=open(P_file, 'a')
for i in range(dim+dim*N):
    PFile.writelines([str(b[i])])
PFile.close()
