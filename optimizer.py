# -*- coding: utf-8 -*-
"""
Created on DEC 2021

@author: Marzi
"""

#import EGWO as EGWO
import PSO as PSO
import DSO as DSO
import IEGWO as IEGWO
import WOA as WOA
import GWO as GWO
import ILP as ILP

import benchmarks
import csv
import numpy
from network import network

#********************************************************

def main_algo(alg,substrate_graph,func_details,popSize,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF):
    function_name=func_details[0]
    V_Comp=func_details[1]
    dim=func_details[2]
    N_V=func_details[3]
    lb=0
    ub=5000
    
    if alg == 0:#DOA(objf,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
        x=DSO.DSO(getattr(benchmarks, function_name),N_V,substrate_graph,V_Comp,dim,popSize,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
    if alg == 1:#IEGWO(objf,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
        x=IEGWO.IEGWO(getattr(benchmarks, function_name),N_V,substrate_graph,V_Comp,dim,popSize,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
    if alg == 2:#GWO(objf,lb,ub,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
        x=GWO.GWO(getattr(benchmarks, function_name),lb,ub,N_V,substrate_graph,V_Comp,dim,popSize,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
    if alg == 3:#WOA(objf,lb,ub,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
        x=WOA.WOA(getattr(benchmarks, function_name),lb,ub,N_V,substrate_graph,V_Comp,dim,popSize,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
    if alg == 4:#PSO(objf,lb,ub,N_V,graph,Position_Nodes,dim,SearchAgents_no,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
        x=PSO.PSO(getattr(benchmarks, function_name),lb,ub,N_V,substrate_graph,V_Comp,dim,popSize,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
    if alg == 5:#ILP (objf,N_V,graph,Position_Nodes,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
        x=ILP.ILP(getattr(benchmarks, function_name),N_V,substrate_graph,V_Comp,dim,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)
    
    return x
        
# Select number of repetitions for each experiment. 
# To obtain meaningful statistical results, usually 30 independent runs 
# are executed for each algorithm.
NumOfRuns=1

# Select general parameters for all optimizers (population size, number of iterations)
PopulationSize = 60
Iterations = 100
Num_of_runs = 15

#Export results ?
Export=True

# CSV Header for the cinvergence 
CnvgHeader=[]

for l in range(0,Iterations):
	CnvgHeader.append("Iter"+str(l+1))
    
algorithm=["DSO","IEGWO","GWO","WOA","PSO","ILP"]
netw=["CRL","NIIF","DFN","Uninett","TWTelecom","OTE","ITCDeltacom","ION","ColtTelecom","Cogent"]

for net in range(8,len(netw)):
    Max_time,substrate_graph,N_V,N_E,V_Comp,VComp_num,VNF_num,link_delay,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF=network(net)
    for alg in range(3,5):
        for itr in range(0,Num_of_runs):
            print("run number: ",itr)
            for k in range (0,NumOfRuns): 
                func_details=["F_dijkstragraph",V_Comp,VNF_num,N_V]
                x=main_algo(alg,substrate_graph,func_details,PopulationSize,Max_time,Storage_AVLB,Capacity_AVLB,IO_AVLB,Storage_VNF,Capacity_VNF,IO_VNF)                   
                #ExportToFile="YourResultsAreHere.csv"
                #Automaticly generated name by date and time
                ExportToFile_all="All_runs_"+algorithm[alg]+"_"+netw[net]+".csv" 
                with open(ExportToFile_all, 'a', newline='\n')as out2:
                    writer=csv.writer(out2,delimiter=',')
                    header= numpy.concatenate([["ExecutionTime","Final Delay","Energy Consumption","Final Position","Final Path"],CnvgHeader])
                    if itr == 0:
                        writer.writerow(header)
                    a2=numpy.concatenate([[x.executionTime,x.delay,x.Energy,x.pos,x.path],x.convergence])
                    writer.writerow(a2)
                    out2.close()