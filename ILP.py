from cvxopt.glpk import ilp
import numpy as np
from cvxopt import matrix
from solution import solution
import time
from dijkstra import dijkstra

def ILP(objf,N_V,graph,Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF):

    #print (help(ilp))    
    s=solution()
    N=len(Position_Nodes)
    timerStart=time.time()
    
    #x : (N*N*(dim-1)) X 1
    Dly=matrix(np.zeros((N,N)))#delay of all links BETWEEN COMP NODES
    c=matrix(np.zeros(N*N*(dim-1),dtype=float))#c.T: 1 X (N*N*(dim-1))
    R=matrix(np.zeros((3*N,N*dim)))#G=R*L:(3N) X (N*dim)
    L=matrix(np.zeros((dim*N,N*N*(dim-1))))
    L2=matrix(np.zeros((dim*N,N*N*(dim-1))))
    h=matrix(np.zeros(3*N))
    AP=matrix(np.zeros((dim,N*dim)))#َAP:E
    A=matrix(np.zeros((dim+dim*N,N*N*(dim-1))))#َA=AP*L:(dim+dim.N) X (N*N*(dim-1))
    b=matrix(np.zeros(dim+dim*N,dtype=float))
    E=matrix(np.zeros((dim,N*dim)))
    J=matrix(np.ones(N))
    Fi=matrix(np.zeros((N,dim)))
    
    for j in range(N):
        for i in range(j):
            path, fitnes=dijkstra(graph, Position_Nodes[i], Position_Nodes[j])
            if fitnes==float("inf"):
                fitnes=1000000000
            Dly[i,j]=fitnes
    
    for i in range(N):
        for j in range(i):
            Dly[i,j]=Dly[j,i]
    
    for k in range(dim-1):
        for i in range(N):
            for j in range(N):
                c[k*N*N+i*N+j]=Dly[i,j]

    for k in range(dim):
        for i in range(N):
            for j in range(N):
                if k==0:
                    L2[i,i*N+j]=1
                else:
                    L2[k*N+i,(k-1)*N*N+j*N+i]=1
    
    for k in range(dim):
        for i in range(N):
            for j in range(N):
                if k==dim-1:
                    L[k*N+i,(k-1)*N*N+j*N+i]=1
                else:
                    L[k*N+i,k*N*N+i*N+j]=1
                    
    for k in range(3):
        for i in range(N):
            for j in range(dim):
                if k == 0:
                    R[k*N+i,j*N+i]=Capacity_VNF[j]
                elif k == 1:
                    R[k*N+i,j*N+i]=Storage_VNF[j]
                else:
                    R[k*N+i,j*N+i]=IO_VNF[j]
                    
            if k == 0:
                h[k*N+i]=Capacity_AVLB[i]
            elif k == 1:
                h[k*N+i]=Storage_AVLB[i]
            else:
                h[k*N+i]=IO_AVLB[i]

    G=R*L
    
    for i in range(dim):
        for j in range(N):
            E[i,j+N*i]=1
                
    for i in range (dim):
        for j in range(N*dim):
            AP[i,j]=E[i,j]
       
    A1=AP*L
    for i in range(dim):
        for j in range(N*N*(dim-1)):
            A[i,j]=A1[i,j]

    for i in range(dim,dim+dim*N):
        for j in range(N*N*(dim-1)):
            A[i,j]=L[i-dim-1,j]-L2[i-dim-1,j]
                  
    for k in range (dim):
        b[k]=1
    
    for k in range(dim,dim+dim*N):
        b[k]=0
        
    B=set(range(N*N*(dim-1)))
    I=set()
        
    (status,x)=ilp(c,G,h,A,b,I,B)
    timerEnd=time.time()
    print(status)
    
    T=L*x
        
    for i in range (N):
        for j in range (dim):
            Fi[i,j]=T[i+j*N]
        
    for i in range(N):
        J[i]=i

    M=J.T*Fi
    Positions=[]
    for i in range(dim):
        Positions.append(Position_Nodes[int(M[i])])
    
    print("Positions:",Positions)
    Delay=[]
    
    path, fitnes=objf(N_V,graph,Positions[0],Positions[dim-1],Positions)
    Dlay=c.T*x
    print("Dlay:",Dlay[0],fitnes)
    Delay=Dlay[0]
    
    #print("path:",path)
    
    used_Pos=np.zeros(len(Position_Nodes))
    used_Comp_Nodes=0
    
    for i in range(0,len(Position_Nodes)):
        for j in range(0,len(Positions)):
            if Positions[j]==Position_Nodes[i]:
                used_Pos[i]=1
    
    for i in range(0,len(Position_Nodes)):
        used_Comp_Nodes=used_Comp_Nodes+used_Pos[i]
             
    s.pos=Positions
    s.path=path
    s.delay=Delay
    s.Energy=used_Comp_Nodes
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.optimizer="ILP"
    s.objfname=objf.__name__
    
    return s
