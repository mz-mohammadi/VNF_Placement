# -*- coding: utf-8 -*-
"""
Created on DEC 2021

@author: Marzi
"""

import random
import numpy
import math
from solution import solution
import time
from benchmarks import quantizer
from benchmarks import check_validity


def WOA(objf,lb,ub,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF):

    #dim=30
    #SearchAgents_no=50
    #lb=-100
    #ub=100
    #Max_iter=500
        
    
    # initialize position vector and score for the leader
    Leader_pos=numpy.zeros(dim)
    Leader_score=float("inf")  #change this to -inf for maximization problems
    
    
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
        isvalid,temp1,temp2,temp3=check_validity(Positions[k,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
        if isvalid:
            k=k+1
        else:
            Positions[k,:]=(ub-lb)*numpy.random.random(dim)
            
    #print("Positions:",Positions)
    #print("q_Positions:",q_Positions)

    #Initialize convergence
    Convergence_curve=[]
    s=solution()

    print("WOA is optimizing  \""+objf.__name__+"\"")    

    timerStart=time.time() 
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    ############################
    
    # Main loop
    timerStart=time.time()
    timer2=time.time()
    time_interval=timer2-timerStart
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    
    Max_iter=1
    itr=0

    while itr < Max_iter:
        fitness=[]
        for i in range(0,SearchAgents_no):
            
            # Return back the search agents that go beyond the boundaries of the search space
            Positions[i,:]=numpy.clip(Positions[i,:], lb, ub)
            q_Positions[i,:]=quantizer(Positions[i,:],dim,Position_Nodes,ub,lb)
            #print("Positions[",i,"]:",Positions[i,:])
            
            isvalid=False
            while (isvalid==False):
                isvalid,temp1,temp2,temp3=check_validity(q_Positions[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                if (isvalid==False):
                    Positions[i,:]=(ub-lb)*numpy.random.random(dim)
                    q_Positions[i,:]=quantizer(Positions[i,:],dim,Position_Nodes,ub,lb)
                    isvalid,temp1,temp2,temp3=check_validity(q_Positions[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
            #print(isvalid)    
            #print("q_Positions[",i,"]:",q_Positions[i,:])
            # Calculate objective function for each search agent
            path, fitnes=objf(N_V,graph,q_Positions[i,0],q_Positions[i,dim-1],q_Positions[i,:])
            fitness.append(fitnes)
            
            # Update the leader
            if fitness[i]<Leader_score: # Change this to > for maximization problem
                Leader_score=fitness[i]; # Update alpha
                Leader_pos=Positions[i,:].copy() # copy current whale position into the leader position
                q_Leader_pos=q_Positions[i,:].copy()
                Leader_path=path.copy()
                #print("q_Leader_pos:",q_Leader_pos)
                #print("Leader_path:",Leader_path)
                #print("Leader_score:",Leader_score)
             
        timer2=time.time()
        time_interval2=timer2-timerStart
        a=2-time_interval2*((2)/Max_time); # a decreases linearly fron 2 to 0 in Eq. (2.3)
        
        # a2 linearly decreases from -1 to -2 to calculate t in Eq. (3.12)
        a2=-1+time_interval2*((-1)/Max_time);
        
        # Update the Position of search agents 
        i=0
        while i<SearchAgents_no:
            r1=random.random() # r1 is a random number in [0,1]
            r2=random.random() # r2 is a random number in [0,1]
            
            A=2*a*r1-a  # Eq. (2.3) in the paper
            C=2*r2      # Eq. (2.4) in the paper
                       
            b=1;               #  parameters in Eq. (2.5)
            l=(a2-1)*random.random()+1   #  parameters in Eq. (2.5)
            
            p = random.random()        # p in Eq. (2.6)
            
            for j in range(0,dim):
                
                if p<0.5:
                    if abs(A)>=1:
                        rand_leader_index = math.floor(SearchAgents_no*random.random());
                        X_rand = Positions[rand_leader_index, :]
                        D_X_rand=abs(C*X_rand[j]-Positions[i,j]) 
                        Positions_upd[i,j]=X_rand[j]-A*D_X_rand      
                        
                    elif abs(A)<1:
                        D_Leader=abs(C*Leader_pos[j]-Positions[i,j]) 
                        Positions_upd[i,j]=Leader_pos[j]-A*D_Leader      
                    
                    
                elif p>=0.5:
                  
                    distance2Leader=abs(Leader_pos[j]-Positions[i,j])
                    # Eq. (2.5)
                    Positions_upd[i,j]=distance2Leader*math.exp(b*l)*math.cos(l*2*math.pi)+Leader_pos[j]
            
            q_Positions_upd[i,:]=quantizer(Positions_upd[i,:],dim,Position_Nodes,ub,lb)
            isvalid,temp1,temp2,temp3=check_validity(q_Positions_upd[i,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
            if isvalid:
                #print("isvalid")
                #print("q_Positions_upd[",i,":]",q_Positions_upd[i,:])
                #input()
                Positions[i,:]=Positions_upd[i,:]
                i=i+1
        
        Convergence_curve.append(Leader_score)
        
        timer2=time.time() 
        time_interval=timer2-timerStart
        if time_interval<=Max_time:
            Max_iter=Max_iter+1
        itr=itr+1
        #print("l:",l)
    
    used_Pos=numpy.zeros(len(Position_Nodes))
    used_Comp_Nodes=0
    
    for i in range(0,len(Position_Nodes)):
        for j in range(0,len(q_Leader_pos)):
            if q_Leader_pos[j]==Position_Nodes[i]:
                used_Pos[i]=1
    
    for i in range(0,len(Position_Nodes)):
        used_Comp_Nodes=used_Comp_Nodes+used_Pos[i]
    
    timerEnd=time.time()
    s.pos=q_Leader_pos
    s.path=Leader_path
    s.delay=Leader_score
    s.Energy=used_Comp_Nodes
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=Convergence_curve
    s.optimizer="WOA"
    s.objfname=objf.__name__
    
    return s