# -*- coding: utf-8 -*-
"""
Created on Mon May 16 00:27:50 2016

"""

import random
import numpy
#import math
from solution import solution
import time
from benchmarks import check_validity
from ARP import ARP
from dijkstra import dijkstra


    

def IEGWO(objf,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF):
        
    # initialize alpha, beta, and delta_pos
    Alpha_pos=numpy.zeros(dim)
    Alpha_score=float("inf")
    
    Beta_pos=numpy.zeros(dim)
    Beta_score=float("inf")
    
    Delta_pos=numpy.zeros(dim)
    Delta_score=float("inf")
    
    fitness=numpy.zeros(SearchAgents_no)
    PG=numpy.zeros(len(Position_Nodes))
    Delay=numpy.zeros(len(Position_Nodes))
    Delay2=numpy.zeros(len(Position_Nodes))
    prob=numpy.zeros(len(Position_Nodes))
    eps=0.005
    D_Proc=0.0001
    
    for i in range (0,len(Position_Nodes)):
        PG[i]=1/len(Position_Nodes)
        
    #Initialize the positions of search agents
    #Positions=numpy.random.uniform(0,1,(SearchAgents_no,dim)) *(ub-lb)+lb
    Positions=numpy.empty((SearchAgents_no,dim))
    Positions_upd=numpy.empty((SearchAgents_no,dim))

    ind=numpy.random.randint(0,len(Position_Nodes),(SearchAgents_no,dim))
    k=0
    isvalid=True
    while k<ind.shape[0]:
        for t in range(0,ind.shape[1]):
            Positions[k,t]=Position_Nodes[ind[k,t]]
        isvalid,temp1,temp2,temp3=check_validity(Positions[k,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
        if isvalid:
            k=k+1
        else:
            ind[k,:]=numpy.random.randint(0,len(Position_Nodes),(1,dim))
                
    Convergence_curve=[]
    s=solution()

     # Loop counter
    print("IEGWO is optimizing  \""+objf.__name__+"\"")    
    
    timerStart=time.time() 
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")

    # Main loop
    Max_iter=1
    l=0
    while l < Max_iter:
        for i in range(0,SearchAgents_no):
            # Return back the search agents that go beyond the boundaries of the search space
            path, fitness[i]=objf(N_V,graph,Positions[i,0],Positions[i,dim-1],Positions[i,:])
            
            # Update Alpha, Beta, and Delta
            if fitness[i]<Alpha_score :
                
                Delta_score=Beta_score # Update delta
                Delta_pos=Beta_pos.copy()
                
                Beta_score=Alpha_score  # Update beta
                Beta_pos=Alpha_pos.copy()
                
                Alpha_score=fitness[i]; # Update alpha
                Alpha_pos=Positions[i,:].copy()

                for j in range (0,dim):
                    for k in range (0,len(Position_Nodes)):
                        if Alpha_pos[j]==Position_Nodes[k]:
                            PG[k]=PG[k]+eps
                            break
                PG_temp=PG.copy()
                for k in range(0,len(PG)):
                    PG[k]=PG_temp[k]/sum(PG_temp)
                
                Alpha_path=path.copy()
        
            
            if (fitness[i]>Alpha_score and fitness[i]<Beta_score ):
                
                Delta_score=Beta_score # Update delta
                Delta_pos=Beta_pos.copy()
                
                Beta_score=fitness[i]  # Update beta
                Beta_pos=Positions[i,:].copy()                
            
            if (fitness[i]>Alpha_score and fitness[i]>Beta_score and fitness[i]<Delta_score): 
                Delta_score=fitness[i] # Update delta
                Delta_pos=Positions[i,:].copy()
                
        #defining the probability of assigning each wolf's position to this VNFk
        P_alpha=0.35
        P_beta=0.3
        P_delta=0.2
        
        # Update the Position of search agents including omegas
        for i in range (0,SearchAgents_no):
            Wolf_Role=ARP(l, Max_iter, Alpha_score, fitness[i]) # 1: exploitation, 0: explration
            
            if Wolf_Role==1: # exploitation
                for j in range (0,dim):
                    isvalid=False
                    P_alpha_t=P_alpha
                    P_beta_t=P_beta
                    P_delta_t=P_delta
                    cntin=1
                    while (isvalid==False)&(cntin==1):
                        Positions_upd[i,:]=Positions[i,:].copy()
                        r1=random.random() # r1 is a random number in [0,1]
                        if (r1>=0 and r1<P_alpha_t):
                            Positions_upd[i,j]=Alpha_pos[j]
                            isvalid,temp1,temp2,temp3=check_validity(Positions_upd[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                            if isvalid:
                                Positions[i,j]=Positions_upd[i,j]
                            else:
                                P_alpha_t=0
                                
                        elif (r1>=P_alpha_t and r1<P_alpha_t+P_beta_t):
                            Positions_upd[i,j]=Beta_pos[j]
                            isvalid,temp1,temp2,temp3=check_validity(Positions_upd[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                            if isvalid:
                                Positions[i,j]=Positions_upd[i,j]
                            else:
                                P_beta_t=0
                                
                        elif (r1>=P_alpha_t+P_beta_t and r1<P_alpha_t+P_beta_t+P_delta_t):
                            Positions_upd[i,j]=Delta_pos[j]
                            isvalid,temp1,temp2,temp3=check_validity(Positions_upd[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                            if isvalid:
                                Positions[i,j]=Positions_upd[i,j]
                            else:
                                P_delta_t=0
                                
                        else:
                            isvalid=False
                            if j==0:                               
                                for k in range(0,len(Position_Nodes)):
                                    prob[k]=1/len(Position_Nodes)
                            else:
                                sum_of_rev_del=0
                                for k in range(0,len(Position_Nodes)):
                                    path, Delay2[k]=dijkstra(graph,Positions[i,j-1],Position_Nodes[k])
                                    Delay[k]=Delay2[k]+D_Proc
                                    sum_of_rev_del=sum_of_rev_del+1/Delay[k]
                                    
                                for k in range(0,len(Position_Nodes)):
                                    prob[k]=(1/Delay[k])/sum_of_rev_del
                            
                            r2=random.random()
                            t=1
                            while (isvalid==False)&(sum(prob)>0)&(t<len(prob)-1):
                                Positions_upd[i,:]=Positions[i,:].copy()
                                if r2<prob[0]:
                                    Positions_upd[i,j]=Position_Nodes[0]
                                    isvalid,temp1,temp2,temp3=check_validity(Positions_upd[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                                    if isvalid==False:
                                        prob[0]=0
                                else:
                                    for t in range(1,len(prob)):
                                        if (r2>=sum(prob[0:t])) & (r2<sum(prob[0:t+1])):
                                            Positions_upd[i,j]=Position_Nodes[t]
                                            isvalid,temp1,temp2,temp3=check_validity(Positions_upd[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                                            if isvalid:
                                                break
                                            else:
                                                prob[t]=0
                            if isvalid:
                                Positions[i,j]=Positions_upd[i,j]
                            elif (P_alpha_t+P_beta_t+P_delta_t==0):
                                cntin=0
                                    
            else: # exploration
                for j in range(0,dim):
                    isvalid=False
                    k=1
                    while (isvalid==False)&(sum(PG)>0)&(k<len(PG)-1):
                        Positions_upd[i,:]=Positions[i,:].copy()
                        r2=random.random()
                        if r2<PG[0]:
                            Positions_upd[i,j]=Position_Nodes[0]
                        else:
                            for k in range(1,len(PG)):
                                if (r2>=sum(PG[0:k])) and (r2<sum(PG[0:k+1])):
                                    Positions_upd[i,j]=Position_Nodes[k]
                                    isvalid,temp1,temp2,temp3=check_validity(Positions_upd[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                                    if isvalid:
                                        break
                                    else:
                                        PG[t]=0
                        if isvalid:
                            Positions[i,j]=Positions_upd[i,j]                    
        
        Convergence_curve.append(Alpha_score)
        
        timer2=time.time()
        time_interval=timer2-timerStart
        if time_interval<=Max_time:
            Max_iter=Max_iter+1
        l=l+1

    timerEnd=time.time()
    
    used_Pos=numpy.zeros(len(Position_Nodes))
    used_Comp_Nodes=0
    
    for i in range(0,len(Position_Nodes)):
        for j in range(0,len(Alpha_pos)):
            if Alpha_pos[j]==Position_Nodes[i]:
                used_Pos[i]=1
    
    for i in range(0,len(Position_Nodes)):
        used_Comp_Nodes=used_Comp_Nodes+used_Pos[i]
    
    s.pos=Alpha_pos
    s.path=Alpha_path
    s.delay=Alpha_score
    s.Energy=used_Comp_Nodes
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=Convergence_curve
    s.optimizer="IEGWO"
    s.objfname=objf.__name__
    
    
    return s
    

