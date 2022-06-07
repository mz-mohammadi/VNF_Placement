A solution to VNFP problem in Python
Here a new algorithm proposed to solve VNF placement problem is presented:Drops Optimization Algorithm (DSO)
To have a comparison, some conventional previous algorithms are implemented, as well: GWO, PSO, WOA, IEGWO, and ILP
To evaluate the implemented algorithms, some networks from topology-zoo.org are used.
The project contains these files:
optimizer: the main module which should be run
DSO: the DSO algorithm
GWO: the GWO algorithm
PSO: the PSO algorithm
WOA: the WOA algorithm
IEGWO: the IEGWO algorithm
networks: description of networks
some modules which are required: ARP, benchmarks, dijkstra, dijkstra_serv, solution
the parameters of the network capacities and VNF requirements: excel files

the output is an excel file for each network
