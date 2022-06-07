# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:00:00 2020
@author: marzi
Here the whole agents are updated instead of every genes seperately

"""

import random
import numpy
from solution import solution
import time
from benchmarks import check_validity
#from dijkstra import dijkstra
from dijkstra_serv import dijkstra_serv


def DSO(objf,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Source,Destination,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF):

    action_size = 3 #to best, to winner, random
    state_size = 3

    qtable = numpy.zeros((SearchAgents_no,state_size, action_size))
    
    learning_rate = 0.8           # Learning rate
    gamma = 0.95                  # Discounting rate       

    epsil=0.00000001
    P_min0=0.01
    lrg_dec=0.05
    Best_score=float("inf")
    
    #Initialize the positions of search agents
    #print("Initializing")
    Positions=numpy.empty((SearchAgents_no,dim))
    Positions_upd=numpy.empty((1,dim))
    Positions_n=numpy.empty((1,dim))
    
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
            ind[k,:]=numpy.random.randint(0,len(Position_Nodes),dim)
    Convergence_curve=[]
    s=solution()

    # Loop counter
    print("DSO is optimizing  \""+objf.__name__+"\"")    
    
    timerStart=time.time()
    timer2=time.time()
    time_interval=timer2-timerStart
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    
    # Main loop
    Max_iter=1
    l=0

    while l < Max_iter:
        Price_min=P_min0+10*time_interval/Max_time
        Prc_min=Price_min*numpy.ones(SearchAgents_no)
        participate=[]
        proposed_price=[]
        fitness=[]
    
        # Calculate objective function for each search agent
        #print("Calculating objective function")
        for i in range (0,SearchAgents_no):
            path, fitnes, lent, dep_VNF=objf(N_V,graph,Source,Destination,Positions[i,:])
            fitness.append(fitnes)
            
            if fitness[i]<Best_score :
                Best_index=i
                Best_score=fitness[i]; # Update Best
                Best_pos=Positions[i,:].copy()
                Best_path=path.copy()
                Best_dep_VNF=dep_VNF.copy()
                Best_lent=lent
                    
        for i in range (0,SearchAgents_no):
            if (5000/(fitness[i]+epsil) < Prc_min[i])|(i==Best_index):
                participate.append(0)
            else:
                participate.append(1)

        #Performing round 1:
        for i in range (0,SearchAgents_no):
            if participate[i]==0:
                proposed_price.append(0)
            else:
                proposed_price.append(random.uniform(Prc_min[i],1000/(fitness[i]+epsil)))
            
            w=numpy.where(proposed_price == numpy.amax(proposed_price))
            winner=w[0][0]
            
        auc=1
        while auc<3:#Performing rounds 2 & 3:
            for i in range (0,SearchAgents_no):
                if participate[i]==0:
                    proposed_price[i]=0
                else:
                    if i!=winner:
                        Prc_min[i]=random.uniform(Prc_min[i],1000/(fitness[i]+epsil)-(1000/(fitness[i]+epsil)-Prc_min[i])/3)
                        proposed_price[i]=random.uniform(Prc_min[i],1000/(fitness[i]+epsil))
            
            w=numpy.where(proposed_price == numpy.amax(proposed_price))
            winner=w[0][0]
            auc=auc+1

        # Update the Position of search agents
        #print("Updating")
        P_best=0.4
        P_winner=0.3
        P_rand=0.2
        state=numpy.zeros((SearchAgents_no))
        action=numpy.zeros((SearchAgents_no))
        timer3=time.time() 
        for i in range (0,SearchAgents_no):
            ser_at_path=[]
            if timer3-timerStart<Max_time/3:
                #print("Max_time/3")
                r1=random.random()
                if (r1<P_best):#Toward the BEST
                    #print("Toward the BEST")
                    for j in range (0,dim):
                        Positions_upd[0,:]=Positions[i,:].copy()
                        ser_at_path=dijkstra_serv(graph,Positions[i,j],Best_pos[j],Position_Nodes)

                        if len(ser_at_path)>0:
                            best_ind=random.randint(0,len(ser_at_path)-1)
                            
                            Positions_upd[0,j]=ser_at_path[best_ind]
                        else:
                            Positions_upd[0,j]=Best_pos[j]
                    
                        isvalid,temp1,temp2,temp3=check_validity(Positions_upd[0,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                        if isvalid:
                            Positions[i,j]=Positions_upd[0,j]

                elif (r1<P_best+P_winner):#from winner
                    #print("from winner")
                    for j in range (0,dim):
                        Positions_upd[0,:]=Positions[i,:].copy()
                        ser_at_path=dijkstra_serv(graph,Positions[i,j],Positions[winner,j],Position_Nodes)

                        if len(ser_at_path)>0:
                            best_ind=random.randint(0,len(ser_at_path)-1)
                            Positions_upd[0,j]=ser_at_path[best_ind]
                        else:
                            Positions_upd[0,j]=Positions[winner,j]
                                        
                        isvalid,temp1,temp2,temp3=check_validity(Positions_upd[0,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                        if isvalid:
                            Positions[i,j]=Positions_upd[0,j]
                        
                elif (r1<P_best+P_winner+P_rand):#random
                    #print("random")
                    Positions_upd[0,:]=Positions[i,:].copy()
                    for j in range (0,dim):
                        ind=numpy.random.randint(0,len(Position_Nodes),(1,dim))
                        Positions_upd[0,j]=Position_Nodes[ind[0,j]]
                        isvalid,temp1,temp2,temp3=check_validity(Positions_upd[0,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                        if isvalid:
                            Positions[i,j]=Positions_upd[0,j]

            else:
                #print(">  Max_time/3")
                action[i] =numpy.where(qtable[i,int(state[i]),:] == numpy.amax(qtable[i,int(state[i]),:]))[0][0]
                #path_ag, fitness_ag=objf(N_V,graph,Source,Destination,Positions[i,:])
            
                if (action[i]==2):#Toward the BEST
                    #print("Toward the BEST")
                    for j in range (0,dim):
                        Positions_upd[0,:]=Positions[i,:].copy()
                        ser_at_path=dijkstra_serv(graph,Positions[i,j],Best_pos[j],Position_Nodes)
                        if len(ser_at_path)>0:
                            best_ind=random.randint(0,len(ser_at_path)-1)
                            Positions_upd[0,j]=ser_at_path[best_ind]
                        else:
                            Positions_upd[0,j]=Best_pos[j]
                    
                        isvalid,temp1,temp2,temp3=check_validity(Positions_upd[0,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                        if isvalid:
                            Positions[i,j]=Positions_upd[0,j]
                                                
                elif (action[i]==1):#Toward the winner
                    #print("Toward the winner")
                    for j in range (0,dim):
                        Positions_upd[0,:]=Positions[i,:].copy()
                        ser_at_path=dijkstra_serv(graph,Positions[i,j],Positions[winner,j],Position_Nodes)

                        if len(ser_at_path)>0:
                            best_ind=random.randint(0,len(ser_at_path)-1)
                            Positions_upd[0,j]=ser_at_path[best_ind]
                        else:
                            Positions_upd[0,j]=Positions[winner,j]
                            
                        isvalid,temp1,temp2,temp3=check_validity(Positions_upd[0,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                        if isvalid:
                            Positions[i,j]=Positions_upd[0,j]
                        
                elif (action[i]==0):#random
                    #print("random")
                    for j in range (0,dim):
                        Positions_upd[0,:]=Positions[i,:].copy()
                        ind=numpy.random.randint(0,len(Position_Nodes),(1,dim))
                        Positions_upd[0,j]=Position_Nodes[ind[0,j]]
                        isvalid,temp1,temp2,temp3=check_validity(Positions_upd[0,:],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                        if isvalid:
                            Positions[i,j]=Positions_upd[0,j]
                        
                path_ag_n, fitness_ag_n, lent_ag_n, dep_VNF_ag_n=objf(N_V,graph,Source,Destination,Positions[i,:])
                if fitness_ag_n<fitness[i]:
                    reward=1
                else:
                    reward=-1

                next_state=int(action[i])
                action2 =numpy.where(qtable[i,next_state,:] == numpy.amax(qtable[i,next_state,:]))[0][0]
                qtable[i,int(state[i]),int(action[i])] = qtable[i,int(state[i]),int(action[i])] + learning_rate * (reward + gamma * qtable[i,next_state, int(action2)] - qtable[i,int(state[i]), int(action[i])])-action[i]*0.05
                state[i]=next_state
                
        # Decomposition of large Drops:
        r_decomp=random.random()
        if r_decomp<lrg_dec:#decomposition is done
            #print("Decomposition")
            b_p=0.5
            w_p=0.3
            BorW=random.random()
            loc=random.randint(0,dim-1)
            if BorW < b_p:#Best is decomposed
                isvalid,S_Comp_Usage,C_Comp_Usage,IO_Comp_Usage=check_validity(Best_pos[0:loc],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                k=loc
                #print("loc:",loc,"Best_pos:",Best_pos)
                ser_ind=int(numpy.where(Position_Nodes == Best_pos[loc-1])[0][0])
                
                while (S_Comp_Usage[ser_ind]<Storage_AVLB[ser_ind])&(C_Comp_Usage[ser_ind]<Capacity_AVLB[ser_ind])&(IO_Comp_Usage[ser_ind]<IO_AVLB[ser_ind])&(k<len(Best_pos)):
                    S_Comp_Usage_tst=S_Comp_Usage[ser_ind]+Storage_VNF[k]
                    C_Comp_Usage_tst=C_Comp_Usage[ser_ind]+Capacity_VNF[k]                          
                    IO_Comp_Usage_tst=IO_Comp_Usage[ser_ind]+IO_VNF[k]
                    
                    if (S_Comp_Usage_tst<Storage_AVLB[ser_ind])&(C_Comp_Usage_tst<Capacity_AVLB[ser_ind])&(IO_Comp_Usage_tst<IO_AVLB[ser_ind]):
                        Positions_n[0,k]=Best_pos[loc-1]
                        k=k+1
                        #print("K_best:",k, "l:",l)
                        S_Comp_Usage[ser_ind]=S_Comp_Usage_tst
                        C_Comp_Usage[ser_ind]=C_Comp_Usage_tst                         
                        IO_Comp_Usage[ser_ind]=IO_Comp_Usage_tst
                    else:
                        break
                    
                if k<len(Best_pos):
                    #print("not finished-best, k:",k)
                    Pos_new=list(Best_pos[0:loc])+list(Positions_n[0,loc:dim])
                    for j in range (k,dim):
                        isvalid=False
                        #print("Pos_new:",Pos_new)
                        #input()
                        while isvalid==False:
                            #print("notvalid")
                            ind_r=numpy.random.randint(0,len(Position_Nodes),(1,1))
                            Pos_new[j]=Position_Nodes[ind_r[0,0]]
                            #print("Pos_new:",Pos_new)
                            isvalid,temp1,temp2,temp3=check_validity(Pos_new[0:j+1],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                            #print("isvalid:",isvalid)
                            #input()
                else:
                    Pos_new=list(Best_pos[0:loc])+list(Positions_n[0,loc:dim])
                    isvalid=True
                    
            elif (b_p < BorW < b_p+w_p):#winner is decomposed
                isvalid,S_Comp_Usage,C_Comp_Usage,IO_Comp_Usage=check_validity(Positions[winner,0:loc],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                k=loc
                #print("loc:",loc,"Best_pos:",Best_pos)
                ser_ind=int(numpy.where(Position_Nodes == Positions[winner,loc-1])[0][0])
                while (S_Comp_Usage[ser_ind]<Storage_AVLB[ser_ind])&(C_Comp_Usage[ser_ind]<Capacity_AVLB[ser_ind])&(IO_Comp_Usage[ser_ind]<IO_AVLB[ser_ind])&(k<len(Best_pos)):
                    S_Comp_Usage_tst=S_Comp_Usage[ser_ind]+Storage_VNF[k]
                    C_Comp_Usage_tst=C_Comp_Usage[ser_ind]+Capacity_VNF[k]                          
                    IO_Comp_Usage_tst=IO_Comp_Usage[ser_ind]+IO_VNF[k]
                    
                    if (S_Comp_Usage_tst<Storage_AVLB[ser_ind])&(C_Comp_Usage_tst<Capacity_AVLB[ser_ind])&(IO_Comp_Usage_tst<IO_AVLB[ser_ind]):
                        Positions_n[0,k]=Positions[winner,loc-1]
                        k=k+1
                        #print("K_winner:",k,"l:",l)
                        S_Comp_Usage[ser_ind]=S_Comp_Usage_tst
                        C_Comp_Usage[ser_ind]=C_Comp_Usage_tst                         
                        IO_Comp_Usage[ser_ind]=IO_Comp_Usage_tst
                    else:
                        break
                        #print("t1:",t)
                   
                if k<len(Best_pos):
                    #print("not finished-best, k:",k)
                    Pos_new=list(Positions[winner,0:loc])+list(Positions_n[0,loc:dim])
                    for j in range (k,dim):
                        isvalid=False
                        #print("Pos_new:",Pos_new)
                        #input()
                        while isvalid==False:
                            #print("notvalid")
                            ind_r=numpy.random.randint(0,len(Position_Nodes),(1,1))
                            Pos_new[j]=Position_Nodes[ind_r[0,0]]
                            #print("Pos_new:",Pos_new)
                            isvalid,temp1,temp2,temp3=check_validity(Pos_new[0:j+1],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                            #print("isvalid:",isvalid)
                            #input()
                else:
                    Pos_new=list(Positions[winner,0:loc])+list(Positions_n[0,loc:dim])
                    isvalid=True
                    
            else:#a random drop is decomposed
                rand_drop=random.randint(0,SearchAgents_no-1)
                isvalid,S_Comp_Usage,C_Comp_Usage,IO_Comp_Usage=check_validity(Positions[rand_drop,0:loc],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                k=loc
                #print("loc:",loc,"Best_pos:",Best_pos)
                ser_ind=int(numpy.where(Position_Nodes == Positions[rand_drop,loc-1])[0][0])
                while (S_Comp_Usage[ser_ind]<Storage_AVLB[ser_ind])&(C_Comp_Usage[ser_ind]<Capacity_AVLB[ser_ind])&(IO_Comp_Usage[ser_ind]<IO_AVLB[ser_ind])&(k<len(Best_pos)):
                    S_Comp_Usage_tst=S_Comp_Usage[ser_ind]+Storage_VNF[k]
                    C_Comp_Usage_tst=C_Comp_Usage[ser_ind]+Capacity_VNF[k]                          
                    IO_Comp_Usage_tst=IO_Comp_Usage[ser_ind]+IO_VNF[k]
                    
                    if (S_Comp_Usage_tst<Storage_AVLB[ser_ind])&(C_Comp_Usage_tst<Capacity_AVLB[ser_ind])&(IO_Comp_Usage_tst<IO_AVLB[ser_ind]):
                        Positions_n[0,k]=Positions[rand_drop,loc-1]
                        k=k+1
                        #print("K_ran:",k,"l:",l)
                        S_Comp_Usage[ser_ind]=S_Comp_Usage_tst
                        C_Comp_Usage[ser_ind]=C_Comp_Usage_tst                         
                        IO_Comp_Usage[ser_ind]=IO_Comp_Usage_tst
                    else:
                        break
                    
                if k<len(Best_pos):
                    #print("not finished-best, k:",k)
                    Pos_new=list(Positions[rand_drop,0:loc])+list(Positions_n[0,loc:dim])
                    for j in range (k,dim):
                        isvalid=False
                        #print("Pos_new:",Pos_new)
                        #input()
                        while isvalid==False:
                            #print("notvalid")
                            ind_r=numpy.random.randint(0,len(Position_Nodes),(1,1))
                            Pos_new[j]=Position_Nodes[ind_r[0,0]]
                            #print("Pos_new:",Pos_new)
                            isvalid,temp1,temp2,temp3=check_validity(Pos_new[0:j+1],Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
                            #print("isvalid:",isvalid)
                            #input()
                else:
                    Pos_new=list(Positions[rand_drop,0:loc])+list(Positions_n[0,loc:dim])
                    isvalid=True
                    
            isvalid,temp1,temp2,temp3=check_validity(Pos_new,Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
            if (isvalid):
                Positions=numpy.append(Positions,Pos_new)
                SearchAgents_no=SearchAgents_no+1
                #print("SearchAgents_no:",SearchAgents_no)
                Positions=Positions.reshape(SearchAgents_no,dim)
                q_newagent=numpy.zeros((1,state_size, action_size))
                qtable=numpy.append(qtable,q_newagent)
                qtable=qtable.reshape(SearchAgents_no,state_size, action_size)
                state=list(state)+list([0])
                action=list(action)+list([0])
          
        lrg_dec=1.02*lrg_dec

        Convergence_curve.append(Best_score)

        timer2=time.time() 
        time_interval=timer2-timerStart
        if time_interval<=Max_time:
            Max_iter=Max_iter+1
        l=l+1
            
    timerEnd=time.time()
             
    isvalid,S_Comp_Usage,C_Comp_Usage,IO_Comp_Usage=check_validity(Best_pos,Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
    for i in range(len(Storage_AVLB)):
        Storage_AVLB[i]=Storage_AVLB[i]-S_Comp_Usage[i]
        Capacity_AVLB[i]=Capacity_AVLB[i]-C_Comp_Usage[i]
        IO_AVLB[i]=IO_AVLB[i]-IO_Comp_Usage[i]
        
    used_Pos=numpy.zeros(len(Position_Nodes))
    used_Comp_Nodes=0
    
    for i in range(0,len(Position_Nodes)):
        for j in range(0,len(Best_pos)):
            if Best_pos[j]==Position_Nodes[i]:
                used_Pos[i]=1
    
    for i in range(0,len(Position_Nodes)):
        used_Comp_Nodes=used_Comp_Nodes+used_Pos[i]
        
    
    
    s.pos=Best_pos
    s.path=Best_path
    s.dep_VNF=Best_dep_VNF
    s.len_path=Best_lent
    s.delay=Best_score
    s.Energy=used_Comp_Nodes
    s.capacities=([Storage_AVLB,Capacity_AVLB,IO_AVLB])
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=Convergence_curve
    s.optimizer="DSO"
    s.objfname=objf.__name__
    
    
    return s
    

