# -*- coding: utf-8 -*-
"""
Created on Tue OCT. 06 12:46:20 2020

@author: Marzi
"""

import numpy
from dijkstra import dijkstra

def check_validity(Positions,V_Comp,VNF_num,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF):
    
    VComp_num=len(V_Comp)

    S_Comp_Usage=numpy.zeros(VComp_num)
    C_Comp_Usage=numpy.zeros(VComp_num)
    IO_Comp_Usage=numpy.zeros(VComp_num)
    S_violation=numpy.zeros(VComp_num)
    C_violation=numpy.zeros(VComp_num)
    IO_violation=numpy.zeros(VComp_num)
    sum_violation=0
    
    for i in range(0,VComp_num):
        for j in range(0,len(Positions)):
            if V_Comp[i]==Positions[j]:
                S_Comp_Usage[i]=S_Comp_Usage[i]+Storage_VNF[j]
                C_Comp_Usage[i]=C_Comp_Usage[i]+Capacity_VNF[j]
                IO_Comp_Usage[i]=IO_Comp_Usage[i]+IO_VNF[j]
        if S_Comp_Usage[i]>Storage_AVLB[i]:
            S_violation[i]=1
        if C_Comp_Usage[i]>Capacity_AVLB[i]:
            C_violation[i]=1
        if IO_Comp_Usage[i]>IO_AVLB[i]:
            IO_violation[i]=1
    for i in range(0,VComp_num):
        sum_violation=sum_violation+S_violation[i]+C_violation[i]+IO_violation[i]
    
    if sum_violation>0:
        return False,S_Comp_Usage,C_Comp_Usage,IO_Comp_Usage
    else:
        return True,S_Comp_Usage,C_Comp_Usage,IO_Comp_Usage

def check_validity_old(Positions,V_Comp,VNF_num,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF):
    
    VComp_num=len(V_Comp)

    S_Comp_Usage=numpy.zeros(VComp_num)
    C_Comp_Usage=numpy.zeros(VComp_num)
    IO_Comp_Usage=numpy.zeros(VComp_num)
    S_violation=numpy.zeros(VComp_num)
    C_violation=numpy.zeros(VComp_num)
    IO_violation=numpy.zeros(VComp_num)
    sum_violation=0
    
    for i in range(0,VComp_num):
        for j in range(0,VNF_num):
            if V_Comp[i]==Positions[j]:
                S_Comp_Usage[i]=S_Comp_Usage[i]+Storage_VNF[j]
                C_Comp_Usage[i]=C_Comp_Usage[i]+Capacity_VNF[j]
                IO_Comp_Usage[i]=IO_Comp_Usage[i]+IO_VNF[j]
        if S_Comp_Usage[i]>Storage_AVLB[i]:
            S_violation[i]=1
        if C_Comp_Usage[i]>Capacity_AVLB[i]:
            C_violation[i]=1
        if IO_Comp_Usage[i]>IO_AVLB[i]:
            IO_violation[i]=1
    for i in range(0,VComp_num):
        sum_violation=sum_violation+S_violation[i]+C_violation[i]+IO_violation[i]
        
    if sum_violation>0:
        return False
    else:
        return True


def F_CRO(N_V,graph,sourceNode,destinationNode,Positions):
    shortest_path=[]
    distance=0
    #print("in F1:",Positions, sourceNode,destinationNode)
    #shortest_path, distance = CRO(N_V,graph, sourceNode, Positions[0])
    #print("in F1:",shortest_path, distance)
    for i in range(1,len(Positions)):
        shortest_path_temp, distance_temp = CRO(N_V,graph, Positions[i-1], Positions[i])
        shortest_path.append(shortest_path_temp)
        distance = distance + distance_temp
    #shortest_path_temp2, distance_temp2 = CRO(N_V,graph, Positions[len(Positions)-1], destinationNode)
    #shortest_path.append(shortest_path_temp2)
    #distance = distance + distance_temp2
    return shortest_path, distance

def F_dijkstragraph(N_V,graph,sourceNode,destinationNode,Positions):
    #print("in F1:",Positions, sourceNode,destinationNode)
    shortest_path, distance = dijkstra(graph, sourceNode, Positions[0])
    #print("in F1:",shortest_path, distance)
    for i in range(1,len(Positions)):
        shortest_path_temp, distance_temp = dijkstra(graph, Positions[i-1], Positions[i])
        shortest_path.append(shortest_path_temp)
        distance = distance + distance_temp
    shortest_path_temp2, distance_temp2 = dijkstra(graph, Positions[len(Positions)-1], destinationNode)
    shortest_path.append(shortest_path_temp2)
    distance = distance + distance_temp2
    return shortest_path, distance

def quantizer(Positions,dim,Position_Nodes,ub,lb):
    
    q_Positions=numpy.empty((1,dim))

    for t in range(0,dim):
        for q in range(0,len(Position_Nodes)):
            if (q*(ub-lb)/len(Position_Nodes)<=Positions[t] and (q+1)*(ub-lb)/len(Position_Nodes)>Positions[t]):
                q_Positions[0,t]=Position_Nodes[q]
            elif (Positions[t]==ub-lb):
                q_Positions[0,t]=Position_Nodes[dim-1]
                
    return q_Positions