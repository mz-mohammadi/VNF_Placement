# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 20:16:22 2022

@author: mareed
"""
import random
import numpy

#parameters:

min_C_AVLB=30
max_C_AVLB=50
min_S_AVLB=70
max_S_AVLB=100
min_Delay=1
max_Delay=10
BW_Interval=200
min_BW_AVLB=800
min_IO_AVLB=50
max_IO_AVLB=70
min_C_VNF=10
max_C_VNF=20
min_S_VNF=20
max_S_VNF=40
min_IO_VNF=20
max_IO_VNF=30
min_BW_SFC=200
max_BW_SFC=400

V_Comp=[2,3,5,8,10,12,14,15,17,18,20,21,22,24,26,29,31,36,39,40,41,45,46,49,52,54,56,58,60,61,62,67,69,70,72,73,74,76,77,78,80,83,85,86,87,88,91,98,103,109,114,117,124,129,133,136,139,143,147]
VComp_num=len(V_Comp)
VNF_num=15
N_E=191

#Defining Substrate Graph Parameters:
Storage_AVLB=numpy.zeros(VComp_num)
Capacity_AVLB=numpy.zeros(VComp_num)
IO_AVLB=numpy.zeros(VComp_num)

VComp_IO_file="ColtTelecom_VCOMP_IO"+".csv"
IOFile=open(VComp_IO_file, 'a')
for i in range(0,VComp_num):
    IO_AVLB[i]=random.randint(min_IO_AVLB,max_IO_AVLB)
    IOFile.writelines([str(IO_AVLB[i]),'\n'])    
IOFile.close()

VComp_Capacity_file="ColtTelecom_VCOMP_Cap"+".csv"
CapacityFile=open(VComp_Capacity_file, 'a')
for i in range(0,VComp_num):
    Capacity_AVLB[i]=random.randint(min_C_AVLB,max_C_AVLB)
    CapacityFile.writelines([str(Capacity_AVLB[i]),'\n'])    
CapacityFile.close()

VComp_storage_file="ColtTelecom_VCOMP_Stor"+".csv"
StorageFile=open(VComp_storage_file, 'a')
for i in range(0,VComp_num):
    Storage_AVLB[i]=random.randint(min_S_AVLB,max_S_AVLB)
    StorageFile.writelines([str(Storage_AVLB[i]),'\n'])    
StorageFile.close()

#Defining VNF Parameters:
Storage_VNF=numpy.zeros(VNF_num)
Capacity_VNF=numpy.zeros(VNF_num)
IO_VNF=numpy.zeros(VNF_num)

VNF_storage_file="ColtTelecom_VNF_Stor"+".csv"
VNFStorageFile=open(VNF_storage_file, 'a')
for i in range(0,VNF_num):
    Storage_VNF[i]=random.randint(min_S_VNF,max_S_VNF)
    VNFStorageFile.writelines([str(Storage_VNF[i]),'\n'])    
VNFStorageFile.close()

VNF_Capacity_file="ColtTelecom_VNF_Cap"+".csv"
VNFCapacityFile=open(VNF_Capacity_file, 'a')
for i in range(0,VNF_num):
    Capacity_VNF[i]=random.randint(min_C_VNF,max_C_VNF)
    VNFCapacityFile.writelines([str(Capacity_VNF[i]),'\n'])    
VNFCapacityFile.close()

VNF_IO_file="ColtTelecom_VNF_IO"+".csv"
VNFIOFile=open(VNF_IO_file, 'a')
for i in range(0,VNF_num):
    IO_VNF[i]=random.randint(min_IO_VNF,max_IO_VNF)
    VNFIOFile.writelines([str(IO_VNF[i]),'\n'])    
VNFIOFile.close()

#Defining links delays:
link_delay=numpy.zeros(N_E)
link_delays_file="ColtTelecom_link_delays"+".csv"
linkdelayfile=open(link_delays_file, 'a')
for i in range(0,N_E):
    link_delay[i]=random.randint(min_Delay,max_Delay)
    linkdelayfile.writelines([str(link_delay[i]),'\n'])    
linkdelayfile.close()