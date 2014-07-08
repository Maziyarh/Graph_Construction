'''
Created on Oct 14, 2013

@author: Maziyar
'''
import networkx as nx
import numpy as np
def IsGraphicalEG(d):
    x = True
    sum_degrees = np.sum(d)
    if (np.mod(sum_degrees,2) != 0):
        x = False
    else:
        degree_dec = np.sort(d)[::-1]
        N = len(d)
        for k in xrange(0,N):
           temp1 =  np.sum(degree_dec[0:k+1])
           temp2 = range(0,N)
           temp3 = np.minimum(temp2[k+1:],degree_dec[k+1:])
           if temp1 > np.sum(temp3)+k*(k+1):
               x= False
               break
        return x
def modify_deg(d,a,b):
    dd = np.copy(d)
    dd[a] = dd[a] - 1
    dd[b] = dd[b] + 1
    if dd[a] == 0:
        dd.remove(a)
    return dd

degrees = input('enter the degree distribution')
print(IsGraphicalEG(degrees))
forbidden_nodes =[]
N = len(degrees)
adjacency = np.zeros((N,N))
deg = np.sort(degrees)[::-1]
deg_tem = np.copy(deg)
stubs = np.copy(deg_tem)
hubs = range(0,N)
while len(hubs) > 0:
    rightmostadj = []
    node = hubs(0)
    forbidden_nodes.append(node)
    k = len(deg_tem)
    if IsGraphicalEG(modify_deg(degrees,node,k)):
        adjacency[(node,k)] = 1
        adjacency[(k,node)] = 1
        rightmostadj.append(k)
        k = k-1
    else:
        forbidden_nodes.append(k)
        k = k - 1
    
    