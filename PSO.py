# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:37:00 2016

@author: Hossam Faris
"""

import random
import numpy
#import math
from colorama import Fore, Back, Style
from solution import solution
import time
from benchmarks import quantizer
from benchmarks import check_validity



def PSO(objf,lb,ub,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF):

    # PSO parameters
    
#    dim=30
#    iters=200
    Vmax=4000
#    PopSize=50     #population size
    wMax=0.5
    wMin=0.2
    c1=2
    c2=2
#    lb=-10
#    ub=10
#    
    s=solution()
    
    
    ######################## Initializations
    
    vel=numpy.zeros((SearchAgents_no,dim))
    vel_up=numpy.zeros((SearchAgents_no,dim))
    
    pBestScore=numpy.zeros(SearchAgents_no) 
    pBestScore.fill(float("inf"))
    
    pBest=numpy.empty((SearchAgents_no,dim))
    q_pBest=numpy.empty((SearchAgents_no,dim))
    
    gBest=numpy.zeros(dim)
    gBestScore=float("inf")
    q_gBest=numpy.zeros(dim)
    
    
    #Initialize the positions of search agents
    Positions=numpy.empty((SearchAgents_no,dim))
    q_Positions=numpy.empty((SearchAgents_no,dim))
    q_Positions_upd=numpy.empty((SearchAgents_no,dim))
    Positions_upd=numpy.empty((SearchAgents_no,dim))
    
    k=0
    isvalid=True
    while k<SearchAgents_no:
        Positions[k,:]=(ub-lb)*numpy.random.random(dim)
        q_Positions[k,:]=quantizer(Positions[k,:],dim,Position_Nodes,ub,lb)
        isvalid,temp1,temp2,temp3=check_validity(q_Positions[k,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
        if isvalid:
            k=k+1
    
    #print("q_Positions:",q_Positions)
            
    Convergence_curve=[]
    s=solution()
    
    ############################################
    print("PSO is optimizing  \""+objf.__name__+"\"")    
    
    timerStart=time.time() 
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    
    # Main loop
    timerStart=time.time()
    timer2=time.time()
    time_interval=timer2-timerStart
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    
    Max_iter=1
    l=0

    while l < Max_iter:
        fitness=[]
        for i in range(0,SearchAgents_no):
            #pos[i,:]=checkBounds(pos[i,:],lb,ub)
            Positions[i,:]=numpy.clip(Positions[i,:], lb, ub)
            q_Positions[i,:]=quantizer(Positions[i,:],dim,Position_Nodes,ub,lb)
            isvalid,temp1,temp2,temp3=check_validity(q_Positions[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
            #print("q_Positions[",i,"]:",q_Positions[i,:])
            #print(isvalid)
            while (isvalid==False):
                #print("clip not valid")
                Positions[i,:]=(ub-lb)*numpy.random.random(dim)
                q_Positions[i,:]=quantizer(Positions[i,:],dim,Position_Nodes,ub,lb)
                isvalid,temp1,temp2,temp3=check_validity(q_Positions[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                    
            #print(isvalid)
            #print("q_Positions[",i,"]:",q_Positions[i,:])
            #Calculate objective function for each particle
            path, fitnes=objf(N_V,graph,q_Positions[i,0],q_Positions[i,dim-1],q_Positions[i,:])
            fitness.append(fitnes)  
            
            if(pBestScore[i]>fitness[i]):
                pBestScore[i]=fitness[i]
                #print("pBestScore[",i,"];",pBestScore[i])
                pBest[i,:]=Positions[i,:].copy()
                q_pBest[i,:]=q_Positions[i,:].copy()

            if(gBestScore>fitness[i]):
                gBestScore=fitness[i]
                #print("gBestScore",gBestScore)
                gBest=Positions[i,:].copy()
                q_gBest=q_Positions[i,:].copy()
                gBestPath=path.copy()

        #Update the W of PSO
        timer2=time.time()
        time_interval2=timer2-timerStart
        w=wMax-time_interval2*((wMax-wMin)/Max_time);
        
        i=0
        notvalid=0
        while i<SearchAgents_no:
            for j in range (0,dim):
                r1=random.random()
                r2=random.random()
                vel_up[i,j]=w*vel[i,j]+c1*r1*(pBest[i,j]-Positions[i,j])+c2*r2*(gBest[j]-Positions[i,j])
                #print("vel_up[",i,",",j,"]:",vel_up[i,j])
                if(vel_up[i,j]>Vmax):
                    vel_up[i,j]=Vmax
                
                if(vel_up[i,j]<-Vmax):
                    vel_up[i,j]=-Vmax
                
                #print("vel_up[",i,",",j,"]:",vel_up[i,j])
                Positions_upd[i,j]=Positions[i,j]+vel_up[i,j]
                
            #print("Positions[",i,"]:",Positions[i,:])
            #print("Positions_upd[",i,"]:",Positions_upd[i,:])
            q_Positions_upd[i,:]=quantizer(Positions_upd[i,:],dim,Position_Nodes,ub,lb)
            isvalid,temp1,temp2,temp3=check_validity(q_Positions_upd[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
            #print("q_Positions_upd[",i,"]:",q_Positions_upd[i,:])
            if isvalid:
                #print("new Pos is valid")
                #print("q_Positions_upd[",i,"]:",q_Positions_upd[i,:])
                Positions[i,:]=Positions_upd[i,:]
                vel[i,:]=vel_up[i,:]
                i=i+1
            else:
                notvalid=notvalid+1
                if (notvalid>25):
                    notvalid=0
                    i=i+1
        
        Convergence_curve.append(gBestScore)
        timer2=time.time() 
        time_interval=timer2-timerStart
        if time_interval<=Max_time:
            Max_iter=Max_iter+1
        l=l+1
        #print("l:",l)
        
    used_Pos=numpy.zeros(len(Position_Nodes))
    used_Comp_Nodes=0
    
    for i in range(0,len(Position_Nodes)):
        for j in range(0,len(q_gBest)):
            if q_gBest[j]==Position_Nodes[i]:
                used_Pos[i]=1
    
    for i in range(0,len(Position_Nodes)):
        used_Comp_Nodes=used_Comp_Nodes+used_Pos[i]
    
    timerEnd=time.time()
    s.pos=q_gBest
    s.path=gBestPath
    s.delay=gBestScore
    s.Energy=used_Comp_Nodes
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=Convergence_curve
    s.optimizer="PSO"
    s.objfname=objf.__name__
    
    return s
         
    
