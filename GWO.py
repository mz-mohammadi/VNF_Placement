# -*- coding: utf-8 -*-
"""
Created on DEC 2021

@author: Marzi
"""

import random
import numpy
#import math
from solution import solution
import time
from benchmarks import quantizer
from benchmarks import check_validity


def GWO(objf,lb,ub,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF):

    #Max_iter=1000
    #lb=-100 #lower bound
    #ub=100  #upper bound
    #dim=30  #dimention of solutions alfa, beta, ...
    #SearchAgents_no=5
    
    # initialize alpha, beta, and delta_pos
    Alpha_pos=numpy.zeros(dim)
    Alpha_score=float("inf")
    
    Beta_pos=numpy.zeros(dim)
    Beta_score=float("inf")
    
    Delta_pos=numpy.zeros(dim)
    Delta_score=float("inf")
    
    #Initialize the positions of search agents
    #Positions=numpy.random.uniform(0,1,(SearchAgents_no,dim)) *(ub-lb)+lb
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
        else:
            Positions[k,:]=(ub-lb)*numpy.random.random(dim)
    
    #print("Positions:",Positions)
    #print("q_Positions:",q_Positions)

    Convergence_curve=[]
    s=solution()

     # Loop counter
    print("GWO is optimizing  \""+objf.__name__+"\"")    
    
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
            
            # Return back the search agents that go beyond the boundaries of the search space
            Positions[i,:]=numpy.clip(Positions[i,:], lb, ub)
            q_Positions[i,:]=quantizer(Positions[i,:],dim,Position_Nodes,ub,lb)
            #print("Positions[:",i,"]:",Positions[i,:])
            isvalid=False
            while (isvalid==False):
                isvalid,temp1,temp2,temp3=check_validity(q_Positions[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                if (isvalid==False):
                    Positions[i,:]=(ub-lb)*numpy.random.random(dim)
                    q_Positions[i,:]=quantizer(Positions[i,:],dim,Position_Nodes,ub,lb)
                    isvalid,temp1,temp2,temp3=check_validity(q_Positions[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)

            q_Positions[i,:]=quantizer(Positions[i,:],dim,Position_Nodes,ub,lb)
            #print("q_Positions[:",i,"]:",q_Positions[i,:])
            #print("i:",i)
            """for t in range(0,dim):
                for q in range(0,len(Position_Nodes)):
                    if (q*(ub-lb)/len(Position_Nodes)<=Positions[i,t] and (q+1)*(ub-lb)/len(Position_Nodes)>Positions[i,t]):
                        q_Positions[i,t]=Position_Nodes[q]
            """    
            # Calculate objective function for each search agent
            path, fitnes=objf(N_V,graph,q_Positions[i,0],q_Positions[i,dim-1],q_Positions[i,:])
            fitness.append(fitnes)

            # Update Alpha, Beta, and Delta
            if fitness[i]<Alpha_score :
                Alpha_score=fitness[i]; # Update alpha
                Alpha_pos=Positions[i,:].copy()
                q_Alpha_pos=q_Positions[i,:].copy()
                Alpha_path=path.copy()
            
            if (fitness[i]>Alpha_score and fitness[i]<Beta_score ):
                Beta_score=fitness[i]  # Update beta
                Beta_pos=Positions[i,:].copy()
            
            
            if (fitness[i]>Alpha_score and fitness[i]>Beta_score and fitness[i]<Delta_score): 
                Delta_score=fitness[i] # Update delta
                Delta_pos=Positions[i,:].copy()
            
        
        
        timer2=time.time()
        time_interval2=timer2-timerStart
        a=2-time_interval2*((2)/Max_time); # a decreases linearly fron 2 to 0
        
        # Update the Position of search agents including omegas
        i=0
        while i<SearchAgents_no:
            for j in range (0,dim):     
                           
                r1=random.random() # r1 is a random number in [0,1]
                r2=random.random() # r2 is a random number in [0,1]
                
                A1=2*a*r1-a; # Equation (3.3)
                C1=2*r2; # Equation (3.4)
                
                D_alpha=abs(C1*Alpha_pos[j]-Positions[i,j]); # Equation (3.5)-part 1
                X1=Alpha_pos[j]-A1*D_alpha; # Equation (3.6)-part 1
                           
                r1=random.random()
                r2=random.random()
                
                A2=2*a*r1-a; # Equation (3.3)
                C2=2*r2; # Equation (3.4)
                
                D_beta=abs(C2*Beta_pos[j]-Positions[i,j]); # Equation (3.5)-part 2
                X2=Beta_pos[j]-A2*D_beta; # Equation (3.6)-part 2       
                
                r1=random.random()
                r2=random.random() 
                
                A3=2*a*r1-a; # Equation (3.3)
                C3=2*r2; # Equation (3.4)
                
                D_delta=abs(C3*Delta_pos[j]-Positions[i,j]); # Equation (3.5)-part 3
                X3=Delta_pos[j]-A3*D_delta; # Equation (3.5)-part 3             
                
                Positions_upd[i,j]=(X1+X2+X3)/3  #Equation (3.7)
                
            Positions_upd[i,:]=numpy.clip(Positions_upd[i,:], lb, ub)
            q_Positions_upd[i,:]=quantizer(Positions_upd[i,:],dim,Position_Nodes,ub,lb)
            isvalid,temp1,temp2,temp3=check_validity(q_Positions_upd[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
            if isvalid:
                Positions[i,:]=Positions_upd[i,:]
                i=i+1

        Convergence_curve.append(Alpha_score)
        
        timer2=time.time() 
        time_interval=timer2-timerStart
        if time_interval<=Max_time:
            Max_iter=Max_iter+1
        l=l+1
    
    used_Pos=numpy.zeros(len(Position_Nodes))
    used_Comp_Nodes=0
    
    for i in range(0,len(Position_Nodes)):
        for j in range(0,len(Alpha_pos)):
            if q_Alpha_pos[j]==Position_Nodes[i]:
                used_Pos[i]=1
    
    for i in range(0,len(Position_Nodes)):
        used_Comp_Nodes=used_Comp_Nodes+used_Pos[i]
    
    timerEnd=time.time()
    s.pos=q_Alpha_pos
    s.path=Alpha_path
    s.delay=Alpha_score
    s.Energy=used_Comp_Nodes
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=Convergence_curve
    s.optimizer="GWO"
    s.objfname=objf.__name__
    
    return s
    

