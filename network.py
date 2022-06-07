# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:54:25 2022

@author: mareed
"""
#definig substrate graph:
#parameters:

"""min_C_AVLB=30
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
"""
from collections import namedtuple
import numpy

def network(net):
    
    Edge = namedtuple('Edge', ['vertex', 'weight'])
    
    class GraphUndirectedWeighted(object):  
        def __init__(self, vertex_count):
            self.vertex_count = vertex_count
            self.adjacency_list = [[] for _ in range(vertex_count)]
    
        def add_edge(self, source, dest, weight):
            assert source < self.vertex_count
            assert dest < self.vertex_count
            self.adjacency_list[source].append(Edge(dest, weight))
            self.adjacency_list[dest].append(Edge(source, weight))
    
        def get_edge(self, vertex):
            for e in self.adjacency_list[int(vertex)]:
                yield e
    
        def get_vertex(self):
            for v in range(self.vertex_count):
                yield v

    if net==0:#CRL
        V_Comp=[2,3,5,8,10,12,14,15,17,18,20,21,22,24,26,29,31]
        VComp_num=len(V_Comp)#17
        VNF_num=7
        Max_time=100
        N_V=33
        N_E=38
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="CRL_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="CRL_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="CRL_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="CRL_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="CRL_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="CRL_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #N_E=38
        
        #Reading link_delay from file:
        link_delay=numpy.zeros(N_E)
        link_delays_file="CRL_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # CRL Network:
        #N_V=33
        substrate_graph=GraphUndirectedWeighted(N_V)
        
        substrate_graph.add_edge(0, 1,link_delay[0])
        substrate_graph.add_edge(0, 3,link_delay[1])
        substrate_graph.add_edge(1, 6,link_delay[2])
        substrate_graph.add_edge(2, 24,link_delay[3])
        substrate_graph.add_edge(2, 3,link_delay[4])
        substrate_graph.add_edge(4, 5,link_delay[5])
        substrate_graph.add_edge(4, 7,link_delay[6])
        substrate_graph.add_edge(5, 6,link_delay[7])
        substrate_graph.add_edge(6, 8,link_delay[8])
        substrate_graph.add_edge(6, 13,link_delay[9])
        substrate_graph.add_edge(6, 7,link_delay[10])
        substrate_graph.add_edge(8, 9,link_delay[11])
        substrate_graph.add_edge(8, 12,link_delay[12])
        substrate_graph.add_edge(9, 18,link_delay[13])
        substrate_graph.add_edge(10, 11,link_delay[14])
        substrate_graph.add_edge(10, 13,link_delay[15])
        substrate_graph.add_edge(11, 32,link_delay[16])
        substrate_graph.add_edge(13, 19,link_delay[17])
        substrate_graph.add_edge(14, 18,link_delay[18])
        substrate_graph.add_edge(14, 21,link_delay[19])
        substrate_graph.add_edge(15, 16,link_delay[20])
        substrate_graph.add_edge(15, 22,link_delay[21])
        substrate_graph.add_edge(16, 17,link_delay[22])
        substrate_graph.add_edge(17, 18,link_delay[23])
        substrate_graph.add_edge(19, 25,link_delay[24])
        substrate_graph.add_edge(19, 20,link_delay[25])
        substrate_graph.add_edge(20, 21,link_delay[26])
        substrate_graph.add_edge(21, 22,link_delay[27])
        substrate_graph.add_edge(23, 24,link_delay[28])
        substrate_graph.add_edge(23, 32,link_delay[29])
        substrate_graph.add_edge(25, 26,link_delay[30])
        substrate_graph.add_edge(26, 27,link_delay[31])
        substrate_graph.add_edge(27, 28,link_delay[32])
        substrate_graph.add_edge(27, 31,link_delay[33])
        substrate_graph.add_edge(28, 29,link_delay[34])
        substrate_graph.add_edge(29, 30,link_delay[35])
        substrate_graph.add_edge(30, 32,link_delay[36])
        substrate_graph.add_edge(31, 32,link_delay[37])

    elif net==1:#NIIF
        
        V_Comp=[2,3,5,8,10,12,14,15,17,18,20,21,22,24,26,29,31]
        VComp_num=len(V_Comp)#17
        VNF_num=8
        Max_time=100
        N_V=36
        N_E=41
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="NIIF_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="NIIF_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="NIIF_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="NIIF_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="NIIF_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="NIIF_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #N_E=41
        
        link_delay=numpy.zeros(N_E)
        link_delays_file="NIIF_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # NIIF Network:
        #N_V=36
        substrate_graph=GraphUndirectedWeighted(N_V)
        substrate_graph.add_edge(0, 32, link_delay[0])
        substrate_graph.add_edge(0, 1, link_delay[1])
        substrate_graph.add_edge(0, 3, link_delay[2])
        substrate_graph.add_edge(0, 7, link_delay[3])
        substrate_graph.add_edge(2, 4, link_delay[4])
        substrate_graph.add_edge(4, 32, link_delay[5])
        substrate_graph.add_edge(4, 5, link_delay[6])
        substrate_graph.add_edge(5, 8, link_delay[7])
        substrate_graph.add_edge(6, 7, link_delay[8])
        substrate_graph.add_edge(7, 32, link_delay[9])
        substrate_graph.add_edge(7, 19, link_delay[10])
        substrate_graph.add_edge(8, 9, link_delay[11])
        substrate_graph.add_edge(9, 21, link_delay[12])
        substrate_graph.add_edge(10, 11, link_delay[13])
        substrate_graph.add_edge(11, 32, link_delay[14])
        substrate_graph.add_edge(11, 27, link_delay[15])
        substrate_graph.add_edge(11, 12, link_delay[16])
        substrate_graph.add_edge(13, 16, link_delay[17])
        substrate_graph.add_edge(13, 14, link_delay[18])
        substrate_graph.add_edge(14, 15, link_delay[19])
        substrate_graph.add_edge(15, 27, link_delay[20])
        substrate_graph.add_edge(16, 23, link_delay[21])
        substrate_graph.add_edge(17, 23, link_delay[22])
        substrate_graph.add_edge(18, 25, link_delay[23])
        substrate_graph.add_edge(18, 19, link_delay[24])
        substrate_graph.add_edge(19, 20, link_delay[25])
        substrate_graph.add_edge(21, 32, link_delay[26])
        substrate_graph.add_edge(22, 23, link_delay[27])
        substrate_graph.add_edge(23, 32, link_delay[28])
        substrate_graph.add_edge(23, 25, link_delay[29])
        substrate_graph.add_edge(24, 25, link_delay[30])
        substrate_graph.add_edge(25, 32, link_delay[31])
        substrate_graph.add_edge(26, 35, link_delay[32])
        substrate_graph.add_edge(27, 35, link_delay[33])
        substrate_graph.add_edge(28, 32, link_delay[34])
        substrate_graph.add_edge(29, 32, link_delay[35])
        substrate_graph.add_edge(30, 32, link_delay[36])
        substrate_graph.add_edge(31, 32, link_delay[37])
        substrate_graph.add_edge(32, 33, link_delay[38])
        substrate_graph.add_edge(32, 34, link_delay[39])
        substrate_graph.add_edge(32, 35, link_delay[40])        
        
    elif net==2:#DFN
        
        V_Comp=[1,3,4,8,11,14,16,19,22,24,26,28,31,34,37,39,41,42,45,47,49,51,53,55,57]
        VComp_num=len(V_Comp)#25
        VNF_num=9
        Max_time=200
        N_V=58
        N_E=87
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="DFN_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="DFN_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="DFN_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="DFN_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="DFN_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="DFN_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #N_E=87
        
        link_delay=numpy.zeros(N_E)
        link_delays_file="DFN_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # DFN Network:
        #N_V=58
        
        substrate_graph=GraphUndirectedWeighted(N_V)
        
        substrate_graph.add_edge(0,1,link_delay[0])
        substrate_graph.add_edge(0,3,link_delay[1])
        substrate_graph.add_edge(1,53,link_delay[2])
        substrate_graph.add_edge(1,6,link_delay[3])
        substrate_graph.add_edge(1,15,link_delay[4])
        substrate_graph.add_edge(2,56,link_delay[5])
        substrate_graph.add_edge(2,49,link_delay[6])
        substrate_graph.add_edge(3,52,link_delay[7])
        substrate_graph.add_edge(3,53,link_delay[8])
        substrate_graph.add_edge(4,51,link_delay[9])
        substrate_graph.add_edge(4,5,link_delay[10])
        substrate_graph.add_edge(5,10,link_delay[11])
        substrate_graph.add_edge(6,7,link_delay[12])
        substrate_graph.add_edge(7,53,link_delay[13])
        substrate_graph.add_edge(8,51,link_delay[14])
        substrate_graph.add_edge(9,51,link_delay[15])
        substrate_graph.add_edge(10,11,link_delay[16])
        substrate_graph.add_edge(10,51,link_delay[17])
        substrate_graph.add_edge(10,36,link_delay[18])
        substrate_graph.add_edge(11,43,link_delay[19])
        substrate_graph.add_edge(12,52,link_delay[20])
        substrate_graph.add_edge(13,52,link_delay[21])
        substrate_graph.add_edge(14,24,link_delay[22])
        substrate_graph.add_edge(14,50,link_delay[23])
        substrate_graph.add_edge(14,27,link_delay[24])
        substrate_graph.add_edge(16,50,link_delay[25])
        substrate_graph.add_edge(16,23,link_delay[26])
        substrate_graph.add_edge(17,25,link_delay[27])
        substrate_graph.add_edge(17,50,link_delay[28])
        substrate_graph.add_edge(17,31,link_delay[29])
        substrate_graph.add_edge(18,19,link_delay[30])
        substrate_graph.add_edge(18,38,link_delay[31])
        substrate_graph.add_edge(19,51,link_delay[32])
        substrate_graph.add_edge(19,20,link_delay[33])
        substrate_graph.add_edge(20,46,link_delay[34])
        substrate_graph.add_edge(21,22,link_delay[35])
        substrate_graph.add_edge(21,23,link_delay[36])
        substrate_graph.add_edge(22,51,link_delay[37])
        substrate_graph.add_edge(23,24,link_delay[38])
        substrate_graph.add_edge(25,27,link_delay[39])
        substrate_graph.add_edge(26,50,link_delay[40])
        substrate_graph.add_edge(27,44,link_delay[41])
        substrate_graph.add_edge(28,51,link_delay[42])
        substrate_graph.add_edge(28,36,link_delay[43])
        substrate_graph.add_edge(29,51,link_delay[44])
        substrate_graph.add_edge(30,48,link_delay[45])
        substrate_graph.add_edge(30,31,link_delay[46])
        substrate_graph.add_edge(32,33,link_delay[47])
        substrate_graph.add_edge(32,50,link_delay[48])
        substrate_graph.add_edge(33,50,link_delay[49])
        substrate_graph.add_edge(33,37,link_delay[50])
        substrate_graph.add_edge(34,35,link_delay[51])
        substrate_graph.add_edge(34,52,link_delay[52])
        substrate_graph.add_edge(35,50,link_delay[53])
        substrate_graph.add_edge(36,51,link_delay[54])
        substrate_graph.add_edge(37,52,link_delay[55])
        substrate_graph.add_edge(38,39,link_delay[56])
        substrate_graph.add_edge(39,44,link_delay[57])
        substrate_graph.add_edge(40,41,link_delay[58])
        substrate_graph.add_edge(40,43,link_delay[59])
        substrate_graph.add_edge(41,53,link_delay[60])
        substrate_graph.add_edge(42,43,link_delay[61])
        substrate_graph.add_edge(42,53,link_delay[62])
        substrate_graph.add_edge(43,51,link_delay[63])
        substrate_graph.add_edge(44,50,link_delay[64])
        substrate_graph.add_edge(44,45,link_delay[65])
        substrate_graph.add_edge(45,46,link_delay[66])
        substrate_graph.add_edge(46,51,link_delay[67])
        substrate_graph.add_edge(47,51,link_delay[68])
        substrate_graph.add_edge(47,53,link_delay[69])
        substrate_graph.add_edge(48,56,link_delay[70])
        substrate_graph.add_edge(48,49,link_delay[71])
        substrate_graph.add_edge(48,52,link_delay[72])
        substrate_graph.add_edge(48,57,link_delay[73])
        substrate_graph.add_edge(50,51,link_delay[74])
        substrate_graph.add_edge(50,52,link_delay[75])
        substrate_graph.add_edge(50,53,link_delay[76])
        substrate_graph.add_edge(50,55,link_delay[77])
        substrate_graph.add_edge(51,52,link_delay[78])
        substrate_graph.add_edge(51,53,link_delay[79])
        substrate_graph.add_edge(52,53,link_delay[80])
        substrate_graph.add_edge(52,54,link_delay[81])
        substrate_graph.add_edge(52,55,link_delay[82])
        substrate_graph.add_edge(52,56,link_delay[83])
        substrate_graph.add_edge(53,54,link_delay[84])
        substrate_graph.add_edge(55,56,link_delay[85])
        substrate_graph.add_edge(56,57,link_delay[86])
        
    elif net==3:#Uninett
    
        V_Comp=[1,3,5,9,11,14,16,18,21,23,25,29,32,34,36,38,41,43,44,46,48,49,51,53,55,58,60,63,64,66,67,68]
        VComp_num=len(V_Comp)#32
        VNF_num=9
        Max_time=200
        N_V=69
        N_E=98
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="Uninett_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="Uninett_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="Uninett_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="Uninett_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="Uninett_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="Uninett_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #N_E=98
        
        link_delay=numpy.zeros(N_E)
        link_delays_file="Uninett_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # Uninett Network:
        #N_V=69
        
        substrate_graph=GraphUndirectedWeighted(N_V)
        
        substrate_graph.add_edge(0,1,link_delay[0])
        substrate_graph.add_edge(0,3,link_delay[1])
        substrate_graph.add_edge(0,68,link_delay[2])
        substrate_graph.add_edge(0,49,link_delay[3])
        substrate_graph.add_edge(0,54,link_delay[4])
        substrate_graph.add_edge(0,23,link_delay[5])
        substrate_graph.add_edge(1,32,link_delay[6])
        substrate_graph.add_edge(1,3,link_delay[7])
        substrate_graph.add_edge(1,6,link_delay[8])
        substrate_graph.add_edge(1,48,link_delay[9])
        substrate_graph.add_edge(1,58,link_delay[10])
        substrate_graph.add_edge(1,62,link_delay[11])
        substrate_graph.add_edge(2,3,link_delay[12])
        substrate_graph.add_edge(2,60,link_delay[13])
        substrate_graph.add_edge(3,5,link_delay[14])
        substrate_graph.add_edge(3,45,link_delay[15])
        substrate_graph.add_edge(3,46,link_delay[16])
        substrate_graph.add_edge(3,22,link_delay[17])
        substrate_graph.add_edge(3,61,link_delay[18])
        substrate_graph.add_edge(4,5,link_delay[19])
        substrate_graph.add_edge(4,7,link_delay[20])
        substrate_graph.add_edge(5,10,link_delay[21])
        substrate_graph.add_edge(5,54,link_delay[22])
        substrate_graph.add_edge(6,51,link_delay[23])
        substrate_graph.add_edge(7,51,link_delay[24])
        substrate_graph.add_edge(8,65,link_delay[25])
        substrate_graph.add_edge(8,36,link_delay[26])
        substrate_graph.add_edge(8,37,link_delay[27])
        substrate_graph.add_edge(8,9,link_delay[28])
        substrate_graph.add_edge(8,29,link_delay[29])
        substrate_graph.add_edge(8,62,link_delay[30])
        substrate_graph.add_edge(9,26,link_delay[31])
        substrate_graph.add_edge(10,50,link_delay[32])
        substrate_graph.add_edge(10,11,link_delay[33])
        substrate_graph.add_edge(12,32,link_delay[34])
        substrate_graph.add_edge(12,15,link_delay[35])
        substrate_graph.add_edge(12,29,link_delay[36])
        substrate_graph.add_edge(12,61,link_delay[37])
        substrate_graph.add_edge(12,13,link_delay[38])
        substrate_graph.add_edge(13,40,link_delay[39])
        substrate_graph.add_edge(13,43,link_delay[40])
        substrate_graph.add_edge(13,43,link_delay[41])
        substrate_graph.add_edge(13,29,link_delay[42])
        substrate_graph.add_edge(14,30,link_delay[43])
        substrate_graph.add_edge(14,31,link_delay[44])
        substrate_graph.add_edge(15,42,link_delay[45])
        substrate_graph.add_edge(15,43,link_delay[46])
        substrate_graph.add_edge(16,17,link_delay[47])
        substrate_graph.add_edge(16,61,link_delay[48])
        substrate_graph.add_edge(16,22,link_delay[49])
        substrate_graph.add_edge(16,39,link_delay[50])
        substrate_graph.add_edge(17,25,link_delay[51])
        substrate_graph.add_edge(18,19,link_delay[52])
        substrate_graph.add_edge(18,20,link_delay[53])
        substrate_graph.add_edge(18,46,link_delay[54])
        substrate_graph.add_edge(18,23,link_delay[55])
        substrate_graph.add_edge(20,21,link_delay[56])
        substrate_graph.add_edge(21,22,link_delay[57])
        substrate_graph.add_edge(22,23,link_delay[58])
        substrate_graph.add_edge(22,24,link_delay[59])
        substrate_graph.add_edge(22,61,link_delay[60])
        substrate_graph.add_edge(24,25,link_delay[61])
        substrate_graph.add_edge(25,38,link_delay[62])
        substrate_graph.add_edge(26,61,link_delay[63])
        substrate_graph.add_edge(26,29,link_delay[64])
        substrate_graph.add_edge(27,35,link_delay[65])
        substrate_graph.add_edge(27,36,link_delay[66])
        substrate_graph.add_edge(27,61,link_delay[67])
        substrate_graph.add_edge(28,32,link_delay[68])
        substrate_graph.add_edge(30,56,link_delay[69])
        substrate_graph.add_edge(31,44,link_delay[70])
        substrate_graph.add_edge(33,40,link_delay[71])
        substrate_graph.add_edge(34,35,link_delay[72])
        substrate_graph.add_edge(34,62,link_delay[73])
        substrate_graph.add_edge(39,41,link_delay[74])
        substrate_graph.add_edge(41,63,link_delay[75])
        substrate_graph.add_edge(42,56,link_delay[76])
        substrate_graph.add_edge(42,44,link_delay[77])
        substrate_graph.add_edge(43,56,link_delay[78])
        substrate_graph.add_edge(43,62,link_delay[79])
        substrate_graph.add_edge(46,47,link_delay[80])
        substrate_graph.add_edge(47,53,link_delay[81])
        substrate_graph.add_edge(48,50,link_delay[82])
        substrate_graph.add_edge(49,50,link_delay[83])
        substrate_graph.add_edge(52,54,link_delay[84])
        substrate_graph.add_edge(53,54,link_delay[85])
        substrate_graph.add_edge(54,55,link_delay[86])
        substrate_graph.add_edge(57,64,link_delay[87])
        substrate_graph.add_edge(57,66,link_delay[88])
        substrate_graph.add_edge(59,67,link_delay[89])
        substrate_graph.add_edge(59,60,link_delay[90])
        substrate_graph.add_edge(61,62,link_delay[91])
        substrate_graph.add_edge(61,63,link_delay[92])
        substrate_graph.add_edge(62,63,link_delay[93])
        substrate_graph.add_edge(62,63,link_delay[94])
        substrate_graph.add_edge(63,64,link_delay[95])
        substrate_graph.add_edge(66,67,link_delay[96])
        substrate_graph.add_edge(67,68,link_delay[97])
        
    elif net==4:#TWTelecom
        
        V_Comp=[1,3,5,9,11,14,16,18,21,23,25,29,32,34,36,38,41,43,44,46,48,49,51,53,55,58,60,63,64,66,67,69,72,74,75]
        VComp_num=len(V_Comp)#35
        VNF_num=9
        Max_time=300
        N_V=76
        N_E=118
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="TWTelecom_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="TWTelecom_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="TWTelecom_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="TWTelecom_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="TWTelecom_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="TWTelecom_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #N_E=118
        
        link_delay=numpy.zeros(N_E)
        link_delays_file="TWTelecom_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # TWTelecom Network:
        #N_V=76
        
        substrate_graph=GraphUndirectedWeighted(N_V)
        
        substrate_graph.add_edge(0,1,link_delay[0])
        substrate_graph.add_edge(0,1,link_delay[1])
        substrate_graph.add_edge(0,67,link_delay[2])
        substrate_graph.add_edge(1,3,link_delay[3])
        substrate_graph.add_edge(1,6,link_delay[4])
        substrate_graph.add_edge(2,66,link_delay[5])
        substrate_graph.add_edge(2,54,link_delay[6])
        substrate_graph.add_edge(3,10,link_delay[7])
        substrate_graph.add_edge(4,5,link_delay[8])
        substrate_graph.add_edge(5,10,link_delay[9])
        substrate_graph.add_edge(5,7,link_delay[10])
        substrate_graph.add_edge(6,7,link_delay[11])
        substrate_graph.add_edge(6,10,link_delay[12])
        substrate_graph.add_edge(6,54,link_delay[13])
        substrate_graph.add_edge(6,55,link_delay[14])
        substrate_graph.add_edge(6,56,link_delay[15])
        substrate_graph.add_edge(8,9,link_delay[16])
        substrate_graph.add_edge(9,27,link_delay[17])
        substrate_graph.add_edge(9,27,link_delay[18])
        substrate_graph.add_edge(10,32,link_delay[19])
        substrate_graph.add_edge(10,70,link_delay[20])
        substrate_graph.add_edge(10,11,link_delay[21])
        substrate_graph.add_edge(10,57,link_delay[22])
        substrate_graph.add_edge(11,71,link_delay[23])
        substrate_graph.add_edge(12,72,link_delay[24])
        substrate_graph.add_edge(12,34,link_delay[25])
        substrate_graph.add_edge(12,13,link_delay[26])
        substrate_graph.add_edge(12,47,link_delay[27])
        substrate_graph.add_edge(14,36,link_delay[28])
        substrate_graph.add_edge(14,15,link_delay[29])
        substrate_graph.add_edge(15,72,link_delay[30])
        substrate_graph.add_edge(15,27,link_delay[31])
        substrate_graph.add_edge(15,63,link_delay[32])
        substrate_graph.add_edge(16,17,link_delay[33])
        substrate_graph.add_edge(16,25,link_delay[34])
        substrate_graph.add_edge(17,38,link_delay[35])
        substrate_graph.add_edge(17,44,link_delay[36])
        substrate_graph.add_edge(17,61,link_delay[37])
        substrate_graph.add_edge(17,25,link_delay[38])
        substrate_graph.add_edge(17,29,link_delay[39])
        substrate_graph.add_edge(18,51,link_delay[40])
        substrate_graph.add_edge(18,51,link_delay[41])
        substrate_graph.add_edge(18,20,link_delay[42])
        substrate_graph.add_edge(19,51,link_delay[43])
        substrate_graph.add_edge(20,25,link_delay[44])
        substrate_graph.add_edge(20,21,link_delay[45])
        substrate_graph.add_edge(20,22,link_delay[46])
        substrate_graph.add_edge(22,23,link_delay[47])
        substrate_graph.add_edge(23,24,link_delay[48])
        substrate_graph.add_edge(24,25,link_delay[49])
        substrate_graph.add_edge(25,37,link_delay[50])
        substrate_graph.add_edge(25,40,link_delay[51])
        substrate_graph.add_edge(25,41,link_delay[52])
        substrate_graph.add_edge(25,53,link_delay[53])
        substrate_graph.add_edge(25,63,link_delay[54])
        substrate_graph.add_edge(25,61,link_delay[55])
        substrate_graph.add_edge(25,31,link_delay[56])
        substrate_graph.add_edge(26,64,link_delay[57])
        substrate_graph.add_edge(26,58,link_delay[58])
        substrate_graph.add_edge(26,53,link_delay[59])
        substrate_graph.add_edge(26,31,link_delay[60])
        substrate_graph.add_edge(27,72,link_delay[61])
        substrate_graph.add_edge(27,41,link_delay[62])
        substrate_graph.add_edge(27,47,link_delay[63])
        substrate_graph.add_edge(27,28,link_delay[64])
        substrate_graph.add_edge(28,33,link_delay[65])
        substrate_graph.add_edge(28,42,link_delay[66])
        substrate_graph.add_edge(29,63,link_delay[67])
        substrate_graph.add_edge(30,51,link_delay[68])
        substrate_graph.add_edge(31,64,link_delay[69])
        substrate_graph.add_edge(32,61,link_delay[70])
        substrate_graph.add_edge(32,68,link_delay[71])
        substrate_graph.add_edge(32,45,link_delay[72])
        substrate_graph.add_edge(32,47,link_delay[73])
        substrate_graph.add_edge(33,41,link_delay[74])
        substrate_graph.add_edge(34,72,link_delay[75])
        substrate_graph.add_edge(35,49,link_delay[76])
        substrate_graph.add_edge(35,36,link_delay[77])
        substrate_graph.add_edge(36,63,link_delay[78])
        substrate_graph.add_edge(37,41,link_delay[79])
        substrate_graph.add_edge(38,49,link_delay[80])
        substrate_graph.add_edge(40,41,link_delay[81])
        substrate_graph.add_edge(41,42,link_delay[82])
        substrate_graph.add_edge(41,58,link_delay[83])
        substrate_graph.add_edge(41,61,link_delay[84])
        substrate_graph.add_edge(43,46,link_delay[85])
        substrate_graph.add_edge(43,47,link_delay[86])
        substrate_graph.add_edge(44,61,link_delay[87])
        substrate_graph.add_edge(45,48,link_delay[88])
        substrate_graph.add_edge(45,47,link_delay[89])
        substrate_graph.add_edge(46,61,link_delay[90])
        substrate_graph.add_edge(47,72,link_delay[91])
        substrate_graph.add_edge(47,48,link_delay[92])
        substrate_graph.add_edge(47,61,link_delay[93])
        substrate_graph.add_edge(47,63,link_delay[94])
        substrate_graph.add_edge(49,63,link_delay[95])
        substrate_graph.add_edge(51,58,link_delay[96])
        substrate_graph.add_edge(54,60,link_delay[97])
        substrate_graph.add_edge(54,61,link_delay[98])
        substrate_graph.add_edge(55,66,link_delay[99])
        substrate_graph.add_edge(55,68,link_delay[100])
        substrate_graph.add_edge(56,57,link_delay[101])
        substrate_graph.add_edge(58,59,link_delay[102])
        substrate_graph.add_edge(58,60,link_delay[103])
        substrate_graph.add_edge(58,61,link_delay[104])
        substrate_graph.add_edge(59,60,link_delay[105])
        substrate_graph.add_edge(60,61,link_delay[106])
        substrate_graph.add_edge(61,66,link_delay[107])
        substrate_graph.add_edge(61,73,link_delay[108])
        substrate_graph.add_edge(62,64,link_delay[109])
        substrate_graph.add_edge(66,75,link_delay[110])
        substrate_graph.add_edge(66,67,link_delay[111])
        substrate_graph.add_edge(68,69,link_delay[112])
        substrate_graph.add_edge(68,70,link_delay[113])
        substrate_graph.add_edge(68,71,link_delay[114])
        substrate_graph.add_edge(69,70,link_delay[115])
        substrate_graph.add_edge(70,71,link_delay[116])
        substrate_graph.add_edge(73,75,link_delay[117])

    elif net==5:#OTE
        
        V_Comp=[2,3,5,8,10,12,14,15,17,18,20,21,22,24,26,29,31,36,39,40,41,45,46,49,52,54,56,58,60,61,62,67,69,70,72,73,74,76,77,78,80,83,85,86,87,88,91]
        VComp_num=len(V_Comp)#47
        VNF_num=10
        Max_time=450
        N_V=93
        N_E=106
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="OTE_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="OTE_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="OTE_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="OTE_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="OTE_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="OTE_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #N_E=106
        
        link_delay=numpy.zeros(N_E)
        link_delays_file="OTE_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # OTE Network:
        #N_V=93
        
        substrate_graph=GraphUndirectedWeighted(N_V)
        
        substrate_graph.add_edge(0,1,link_delay[0])
        substrate_graph.add_edge(1,56,link_delay[1])
        substrate_graph.add_edge(2,73,link_delay[2])
        substrate_graph.add_edge(2,3,link_delay[3])
        substrate_graph.add_edge(2,5,link_delay[4])
        substrate_graph.add_edge(3,4,link_delay[5])
        substrate_graph.add_edge(4,49,link_delay[6])
        substrate_graph.add_edge(4,17,link_delay[7])
        substrate_graph.add_edge(4,5,link_delay[8])
        substrate_graph.add_edge(4,79,link_delay[9])
        substrate_graph.add_edge(6,7,link_delay[10])
        substrate_graph.add_edge(10,56,link_delay[11])
        substrate_graph.add_edge(11,16,link_delay[12])
        substrate_graph.add_edge(12,72,link_delay[13])
        substrate_graph.add_edge(13,56,link_delay[14])
        substrate_graph.add_edge(14,17,link_delay[15])
        substrate_graph.add_edge(14,15,link_delay[16])
        substrate_graph.add_edge(15,17,link_delay[17])
        substrate_graph.add_edge(15,51,link_delay[18])
        substrate_graph.add_edge(16,34,link_delay[19])
        substrate_graph.add_edge(16,55,link_delay[20])
        substrate_graph.add_edge(18,35,link_delay[21])
        substrate_graph.add_edge(18,28,link_delay[22])
        substrate_graph.add_edge(18,77,link_delay[23])
        substrate_graph.add_edge(19,57,link_delay[24])
        substrate_graph.add_edge(19,47,link_delay[25])
        substrate_graph.add_edge(19,47,link_delay[26])
        substrate_graph.add_edge(20,24,link_delay[27])
        substrate_graph.add_edge(20,21,link_delay[28])
        substrate_graph.add_edge(20,22,link_delay[29])
        substrate_graph.add_edge(21,26,link_delay[30])
        substrate_graph.add_edge(22,84,link_delay[31])
        substrate_graph.add_edge(22,23,link_delay[32])
        substrate_graph.add_edge(23,27,link_delay[33])
        substrate_graph.add_edge(24,25,link_delay[34])
        substrate_graph.add_edge(25,56,link_delay[35])
        substrate_graph.add_edge(25,56,link_delay[36])
        substrate_graph.add_edge(25,27,link_delay[37])
        substrate_graph.add_edge(26,88,link_delay[38])
        substrate_graph.add_edge(28,39,link_delay[39])
        substrate_graph.add_edge(28,40,link_delay[40])
        substrate_graph.add_edge(28,85,link_delay[41])
        substrate_graph.add_edge(28,29,link_delay[42])
        substrate_graph.add_edge(28,30,link_delay[43])
        substrate_graph.add_edge(28,63,link_delay[44])
        substrate_graph.add_edge(29,78,link_delay[45])
        substrate_graph.add_edge(31,64,link_delay[46])
        substrate_graph.add_edge(31,65,link_delay[47])
        substrate_graph.add_edge(31,66,link_delay[48])
        substrate_graph.add_edge(31,68,link_delay[49])
        substrate_graph.add_edge(31,63,link_delay[50])
        substrate_graph.add_edge(32,57,link_delay[51])
        substrate_graph.add_edge(33,65,link_delay[52])
        substrate_graph.add_edge(33,42,link_delay[53])
        substrate_graph.add_edge(33,57,link_delay[54])
        substrate_graph.add_edge(36,37,link_delay[55])
        substrate_graph.add_edge(37,77,link_delay[56])
        substrate_graph.add_edge(40,64,link_delay[57])
        substrate_graph.add_edge(41,42,link_delay[58])
        substrate_graph.add_edge(41,59,link_delay[59])
        substrate_graph.add_edge(41,62,link_delay[60])
        substrate_graph.add_edge(42,60,link_delay[61])
        substrate_graph.add_edge(43,48,link_delay[62])
        substrate_graph.add_edge(43,55,link_delay[63])
        substrate_graph.add_edge(44,50,link_delay[64])
        substrate_graph.add_edge(44,46,link_delay[65])
        substrate_graph.add_edge(44,55,link_delay[66])
        substrate_graph.add_edge(45,46,link_delay[67])
        substrate_graph.add_edge(46,51,link_delay[68])
        substrate_graph.add_edge(47,58,link_delay[69])
        substrate_graph.add_edge(47,58,link_delay[70])
        substrate_graph.add_edge(49,50,link_delay[71])
        substrate_graph.add_edge(51,52,link_delay[72])
        substrate_graph.add_edge(51,55,link_delay[73])
        substrate_graph.add_edge(53,71,link_delay[74])
        substrate_graph.add_edge(54,67,link_delay[75])
        substrate_graph.add_edge(54,61,link_delay[76])
        substrate_graph.add_edge(55,56,link_delay[77])
        substrate_graph.add_edge(55,58,link_delay[78])
        substrate_graph.add_edge(56,58,link_delay[79])
        substrate_graph.add_edge(57,67,link_delay[80])
        substrate_graph.add_edge(57,58,link_delay[81])
        substrate_graph.add_edge(57,59,link_delay[82])
        substrate_graph.add_edge(57,61,link_delay[83])
        substrate_graph.add_edge(67,70,link_delay[84])
        substrate_graph.add_edge(69,72,link_delay[85])
        substrate_graph.add_edge(73,74,link_delay[86])
        substrate_graph.add_edge(74,80,link_delay[87])
        substrate_graph.add_edge(75,81,link_delay[88])
        substrate_graph.add_edge(75,90,link_delay[89])
        substrate_graph.add_edge(76,90,link_delay[90])
        substrate_graph.add_edge(76,82,link_delay[91])
        substrate_graph.add_edge(77,78,link_delay[92])
        substrate_graph.add_edge(79,80,link_delay[93])
        substrate_graph.add_edge(80,81,link_delay[94])
        substrate_graph.add_edge(80,82,link_delay[95])
        substrate_graph.add_edge(83,84,link_delay[96])
        substrate_graph.add_edge(83,87,link_delay[97])
        substrate_graph.add_edge(85,89,link_delay[98])
        substrate_graph.add_edge(85,86,link_delay[99])
        substrate_graph.add_edge(86,87,link_delay[100])
        substrate_graph.add_edge(87,90,link_delay[101])
        substrate_graph.add_edge(87,92,link_delay[102])
        substrate_graph.add_edge(88,89,link_delay[103])
        substrate_graph.add_edge(90,91,link_delay[104])
        substrate_graph.add_edge(91,92,link_delay[105])

    elif net==6:#ITCDeltacom
        
        V_Comp=[1,3,5,9,11,14,16,18,21,23,25,29,32,34,36,38,41,43,44,48,49,51,53,55,58,60,63,64,67,69,72,74,77,79,82,83,86,88,90,93,95,95,97,98,101,105,108,109,111,112]
        VComp_num=len(V_Comp)#50
        VNF_num=14
        Max_time=600
        N_V=113
        N_E=183
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="ITCDeltacom_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="ITCDeltacom_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="ITCDeltacom_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="ITCDeltacom_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="ITCDeltacom_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="ITCDeltacom_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #N_E=183
        
        link_delay=numpy.zeros(N_E)
        link_delays_file="ITCDeltacom_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # ITCDeltacom Network:
        #N_V=113
        
        substrate_graph=GraphUndirectedWeighted(N_V)
        
        substrate_graph.add_edge(0,64,link_delay[0])
        substrate_graph.add_edge(0,64,link_delay[1])
        substrate_graph.add_edge(0,1,link_delay[2])
        substrate_graph.add_edge(0,9,link_delay[3])
        substrate_graph.add_edge(0,8,link_delay[4])
        substrate_graph.add_edge(0,63,link_delay[5])
        substrate_graph.add_edge(0,63,link_delay[6])
        substrate_graph.add_edge(1,65,link_delay[7])
        substrate_graph.add_edge(2,55,link_delay[8])
        substrate_graph.add_edge(2,87,link_delay[9])
        substrate_graph.add_edge(3,88,link_delay[10])
        substrate_graph.add_edge(3,4,link_delay[11])
        substrate_graph.add_edge(3,4,link_delay[12])
        substrate_graph.add_edge(3,45,link_delay[13])
        substrate_graph.add_edge(3,86,link_delay[14])
        substrate_graph.add_edge(3,47,link_delay[15])
        substrate_graph.add_edge(4,86,link_delay[16])
        substrate_graph.add_edge(4,5,link_delay[17])
        substrate_graph.add_edge(4,6,link_delay[18])
        substrate_graph.add_edge(4,6,link_delay[19])
        substrate_graph.add_edge(4,7,link_delay[20])
        substrate_graph.add_edge(5,46,link_delay[21])
        substrate_graph.add_edge(6,80,link_delay[22])
        substrate_graph.add_edge(6,81,link_delay[23])
        substrate_graph.add_edge(6,62,link_delay[24])
        substrate_graph.add_edge(7,8,link_delay[25])
        substrate_graph.add_edge(8,86,link_delay[26])
        substrate_graph.add_edge(8,63,link_delay[27])
        substrate_graph.add_edge(8,63,link_delay[28])
        substrate_graph.add_edge(9,63,link_delay[29])
        substrate_graph.add_edge(10,16,link_delay[30])
        substrate_graph.add_edge(10,104,link_delay[31])
        substrate_graph.add_edge(10,11,link_delay[32])
        substrate_graph.add_edge(10,13,link_delay[33])
        substrate_graph.add_edge(11,16,link_delay[34])
        substrate_graph.add_edge(11,104,link_delay[35])
        substrate_graph.add_edge(11,13,link_delay[36])
        substrate_graph.add_edge(12,19,link_delay[37])
        substrate_graph.add_edge(12,13,link_delay[38])
        substrate_graph.add_edge(14,17,link_delay[39])
        substrate_graph.add_edge(14,84,link_delay[40])
        substrate_graph.add_edge(15,97,link_delay[41])
        substrate_graph.add_edge(15,47,link_delay[42])
        substrate_graph.add_edge(16,104,link_delay[43])
        substrate_graph.add_edge(17,43,link_delay[44])
        substrate_graph.add_edge(18,19,link_delay[45])
        substrate_graph.add_edge(18,35,link_delay[46])
        substrate_graph.add_edge(19,104,link_delay[47])
        substrate_graph.add_edge(19,36,link_delay[48])
        substrate_graph.add_edge(19,37,link_delay[49])
        substrate_graph.add_edge(19,37,link_delay[50])
        substrate_graph.add_edge(20,21,link_delay[51])
        substrate_graph.add_edge(20,22,link_delay[52])
        substrate_graph.add_edge(20,23,link_delay[53])
        substrate_graph.add_edge(21,26,link_delay[54])
        substrate_graph.add_edge(22,83,link_delay[55])
        substrate_graph.add_edge(23,105,link_delay[56])
        substrate_graph.add_edge(24,25,link_delay[57])
        substrate_graph.add_edge(24,27,link_delay[58])
        substrate_graph.add_edge(24,95,link_delay[59])
        substrate_graph.add_edge(25,89,link_delay[60])
        substrate_graph.add_edge(25,26,link_delay[61])
        substrate_graph.add_edge(25,28,link_delay[62])
        substrate_graph.add_edge(25,92,link_delay[63])
        substrate_graph.add_edge(27,83,link_delay[64])
        substrate_graph.add_edge(28,29,link_delay[65])
        substrate_graph.add_edge(29,92,link_delay[66])
        substrate_graph.add_edge(30,103,link_delay[67])
        substrate_graph.add_edge(30,36,link_delay[68])
        substrate_graph.add_edge(30,36,link_delay[69])
        substrate_graph.add_edge(30,77,link_delay[70])
        substrate_graph.add_edge(30,31,link_delay[71])
        substrate_graph.add_edge(31,112,link_delay[72])
        substrate_graph.add_edge(31,36,link_delay[73])
        substrate_graph.add_edge(31,37,link_delay[74])
        substrate_graph.add_edge(32,33,link_delay[75])
        substrate_graph.add_edge(32,34,link_delay[76])
        substrate_graph.add_edge(33,38,link_delay[77])
        substrate_graph.add_edge(34,35,link_delay[78])
        substrate_graph.add_edge(36,37,link_delay[79])
        substrate_graph.add_edge(36,37,link_delay[80])
        substrate_graph.add_edge(38,39,link_delay[81])
        substrate_graph.add_edge(40,41,link_delay[82])
        substrate_graph.add_edge(40,49,link_delay[83])
        substrate_graph.add_edge(41,42,link_delay[84])
        substrate_graph.add_edge(42,43,link_delay[85])
        substrate_graph.add_edge(43,45,link_delay[86])
        substrate_graph.add_edge(44,47,link_delay[87])
        substrate_graph.add_edge(46,47,link_delay[88])
        substrate_graph.add_edge(47,73,link_delay[89])
        substrate_graph.add_edge(47,51,link_delay[90])
        substrate_graph.add_edge(47,84,link_delay[91])
        substrate_graph.add_edge(47,111,link_delay[92])
        substrate_graph.add_edge(47,60,link_delay[93])
        substrate_graph.add_edge(47,60,link_delay[94])
        substrate_graph.add_edge(48,57,link_delay[95])
        substrate_graph.add_edge(48,49,link_delay[96])
        substrate_graph.add_edge(49,84,link_delay[97])
        substrate_graph.add_edge(49,54,link_delay[98])
        substrate_graph.add_edge(50,57,link_delay[99])
        substrate_graph.add_edge(50,91,link_delay[100])
        substrate_graph.add_edge(50,52,link_delay[101])
        substrate_graph.add_edge(50,51,link_delay[102])
        substrate_graph.add_edge(52,53,link_delay[103])
        substrate_graph.add_edge(53,59,link_delay[104])
        substrate_graph.add_edge(53,60,link_delay[105])
        substrate_graph.add_edge(54,56,link_delay[106])
        substrate_graph.add_edge(54,90,link_delay[107])
        substrate_graph.add_edge(54,111,link_delay[108])
        substrate_graph.add_edge(54,55,link_delay[109])
        substrate_graph.add_edge(55,94,link_delay[110])
        substrate_graph.add_edge(55,111,link_delay[111])
        substrate_graph.add_edge(56,57,link_delay[112])
        substrate_graph.add_edge(58,105,link_delay[113])
        substrate_graph.add_edge(58,61,link_delay[114])
        substrate_graph.add_edge(58,110,link_delay[115])
        substrate_graph.add_edge(59,60,link_delay[116])
        substrate_graph.add_edge(60,104,link_delay[117])
        substrate_graph.add_edge(60,104,link_delay[118])
        substrate_graph.add_edge(60,104,link_delay[119])
        substrate_graph.add_edge(60,97,link_delay[120])
        substrate_graph.add_edge(61,82,link_delay[121])
        substrate_graph.add_edge(62,80,link_delay[122])
        substrate_graph.add_edge(62,70,link_delay[123])
        substrate_graph.add_edge(62,85,link_delay[124])
        substrate_graph.add_edge(63,85,link_delay[125])
        substrate_graph.add_edge(63,70,link_delay[126])
        substrate_graph.add_edge(64,65,link_delay[127])
        substrate_graph.add_edge(64,66,link_delay[128])
        substrate_graph.add_edge(64,66,link_delay[129])
        substrate_graph.add_edge(64,67,link_delay[130])
        substrate_graph.add_edge(66,67,link_delay[131])
        substrate_graph.add_edge(66,69,link_delay[132])
        substrate_graph.add_edge(66,85,link_delay[133])
        substrate_graph.add_edge(68,69,link_delay[134])
        substrate_graph.add_edge(68,71,link_delay[135])
        substrate_graph.add_edge(70,71,link_delay[136])
        substrate_graph.add_edge(72,73,link_delay[137])
        substrate_graph.add_edge(72,75,link_delay[138])
        substrate_graph.add_edge(72,75,link_delay[139])
        substrate_graph.add_edge(72,75,link_delay[140])
        substrate_graph.add_edge(72,81,link_delay[141])
        substrate_graph.add_edge(72,81,link_delay[142])
        substrate_graph.add_edge(72,81,link_delay[143])
        substrate_graph.add_edge(73,98,link_delay[144])
        substrate_graph.add_edge(74,112,link_delay[145])
        substrate_graph.add_edge(74,75,link_delay[146])
        substrate_graph.add_edge(74,103,link_delay[147])
        substrate_graph.add_edge(75,104,link_delay[148])
        substrate_graph.add_edge(75,104,link_delay[149])
        substrate_graph.add_edge(75,76,link_delay[150])
        substrate_graph.add_edge(76,100,link_delay[151])
        substrate_graph.add_edge(77,81,link_delay[152])
        substrate_graph.add_edge(77,81,link_delay[153])
        substrate_graph.add_edge(77,81,link_delay[154])
        substrate_graph.add_edge(77,81,link_delay[155])
        substrate_graph.add_edge(77,100,link_delay[156])
        substrate_graph.add_edge(77,103,link_delay[157])
        substrate_graph.add_edge(78,101,link_delay[158])
        substrate_graph.add_edge(79,102,link_delay[159])
        substrate_graph.add_edge(79,102,link_delay[160])
        substrate_graph.add_edge(81,101,link_delay[161])
        substrate_graph.add_edge(82,83,link_delay[162])
        substrate_graph.add_edge(87,88,link_delay[163])
        substrate_graph.add_edge(88,93,link_delay[164])
        substrate_graph.add_edge(89,96,link_delay[165])
        substrate_graph.add_edge(89,90,link_delay[166])
        substrate_graph.add_edge(91,92,link_delay[167])
        substrate_graph.add_edge(93,94,link_delay[168])
        substrate_graph.add_edge(94,95,link_delay[169])
        substrate_graph.add_edge(95,96,link_delay[170])
        substrate_graph.add_edge(97,98,link_delay[171])
        substrate_graph.add_edge(98,99,link_delay[172])
        substrate_graph.add_edge(99,104,link_delay[173])
        substrate_graph.add_edge(99,112,link_delay[174])
        substrate_graph.add_edge(100,102,link_delay[175])
        substrate_graph.add_edge(101,102,link_delay[176])
        substrate_graph.add_edge(105,106,link_delay[177])
        substrate_graph.add_edge(106,107,link_delay[178])
        substrate_graph.add_edge(107,108,link_delay[179])
        substrate_graph.add_edge(108,109,link_delay[180])
        substrate_graph.add_edge(108,109,link_delay[181])
        substrate_graph.add_edge(109,110,link_delay[182])
        
    elif net==7:#ION
        
        V_Comp=[2,3,5,8,10,12,14,15,17,18,20,21,22,24,26,29,31,36,39,40,41,45,46,49,52,54,56,58,60,61,62,67,69,70,72,73,74,76,77,78,80,83,85,86,87,88,91,98,103,109,114,117,124]
        VComp_num=len(V_Comp)#53
        VNF_num=14
        Max_time=600
        N_V=125
        N_E=150
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="Ion_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="Ion_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="Ion_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="Ion_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="Ion_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="Ion_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #N_E=150
        
        #Reading link_delay from file:
        link_delay=numpy.zeros(N_E)
        link_delays_file="Ion_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # ION Network:
        #N_V=125
        substrate_graph=GraphUndirectedWeighted(N_V)
        substrate_graph.add_edge(0, 25,link_delay[0])
        substrate_graph.add_edge(0, 9,link_delay[1])
        substrate_graph.add_edge(1, 114,link_delay[2])
        substrate_graph.add_edge(1, 70,link_delay[3])
        substrate_graph.add_edge(2, 99,link_delay[4])
        substrate_graph.add_edge(2, 3,link_delay[5])
        substrate_graph.add_edge(3, 4,link_delay[6])
        substrate_graph.add_edge(3, 5,link_delay[7])
        substrate_graph.add_edge(3, 6,link_delay[8])
        substrate_graph.add_edge(3, 6,link_delay[9])
        substrate_graph.add_edge(3, 7,link_delay[10])
        substrate_graph.add_edge(5, 103,link_delay[11])
        substrate_graph.add_edge(8, 100,link_delay[12])
        substrate_graph.add_edge(8, 92,link_delay[13])
        substrate_graph.add_edge(9, 64,link_delay[14])
        substrate_graph.add_edge(10, 58,link_delay[15])
        substrate_graph.add_edge(10, 11,link_delay[16])
        substrate_graph.add_edge(11, 18,link_delay[17])
        substrate_graph.add_edge(12, 19,link_delay[18])
        substrate_graph.add_edge(13, 18,link_delay[19])
        substrate_graph.add_edge(13, 19,link_delay[20])
        substrate_graph.add_edge(14, 17,link_delay[21])
        substrate_graph.add_edge(14, 111,link_delay[22])
        substrate_graph.add_edge(15, 114,link_delay[23])
        substrate_graph.add_edge(15, 111,link_delay[24])
        substrate_graph.add_edge(16, 112,link_delay[25])
        substrate_graph.add_edge(16, 17,link_delay[26])
        substrate_graph.add_edge(18, 39,link_delay[27])
        substrate_graph.add_edge(19, 59,link_delay[28])
        substrate_graph.add_edge(20, 64,link_delay[29])
        substrate_graph.add_edge(20, 36,link_delay[30])
        substrate_graph.add_edge(21, 80,link_delay[31])
        substrate_graph.add_edge(21, 54,link_delay[32])
        substrate_graph.add_edge(21, 79,link_delay[33])
        substrate_graph.add_edge(22, 80,link_delay[34])
        substrate_graph.add_edge(22, 54,link_delay[35])
        substrate_graph.add_edge(22, 79,link_delay[36])
        substrate_graph.add_edge(23, 26,link_delay[37])
        substrate_graph.add_edge(23, 27,link_delay[38])
        substrate_graph.add_edge(24, 35,link_delay[39])
        substrate_graph.add_edge(24, 35,link_delay[40])
        substrate_graph.add_edge(24, 36,link_delay[41])
        substrate_graph.add_edge(25, 28,link_delay[42])
        substrate_graph.add_edge(26, 107,link_delay[43])
        substrate_graph.add_edge(26, 87,link_delay[44])
        substrate_graph.add_edge(27, 28,link_delay[45])
        substrate_graph.add_edge(28, 88,link_delay[46])
        substrate_graph.add_edge(29, 32,link_delay[47])
        substrate_graph.add_edge(29, 33,link_delay[48])
        substrate_graph.add_edge(29, 101,link_delay[49])
        substrate_graph.add_edge(29, 105,link_delay[50])
        substrate_graph.add_edge(29, 106,link_delay[51])
        substrate_graph.add_edge(29, 30,link_delay[52])
        substrate_graph.add_edge(30, 31,link_delay[53])
        substrate_graph.add_edge(31, 32,link_delay[54])
        substrate_graph.add_edge(33, 34,link_delay[55])
        substrate_graph.add_edge(34, 104,link_delay[56])
        substrate_graph.add_edge(34, 103,link_delay[57])
        substrate_graph.add_edge(35, 42,link_delay[58])
        substrate_graph.add_edge(37, 40,link_delay[59])
        substrate_graph.add_edge(37, 38,link_delay[60])
        substrate_graph.add_edge(38, 43,link_delay[61])
        substrate_graph.add_edge(39, 40,link_delay[62])
        substrate_graph.add_edge(41, 42,link_delay[63])
        substrate_graph.add_edge(41, 44,link_delay[64])
        substrate_graph.add_edge(43, 44,link_delay[65])
        substrate_graph.add_edge(44, 116,link_delay[66])
        substrate_graph.add_edge(45, 93,link_delay[67])
        substrate_graph.add_edge(45, 54,link_delay[68])
        substrate_graph.add_edge(46, 93,link_delay[69])
        substrate_graph.add_edge(46, 47,link_delay[70])
        substrate_graph.add_edge(47, 48,link_delay[71])
        substrate_graph.add_edge(48, 49,link_delay[72])
        substrate_graph.add_edge(48, 123,link_delay[73])
        substrate_graph.add_edge(48, 78,link_delay[74])
        substrate_graph.add_edge(49, 109,link_delay[75])
        substrate_graph.add_edge(50, 76,link_delay[76])
        substrate_graph.add_edge(51, 76,link_delay[77])
        substrate_graph.add_edge(51, 52,link_delay[78])
        substrate_graph.add_edge(52, 109,link_delay[79])
        substrate_graph.add_edge(53, 123,link_delay[80])
        substrate_graph.add_edge(55, 56,link_delay[81])
        substrate_graph.add_edge(55, 62,link_delay[82])
        substrate_graph.add_edge(56, 57,link_delay[83])
        substrate_graph.add_edge(57, 97,link_delay[84])
        substrate_graph.add_edge(58, 97,link_delay[85])
        substrate_graph.add_edge(58, 92,link_delay[86])
        substrate_graph.add_edge(59, 124,link_delay[87])
        substrate_graph.add_edge(59, 61,link_delay[88])
        substrate_graph.add_edge(60, 124,link_delay[89])
        substrate_graph.add_edge(60, 124,link_delay[90])
        substrate_graph.add_edge(60, 109,link_delay[91])
        substrate_graph.add_edge(61, 98,link_delay[92])
        substrate_graph.add_edge(62, 98,link_delay[93])
        substrate_graph.add_edge(63, 96,link_delay[94])
        substrate_graph.add_edge(63, 66,link_delay[95])
        substrate_graph.add_edge(64, 116,link_delay[96])
        substrate_graph.add_edge(64, 65,link_delay[97])
        substrate_graph.add_edge(65, 111,link_delay[98])
        substrate_graph.add_edge(66, 87,link_delay[99])
        substrate_graph.add_edge(67, 74,link_delay[100])
        substrate_graph.add_edge(67, 68,link_delay[101])
        substrate_graph.add_edge(67, 86,link_delay[102])
        substrate_graph.add_edge(68, 95,link_delay[103])
        substrate_graph.add_edge(69, 117,link_delay[104])
        substrate_graph.add_edge(69, 70,link_delay[105])
        substrate_graph.add_edge(71, 74,link_delay[106])
        substrate_graph.add_edge(72, 74,link_delay[107])
        substrate_graph.add_edge(72, 117,link_delay[108])
        substrate_graph.add_edge(73, 124,link_delay[109])
        substrate_graph.add_edge(73, 110,link_delay[110])
        substrate_graph.add_edge(74, 112,link_delay[111])
        substrate_graph.add_edge(74, 110,link_delay[112])
        substrate_graph.add_edge(75, 76,link_delay[113])
        substrate_graph.add_edge(75, 95,link_delay[114])
        substrate_graph.add_edge(76, 110,link_delay[115])
        substrate_graph.add_edge(77, 80,link_delay[116])
        substrate_graph.add_edge(77, 78,link_delay[117])
        substrate_graph.add_edge(79, 82,link_delay[118])
        substrate_graph.add_edge(81, 82,link_delay[119])
        substrate_graph.add_edge(81, 94,link_delay[120])
        substrate_graph.add_edge(83, 86,link_delay[121])
        substrate_graph.add_edge(83, 94,link_delay[122])
        substrate_graph.add_edge(84, 94,link_delay[123])
        substrate_graph.add_edge(85, 95,link_delay[124])
        substrate_graph.add_edge(88, 91,link_delay[125])
        substrate_graph.add_edge(89, 90,link_delay[126])
        substrate_graph.add_edge(89, 115,link_delay[127])
        substrate_graph.add_edge(89, 122,link_delay[128])
        substrate_graph.add_edge(90, 96,link_delay[129])
        substrate_graph.add_edge(91, 120,link_delay[130])
        substrate_graph.add_edge(93, 123,link_delay[131])
        substrate_graph.add_edge(96, 121,link_delay[132])
        substrate_graph.add_edge(99, 105,link_delay[133])
        substrate_graph.add_edge(100, 105,link_delay[134])
        substrate_graph.add_edge(100, 107,link_delay[135])
        substrate_graph.add_edge(101, 106,link_delay[136])
        substrate_graph.add_edge(102, 103,link_delay[137])
        substrate_graph.add_edge(102, 103,link_delay[138])
        substrate_graph.add_edge(106, 108,link_delay[139])
        substrate_graph.add_edge(107, 108,link_delay[140])
        substrate_graph.add_edge(111, 113,link_delay[141])
        substrate_graph.add_edge(112, 113,link_delay[142])
        substrate_graph.add_edge(113, 114,link_delay[143])
        substrate_graph.add_edge(115, 117,link_delay[144])
        substrate_graph.add_edge(117, 118,link_delay[145])
        substrate_graph.add_edge(118, 119,link_delay[146])
        substrate_graph.add_edge(119, 120,link_delay[147])
        substrate_graph.add_edge(120, 121,link_delay[148])
        substrate_graph.add_edge(121, 122,link_delay[149])
        
    elif net==8:#ColtTelecom
        V_Comp=[2,3,5,8,10,12,14,15,17,18,20,21,22,24,26,29,31,36,39,40,41,45,46,49,52,54,56,58,60,61,62,67,69,70,72,73,74,76,77,78,80,83,85,86,87,88,91,98,103,109,114,117,124,129,133,136,139,143,147]
        VComp_num=len(V_Comp)#59
        VNF_num=15
        Max_time=800
        N_V=153
        N_E=191
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="ColtTelecom_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="ColtTelecom_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="ColtTelecom_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="ColtTelecom_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="ColtTelecom_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="ColtTelecom_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #N_E=191
        
        #Reading link_delay from file:
        link_delay=numpy.zeros(N_E)
        link_delays_file="ColtTelecom_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # ColtTelecom Network:
        #N_V=153
        substrate_graph=GraphUndirectedWeighted(N_V)
        
        substrate_graph.add_edge(0,1,link_delay[0])
        substrate_graph.add_edge(0,10,link_delay[1])
        substrate_graph.add_edge(0,99,link_delay[2])
        substrate_graph.add_edge(0,99,link_delay[3])
        substrate_graph.add_edge(2,144,link_delay[4])
        substrate_graph.add_edge(2,51,link_delay[5])
        substrate_graph.add_edge(3,144,link_delay[6])
        substrate_graph.add_edge(3,144,link_delay[7])
        substrate_graph.add_edge(4,8,link_delay[8])
        substrate_graph.add_edge(4,5,link_delay[9])
        substrate_graph.add_edge(5,144,link_delay[10])
        substrate_graph.add_edge(5,11,link_delay[11])
        substrate_graph.add_edge(6,11,link_delay[12])
        substrate_graph.add_edge(6,7,link_delay[13])
        substrate_graph.add_edge(7,144,link_delay[14])
        substrate_graph.add_edge(8,13,link_delay[15])
        substrate_graph.add_edge(9,13,link_delay[16])
        substrate_graph.add_edge(9,13,link_delay[17])
        substrate_graph.add_edge(10,97,link_delay[18])
        substrate_graph.add_edge(10,97,link_delay[19])
        substrate_graph.add_edge(10,98,link_delay[20])
        substrate_graph.add_edge(10,98,link_delay[21])
        substrate_graph.add_edge(10,101,link_delay[22])
        substrate_graph.add_edge(10,11,link_delay[23])
        substrate_graph.add_edge(10,13,link_delay[24])
        substrate_graph.add_edge(12,141,link_delay[25])
        substrate_graph.add_edge(12,30,link_delay[26])
        substrate_graph.add_edge(13,119,link_delay[27])
        substrate_graph.add_edge(14,17,link_delay[28])
        substrate_graph.add_edge(14,141,link_delay[29])
        substrate_graph.add_edge(15,18,link_delay[30])
        substrate_graph.add_edge(15,19,link_delay[31])
        substrate_graph.add_edge(15,132,link_delay[32])
        substrate_graph.add_edge(16,51,link_delay[33])
        substrate_graph.add_edge(16,60,link_delay[34])
        substrate_graph.add_edge(17,136,link_delay[35])
        substrate_graph.add_edge(17,143,link_delay[36])
        substrate_graph.add_edge(17,133,link_delay[37])
        substrate_graph.add_edge(17,133,link_delay[38])
        substrate_graph.add_edge(17,134,link_delay[39])
        substrate_graph.add_edge(18,142,link_delay[40])
        substrate_graph.add_edge(19,49,link_delay[41])
        substrate_graph.add_edge(20,23,link_delay[42])
        substrate_graph.add_edge(21,81,link_delay[43])
        substrate_graph.add_edge(22,23,link_delay[44])
        substrate_graph.add_edge(23,151,link_delay[45])
        substrate_graph.add_edge(23,151,link_delay[46])
        substrate_graph.add_edge(24,81,link_delay[47])
        substrate_graph.add_edge(25,81,link_delay[48])
        substrate_graph.add_edge(26,81,link_delay[49])
        substrate_graph.add_edge(27,81,link_delay[50])
        substrate_graph.add_edge(28,140,link_delay[51])
        substrate_graph.add_edge(28,29,link_delay[52])
        substrate_graph.add_edge(30,118,link_delay[53])
        substrate_graph.add_edge(30,119,link_delay[54])
        substrate_graph.add_edge(31,119,link_delay[55])
        substrate_graph.add_edge(31,119,link_delay[56])
        substrate_graph.add_edge(32,33,link_delay[57])
        substrate_graph.add_edge(32,35,link_delay[58])
        substrate_graph.add_edge(33,74,link_delay[59])
        substrate_graph.add_edge(33,38,link_delay[60])
        substrate_graph.add_edge(34,119,link_delay[61])
        substrate_graph.add_edge(34,119,link_delay[62])
        substrate_graph.add_edge(35,74,link_delay[63])
        substrate_graph.add_edge(36,73,link_delay[64])
        substrate_graph.add_edge(36,39,link_delay[65])
        substrate_graph.add_edge(37,73,link_delay[66])
        substrate_graph.add_edge(38,74,link_delay[67])
        substrate_graph.add_edge(39,124,link_delay[68])
        substrate_graph.add_edge(40,142,link_delay[69])
        substrate_graph.add_edge(41,142,link_delay[70])
        substrate_graph.add_edge(42,142,link_delay[71])
        substrate_graph.add_edge(43,142,link_delay[72])
        substrate_graph.add_edge(44,142,link_delay[73])
        substrate_graph.add_edge(45,49,link_delay[74])
        substrate_graph.add_edge(46,142,link_delay[75])
        substrate_graph.add_edge(47,142,link_delay[76])
        substrate_graph.add_edge(48,49,link_delay[77])
        substrate_graph.add_edge(49,129,link_delay[78])
        substrate_graph.add_edge(50,56,link_delay[79])
        substrate_graph.add_edge(50,58,link_delay[80])
        substrate_graph.add_edge(50,51,link_delay[81])
        substrate_graph.add_edge(50,52,link_delay[82])
        substrate_graph.add_edge(50,53,link_delay[83])
        substrate_graph.add_edge(51,136,link_delay[84])
        substrate_graph.add_edge(51,53,link_delay[85])
        substrate_graph.add_edge(51,92,link_delay[86])
        substrate_graph.add_edge(51,127,link_delay[87])
        substrate_graph.add_edge(51,127,link_delay[88])
        substrate_graph.add_edge(53,92,link_delay[89])
        substrate_graph.add_edge(54,139,link_delay[90])
        substrate_graph.add_edge(54,140,link_delay[91])
        substrate_graph.add_edge(54,55,link_delay[92])
        substrate_graph.add_edge(55,140,link_delay[93])
        substrate_graph.add_edge(56,57,link_delay[94])
        substrate_graph.add_edge(56,57,link_delay[95])
        substrate_graph.add_edge(56,59,link_delay[96])
        substrate_graph.add_edge(58,59,link_delay[97])
        substrate_graph.add_edge(60,128,link_delay[98])
        substrate_graph.add_edge(60,144,link_delay[99])
        substrate_graph.add_edge(61,81,link_delay[100])
        substrate_graph.add_edge(62,115,link_delay[101])
        substrate_graph.add_edge(62,140,link_delay[102])
        substrate_graph.add_edge(62,94,link_delay[103])
        substrate_graph.add_edge(63,125,link_delay[104])
        substrate_graph.add_edge(63,126,link_delay[105])
        substrate_graph.add_edge(64,72,link_delay[106])
        substrate_graph.add_edge(64,126,link_delay[107])
        substrate_graph.add_edge(65,152,link_delay[108])
        substrate_graph.add_edge(66,152,link_delay[109])
        substrate_graph.add_edge(66,68,link_delay[110])
        substrate_graph.add_edge(67,152,link_delay[111])
        substrate_graph.add_edge(68,81,link_delay[112])
        substrate_graph.add_edge(68,108,link_delay[113])
        substrate_graph.add_edge(69,152,link_delay[114])
        substrate_graph.add_edge(70,152,link_delay[115])
        substrate_graph.add_edge(71,152,link_delay[116])
        substrate_graph.add_edge(72,152,link_delay[117])
        substrate_graph.add_edge(73,120,link_delay[118])
        substrate_graph.add_edge(73,117,link_delay[119])
        substrate_graph.add_edge(74,117,link_delay[120])
        substrate_graph.add_edge(74,125,link_delay[121])
        substrate_graph.add_edge(75,140,link_delay[122])
        substrate_graph.add_edge(75,150,link_delay[123])
        substrate_graph.add_edge(76,140,link_delay[124])
        substrate_graph.add_edge(76,77,link_delay[125])
        substrate_graph.add_edge(77,150,link_delay[126])
        substrate_graph.add_edge(78,115,link_delay[127])
        substrate_graph.add_edge(78,142,link_delay[128])
        substrate_graph.add_edge(78,94,link_delay[129])
        substrate_graph.add_edge(79,137,link_delay[130])
        substrate_graph.add_edge(79,122,link_delay[131])
        substrate_graph.add_edge(79,84,link_delay[132])
        substrate_graph.add_edge(80,137,link_delay[133])
        substrate_graph.add_edge(80,151,link_delay[134])
        substrate_graph.add_edge(81,107,link_delay[135])
        substrate_graph.add_edge(81,93,link_delay[136])
        substrate_graph.add_edge(82,83,link_delay[137])
        substrate_graph.add_edge(82,138,link_delay[138])
        substrate_graph.add_edge(82,123,link_delay[139])
        substrate_graph.add_edge(82,84,link_delay[140])
        substrate_graph.add_edge(85,123,link_delay[141])
        substrate_graph.add_edge(86,121,link_delay[142])
        substrate_graph.add_edge(86,122,link_delay[143])
        substrate_graph.add_edge(86,151,link_delay[144])
        substrate_graph.add_edge(87,152,link_delay[145])
        substrate_graph.add_edge(88,152,link_delay[146])
        substrate_graph.add_edge(89,152,link_delay[147])
        substrate_graph.add_edge(90,138,link_delay[148])
        substrate_graph.add_edge(91,140,link_delay[149])
        substrate_graph.add_edge(91,150,link_delay[150])
        substrate_graph.add_edge(95,107,link_delay[151])
        substrate_graph.add_edge(96,152,link_delay[152])
        substrate_graph.add_edge(97,100,link_delay[153])
        substrate_graph.add_edge(97,100,link_delay[154])
        substrate_graph.add_edge(98,101,link_delay[155])
        substrate_graph.add_edge(99,102,link_delay[156])
        substrate_graph.add_edge(99,102,link_delay[157])
        substrate_graph.add_edge(101,104,link_delay[158])
        substrate_graph.add_edge(101,104,link_delay[159])
        substrate_graph.add_edge(103,152,link_delay[160])
        substrate_graph.add_edge(105,106,link_delay[161])
        substrate_graph.add_edge(105,108,link_delay[162])
        substrate_graph.add_edge(106,152,link_delay[163])
        substrate_graph.add_edge(107,111,link_delay[164])
        substrate_graph.add_edge(109,112,link_delay[165])
        substrate_graph.add_edge(109,152,link_delay[166])
        substrate_graph.add_edge(110,152,link_delay[167])
        substrate_graph.add_edge(111,112,link_delay[168])
        substrate_graph.add_edge(113,152,link_delay[169])
        substrate_graph.add_edge(114,152,link_delay[170])
        substrate_graph.add_edge(115,139,link_delay[171])
        substrate_graph.add_edge(116,142,link_delay[172])
        substrate_graph.add_edge(117,118,link_delay[173])
        substrate_graph.add_edge(118,139,link_delay[174])
        substrate_graph.add_edge(121,148,link_delay[175])
        substrate_graph.add_edge(123,145,link_delay[176])
        substrate_graph.add_edge(123,139,link_delay[177])
        substrate_graph.add_edge(123,124,link_delay[178])
        substrate_graph.add_edge(129,131,link_delay[179])
        substrate_graph.add_edge(130,143,link_delay[180])
        substrate_graph.add_edge(131,143,link_delay[181])
        substrate_graph.add_edge(132,143,link_delay[182])
        substrate_graph.add_edge(134,135,link_delay[183])
        substrate_graph.add_edge(135,136,link_delay[184])
        substrate_graph.add_edge(138,152,link_delay[185])
        substrate_graph.add_edge(139,146,link_delay[186])
        substrate_graph.add_edge(139,149,link_delay[187])
        substrate_graph.add_edge(140,142,link_delay[188])
        substrate_graph.add_edge(146,147,link_delay[189])
        substrate_graph.add_edge(148,149,link_delay[190])

    elif net==9:#Cogent
        V_Comp=[2,3,5,8,10,12,14,15,17,18,20,21,22,24,26,29,31,36,39,40,41,45,46,49,52,54,56,58,60,61,62,67,69,70,72,73,74,76,77,78,80,83,85,86,87,88,91,98,103,109,114,117,124,129,133,136,139,143,147,152,157,160,164,169,173,177,181,185,189,194]
        VComp_num=len(V_Comp)#70
        VNF_num=17
        Max_time=1000
        N_V=197
        N_E=245
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="Cogent_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="Cogent_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="Cogent_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="Cogent_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="Cogent_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="Cogent_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        #N_E=245
        
        #Reading link_delay from file:
        link_delay=numpy.zeros(N_E)
        link_delays_file="Cogent_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # Cogent Network:
        #N_V=197
        substrate_graph=GraphUndirectedWeighted(N_V)
        
        substrate_graph.add_edge(0,176,link_delay[0])
        substrate_graph.add_edge(0,9,link_delay[1])
        substrate_graph.add_edge(1,8,link_delay[2])
        substrate_graph.add_edge(1,176,link_delay[3])
        substrate_graph.add_edge(1,114,link_delay[4])
        substrate_graph.add_edge(1,116,link_delay[5])
        substrate_graph.add_edge(1,175,link_delay[6])
        substrate_graph.add_edge(2,76,link_delay[7])
        substrate_graph.add_edge(2,77,link_delay[8])
        substrate_graph.add_edge(3,4,link_delay[9])
        substrate_graph.add_edge(3,77,link_delay[10])
        substrate_graph.add_edge(4,6,link_delay[11])
        substrate_graph.add_edge(4,135,link_delay[12])
        substrate_graph.add_edge(5,131,link_delay[13])
        substrate_graph.add_edge(5,6,link_delay[14])
        substrate_graph.add_edge(6,7,link_delay[15])
        substrate_graph.add_edge(7,8,link_delay[16])
        substrate_graph.add_edge(7,174,link_delay[17])
        substrate_graph.add_edge(8,194,link_delay[18])
        substrate_graph.add_edge(8,9,link_delay[19])
        substrate_graph.add_edge(8,191,link_delay[20])
        substrate_graph.add_edge(10,11,link_delay[21])
        substrate_graph.add_edge(10,13,link_delay[22])
        substrate_graph.add_edge(11,16,link_delay[23])
        substrate_graph.add_edge(12,32,link_delay[24])
        substrate_graph.add_edge(12,13,link_delay[25])
        substrate_graph.add_edge(12,30,link_delay[26])
        substrate_graph.add_edge(13,16,link_delay[27])
        substrate_graph.add_edge(13,15,link_delay[28])
        substrate_graph.add_edge(14,64,link_delay[29])
        substrate_graph.add_edge(14,129,link_delay[30])
        substrate_graph.add_edge(14,15,link_delay[31])
        substrate_graph.add_edge(16,17,link_delay[32])
        substrate_graph.add_edge(18,19,link_delay[33])
        substrate_graph.add_edge(18,30,link_delay[34])
        substrate_graph.add_edge(19,89,link_delay[35])
        substrate_graph.add_edge(19,68,link_delay[36])
        substrate_graph.add_edge(19,82,link_delay[37])
        substrate_graph.add_edge(20,21,link_delay[38])
        substrate_graph.add_edge(20,23,link_delay[39])
        substrate_graph.add_edge(21,26,link_delay[40])
        substrate_graph.add_edge(22,188,link_delay[41])
        substrate_graph.add_edge(22,23,link_delay[42])
        substrate_graph.add_edge(24,27,link_delay[43])
        substrate_graph.add_edge(25,171,link_delay[44])
        substrate_graph.add_edge(25,55,link_delay[45])
        substrate_graph.add_edge(26,27,link_delay[46])
        substrate_graph.add_edge(26,28,link_delay[47])
        substrate_graph.add_edge(26,29,link_delay[48])
        substrate_graph.add_edge(28,51,link_delay[49])
        substrate_graph.add_edge(28,54,link_delay[50])
        substrate_graph.add_edge(29,78,link_delay[51])
        substrate_graph.add_edge(30,35,link_delay[52])
        substrate_graph.add_edge(31,37,link_delay[53])
        substrate_graph.add_edge(32,33,link_delay[54])
        substrate_graph.add_edge(32,37,link_delay[55])
        substrate_graph.add_edge(34,37,link_delay[56])
        substrate_graph.add_edge(35,37,link_delay[57])
        substrate_graph.add_edge(36,38,link_delay[58])
        substrate_graph.add_edge(36,39,link_delay[59])
        substrate_graph.add_edge(37,160,link_delay[60])
        substrate_graph.add_edge(37,38,link_delay[61])
        substrate_graph.add_edge(38,196,link_delay[62])
        substrate_graph.add_edge(39,181,link_delay[63])
        substrate_graph.add_edge(40,41,link_delay[64])
        substrate_graph.add_edge(40,42,link_delay[65])
        substrate_graph.add_edge(41,43,link_delay[66])
        substrate_graph.add_edge(41,189,link_delay[67])
        substrate_graph.add_edge(42,43,link_delay[68])
        substrate_graph.add_edge(42,143,link_delay[69])
        substrate_graph.add_edge(42,143,link_delay[70])
        substrate_graph.add_edge(44,45,link_delay[71])
        substrate_graph.add_edge(44,47,link_delay[72])
        substrate_graph.add_edge(45,48,link_delay[73])
        substrate_graph.add_edge(45,164,link_delay[74])
        substrate_graph.add_edge(46,49,link_delay[75])
        substrate_graph.add_edge(46,47,link_delay[76])
        substrate_graph.add_edge(48,155,link_delay[77])
        substrate_graph.add_edge(48,181,link_delay[78])
        substrate_graph.add_edge(49,177,link_delay[79])
        substrate_graph.add_edge(49,147,link_delay[80])
        substrate_graph.add_edge(49,165,link_delay[81])
        substrate_graph.add_edge(50,57,link_delay[82])
        substrate_graph.add_edge(50,51,link_delay[83])
        substrate_graph.add_edge(51,188,link_delay[84])
        substrate_graph.add_edge(52,53,link_delay[85])
        substrate_graph.add_edge(52,55,link_delay[86])
        substrate_graph.add_edge(53,58,link_delay[87])
        substrate_graph.add_edge(54,55,link_delay[88])
        substrate_graph.add_edge(56,57,link_delay[89])
        substrate_graph.add_edge(56,59,link_delay[90])
        substrate_graph.add_edge(58,59,link_delay[91])
        substrate_graph.add_edge(60,61,link_delay[92])
        substrate_graph.add_edge(60,69,link_delay[93])
        substrate_graph.add_edge(61,128,link_delay[94])
        substrate_graph.add_edge(61,122,link_delay[95])
        substrate_graph.add_edge(62,144,link_delay[96])
        substrate_graph.add_edge(62,86,link_delay[97])
        substrate_graph.add_edge(62,63,link_delay[98])
        substrate_graph.add_edge(63,68,link_delay[99])
        substrate_graph.add_edge(63,149,link_delay[100])
        substrate_graph.add_edge(64,65,link_delay[101])
        substrate_graph.add_edge(64,67,link_delay[102])
        substrate_graph.add_edge(64,68,link_delay[103])
        substrate_graph.add_edge(65,66,link_delay[104])
        substrate_graph.add_edge(66,67,link_delay[105])
        substrate_graph.add_edge(67,69,link_delay[106])
        substrate_graph.add_edge(69,144,link_delay[107])
        substrate_graph.add_edge(70,79,link_delay[108])
        substrate_graph.add_edge(70,183,link_delay[109])
        substrate_graph.add_edge(71,72,link_delay[110])
        substrate_graph.add_edge(71,79,link_delay[111])
        substrate_graph.add_edge(72,73,link_delay[112])
        substrate_graph.add_edge(73,74,link_delay[113])
        substrate_graph.add_edge(74,183,link_delay[114])
        substrate_graph.add_edge(75,173,link_delay[115])
        substrate_graph.add_edge(75,183,link_delay[116])
        substrate_graph.add_edge(76,173,link_delay[117])
        substrate_graph.add_edge(77,152,link_delay[118])
        substrate_graph.add_edge(77,162,link_delay[119])
        substrate_graph.add_edge(77,133,link_delay[120])
        substrate_graph.add_edge(78,94,link_delay[121])
        substrate_graph.add_edge(78,79,link_delay[122])
        substrate_graph.add_edge(80,81,link_delay[123])
        substrate_graph.add_edge(80,81,link_delay[124])
        substrate_graph.add_edge(80,86,link_delay[125])
        substrate_graph.add_edge(80,87,link_delay[126])
        substrate_graph.add_edge(82,88,link_delay[127])
        substrate_graph.add_edge(82,83,link_delay[128])
        substrate_graph.add_edge(82,150,link_delay[129])
        substrate_graph.add_edge(83,148,link_delay[130])
        substrate_graph.add_edge(84,148,link_delay[131])
        substrate_graph.add_edge(84,85,link_delay[132])
        substrate_graph.add_edge(86,87,link_delay[133])
        substrate_graph.add_edge(87,88,link_delay[134])
        substrate_graph.add_edge(89,150,link_delay[135])
        substrate_graph.add_edge(90,172,link_delay[136])
        substrate_graph.add_edge(91,99,link_delay[137])
        substrate_graph.add_edge(91,92,link_delay[138])
        substrate_graph.add_edge(92,96,link_delay[139])
        substrate_graph.add_edge(92,93,link_delay[140])
        substrate_graph.add_edge(92,183,link_delay[141])
        substrate_graph.add_edge(94,171,link_delay[142])
        substrate_graph.add_edge(95,96,link_delay[143])
        substrate_graph.add_edge(95,171,link_delay[144])
        substrate_graph.add_edge(96,97,link_delay[145])
        substrate_graph.add_edge(97,172,link_delay[146])
        substrate_graph.add_edge(98,194,link_delay[147])
        substrate_graph.add_edge(98,131,link_delay[148])
        substrate_graph.add_edge(99,100,link_delay[149])
        substrate_graph.add_edge(100,132,link_delay[150])
        substrate_graph.add_edge(101,104,link_delay[151])
        substrate_graph.add_edge(101,180,link_delay[152])
        substrate_graph.add_edge(101,102,link_delay[153])
        substrate_graph.add_edge(102,109,link_delay[154])
        substrate_graph.add_edge(103,104,link_delay[155])
        substrate_graph.add_edge(103,106,link_delay[156])
        substrate_graph.add_edge(105,106,link_delay[157])
        substrate_graph.add_edge(105,107,link_delay[158])
        substrate_graph.add_edge(105,179,link_delay[159])
        substrate_graph.add_edge(107,108,link_delay[160])
        substrate_graph.add_edge(107,129,link_delay[161])
        substrate_graph.add_edge(108,179,link_delay[162])
        substrate_graph.add_edge(109,110,link_delay[163])
        substrate_graph.add_edge(110,128,link_delay[164])
        substrate_graph.add_edge(111,112,link_delay[165])
        substrate_graph.add_edge(111,140,link_delay[166])
        substrate_graph.add_edge(112,137,link_delay[167])
        substrate_graph.add_edge(113,114,link_delay[168])
        substrate_graph.add_edge(113,191,link_delay[169])
        substrate_graph.add_edge(115,116,link_delay[170])
        substrate_graph.add_edge(115,118,link_delay[171])
        substrate_graph.add_edge(117,120,link_delay[172])
        substrate_graph.add_edge(117,118,link_delay[173])
        substrate_graph.add_edge(119,176,link_delay[174])
        substrate_graph.add_edge(119,175,link_delay[175])
        substrate_graph.add_edge(120,175,link_delay[176])
        substrate_graph.add_edge(121,122,link_delay[177])
        substrate_graph.add_edge(121,124,link_delay[178])
        substrate_graph.add_edge(123,124,link_delay[179])
        substrate_graph.add_edge(123,125,link_delay[180])
        substrate_graph.add_edge(123,126,link_delay[181])
        substrate_graph.add_edge(127,128,link_delay[182])
        substrate_graph.add_edge(127,130,link_delay[183])
        substrate_graph.add_edge(129,130,link_delay[184])
        substrate_graph.add_edge(131,142,link_delay[185])
        substrate_graph.add_edge(132,135,link_delay[186])
        substrate_graph.add_edge(133,173,link_delay[187])
        substrate_graph.add_edge(134,137,link_delay[188])
        substrate_graph.add_edge(134,138,link_delay[189])
        substrate_graph.add_edge(134,135,link_delay[190])
        substrate_graph.add_edge(136,139,link_delay[191])
        substrate_graph.add_edge(137,172,link_delay[192])
        substrate_graph.add_edge(138,174,link_delay[193])
        substrate_graph.add_edge(138,141,link_delay[194])
        substrate_graph.add_edge(139,174,link_delay[195])
        substrate_graph.add_edge(140,141,link_delay[196])
        substrate_graph.add_edge(142,143,link_delay[197])
        substrate_graph.add_edge(143,185,link_delay[198])
        substrate_graph.add_edge(144,149,link_delay[199])
        substrate_graph.add_edge(145,157,link_delay[200])
        substrate_graph.add_edge(146,152,link_delay[201])
        substrate_graph.add_edge(146,154,link_delay[202])
        substrate_graph.add_edge(147,166,link_delay[203])
        substrate_graph.add_edge(147,177,link_delay[204])
        substrate_graph.add_edge(148,154,link_delay[205])
        substrate_graph.add_edge(149,150,link_delay[206])
        substrate_graph.add_edge(151,152,link_delay[207])
        substrate_graph.add_edge(152,153,link_delay[208])
        substrate_graph.add_edge(153,160,link_delay[209])
        substrate_graph.add_edge(153,154,link_delay[210])
        substrate_graph.add_edge(154,159,link_delay[211])
        substrate_graph.add_edge(154,183,link_delay[212])
        substrate_graph.add_edge(155,195,link_delay[213])
        substrate_graph.add_edge(155,156,link_delay[214])
        substrate_graph.add_edge(155,165,link_delay[215])
        substrate_graph.add_edge(156,157,link_delay[216])
        substrate_graph.add_edge(157,158,link_delay[217])
        substrate_graph.add_edge(158,183,link_delay[218])
        substrate_graph.add_edge(158,196,link_delay[219])
        substrate_graph.add_edge(158,165,link_delay[220])
        substrate_graph.add_edge(161,162,link_delay[221])
        substrate_graph.add_edge(162,163,link_delay[222])
        substrate_graph.add_edge(162,167,link_delay[223])
        substrate_graph.add_edge(163,187,link_delay[224])
        substrate_graph.add_edge(163,164,link_delay[225])
        substrate_graph.add_edge(165,177,link_delay[226])
        substrate_graph.add_edge(165,181,link_delay[227])
        substrate_graph.add_edge(165,184,link_delay[228])
        substrate_graph.add_edge(165,186,link_delay[229])
        substrate_graph.add_edge(166,170,link_delay[230])
        substrate_graph.add_edge(166,183,link_delay[231])
        substrate_graph.add_edge(167,168,link_delay[232])
        substrate_graph.add_edge(168,169,link_delay[233])
        substrate_graph.add_edge(169,185,link_delay[234])
        substrate_graph.add_edge(178,179,link_delay[235])
        substrate_graph.add_edge(181,196,link_delay[236])
        substrate_graph.add_edge(182,189,link_delay[237])
        substrate_graph.add_edge(183,184,link_delay[238])
        substrate_graph.add_edge(183,186,link_delay[239])
        substrate_graph.add_edge(186,187,link_delay[240])
        substrate_graph.add_edge(190,191,link_delay[241])
        substrate_graph.add_edge(192,193,link_delay[242])
        substrate_graph.add_edge(193,194,link_delay[243])
        substrate_graph.add_edge(195,196,link_delay[244])


        
    """elif net==8:#test
        V_Comp=[2,4,5,7]
        VComp_num=len(V_Comp)
        VNF_num=2
        Max_time=30
        
        #Defining VNF Parameters:
        Storage_VNF=numpy.zeros(VNF_num)
        Capacity_VNF=numpy.zeros(VNF_num)
        IO_VNF=numpy.zeros(VNF_num)
        
        VNF_storage_file="test_VNF_Stor.csv" 
        VNFStorageFile=open(VNF_storage_file, 'r')
        
        lines_stor_VNF=[]
        for line in VNFStorageFile:
            lines_stor_VNF.append(line)
            
        Storage_VNF=[]
        for line in lines_stor_VNF:
            Storage_VNF.append(float(line))
        
        VNFStorageFile.close()
        
        VNF_Capacity_file="test_VNF_Cap.csv" 
        VNFCapacityFile=open(VNF_Capacity_file, 'r')
        
        lines_cap_VNF=[]
        for line in VNFCapacityFile:
            lines_cap_VNF.append(line)
            
        Capacity_VNF=[]
        for line in lines_cap_VNF:
            Capacity_VNF.append(float(line))
        
        VNFCapacityFile.close()
        
        VNF_IO_file="test_VNF_IO.csv" 
        VNFIOFile=open(VNF_IO_file, 'r')
        
        lines_IO_VNF=[]
        for line in VNFIOFile:
            lines_IO_VNF.append(line)
            
        IO_VNF=[]
        for line in lines_IO_VNF:
            IO_VNF.append(float(line))
        
        VNFIOFile.close()
        
        #Defining Substrate Graph Parameters:
        Storage_AVLB=numpy.zeros(VComp_num)
        Capacity_AVLB=numpy.zeros(VComp_num)
        IO_AVLB=numpy.zeros(VComp_num)
        
        VComp_IO_file="test_VCOMP_IO.csv" 
        IOFile=open(VComp_IO_file, 'r')
        
        lines_IO_comp=[]
        for line in IOFile:
            lines_IO_comp.append(line)
            
        IO_AVLB=[]
        for line in lines_IO_comp:
            IO_AVLB.append(float(line))
        
        IOFile.close()
        
        VComp_Capacity_file="test_VCOMP_Cap.csv" 
        CapacityFile=open(VComp_Capacity_file, 'r')
        
        lines_cap_comp=[]
        for line in CapacityFile:
            lines_cap_comp.append(line)
            
        Capacity_AVLB=[]
        for line in lines_cap_comp:
            Capacity_AVLB.append(float(line))
        
        CapacityFile.close()
        
        VComp_storage_file="test_VCOMP_Stor.csv" 
        StorageFile=open(VComp_storage_file, 'r')
        
        lines_stor_comp=[]
        for line in StorageFile:
            lines_stor_comp.append(line)
            
        Storage_AVLB=[]
        for line in lines_stor_comp:
            Storage_AVLB.append(float(line))
        
        StorageFile.close()
        
        N_E=15
        
        #Reading link_delay from file:
        link_delay=numpy.zeros(N_E)
        link_delays_file="test_link_delays.csv"
        delayFile=open(link_delays_file, 'r')
        
        
        lines_del=[]
        for line in delayFile:
            lines_del.append(line)
            
        link_delay=[]
        for line in lines_del:
            link_delay.append(float(line))
        
        delayFile.close()
        
        # test Network:
        N_V=11
        substrate_graph=GraphUndirectedWeighted(N_V)
        
        substrate_graph.add_edge(0, 1,link_delay[0])
        substrate_graph.add_edge(0, 9,link_delay[1])
        substrate_graph.add_edge(1, 2,link_delay[2])
        substrate_graph.add_edge(1, 8,link_delay[3])
        substrate_graph.add_edge(2, 3,link_delay[4])
        substrate_graph.add_edge(2, 10,link_delay[5])
        substrate_graph.add_edge(3, 4,link_delay[6])
        substrate_graph.add_edge(4, 5,link_delay[7])
        substrate_graph.add_edge(4, 6,link_delay[8])
        substrate_graph.add_edge(4, 10,link_delay[9])
        substrate_graph.add_edge(5, 6,link_delay[10])
        substrate_graph.add_edge(6, 7,link_delay[11])
        substrate_graph.add_edge(6, 8,link_delay[12])
        substrate_graph.add_edge(6, 9,link_delay[13])
        substrate_graph.add_edge(9, 10,link_delay[14])"""
        
    return Max_time,substrate_graph,N_V,N_E,V_Comp,VComp_num,VNF_num,link_delay,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF