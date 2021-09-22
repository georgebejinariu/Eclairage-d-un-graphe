# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:52:50 2020

@author: Asus
"""

#from Graph_Class import Vertex
from Graph_Class import Graph
import random
#from math import factorial



g = Graph()
g.add_edge(1, 2,1,1)

def f_lit_con_graf(nr_nodes,nr_edges):
    """  
    spawning a connected graph with nr_nodes nodes 
                                and nr_edges edges
        nr_edges in [nr_nodes - 1, nr_nodes*(nr_nodes-1)/2 ]
    """
    if nr_edges < nr_nodes-1 or nr_edges > nr_nodes*(nr_nodes-1)/2:
        print('nr_edges not in [nr_nodes - 1, nr_nodes*(nr_nodes-1)/2 ]')
        return 0

    fop = Graph()
    fop_l = []
    fop.add_vertex(0, 1)
    for i in range(1,nr_nodes):
        r = random.choice(list(fop.vert_dict.keys()))
        fop.add_vertex(i, 1)
        fop.add_edge(i,r)
        fop_l.append((i,r))
        fop_l.append((r,i))
        
        
    for i in range(nr_nodes-1, nr_edges):
        fr = random.choice(list(fop.vert_dict.keys()))
        to = random.choice(list(fop.vert_dict.keys()))
        while to == fr:
            to = random.choice(list(fop.vert_dict.keys()))
        
        while (fr,to) in fop_l:
            fr = random.choice(list(fop.vert_dict.keys()))
            to = random.choice(list(fop.vert_dict.keys()))
            while to == fr:
                to = random.choice(list(fop.vert_dict.keys()))
        
        fop.add_edge(fr, to)
        fop_l.append((fr,to))
        fop_l.append((to,fr))
    return fop


def simulated_annealing(g):
    adj_dic = {}
    ##switching leafs off and counting the edges each node has
    M = 0
    m = 10**1000
    S = 0
    j = 0
    for i in g.vert_dict.keys():
        l = len(g.vert_dict[i].adjacent)
        adj_dic[i] = len(g.vert_dict[i].adjacent)
        if l > M:
            M = l
        if l < m:
            m = l
        S = S + l
        j+=1
        
        if len(g.vert_dict[i].adjacent) == 1:
            g.vert_dict[i].light = 0
    
    Avg = S/j
    
    
    ###create the lights_list
    for i in range(10):
        r = random.choice(list(g.vert_dict.keys()))
        if adj_dic[r] < Avg:
            if random.random() > 0.1:
                g.switch_off(r)
                
        
        while g.is_lit() ==0:
                r = random.choice(list(g.vert_dict.keys()))
                g.switch_on(r)
        
        
        while g.is_min_lit() == 0:
            
            r = random.choice(list(g.vert_dict.keys()))
            if adj_dic[r] < Avg:
                if random.random() > 0.1:
                    g.switch_off(r)
            else:
                if random.random() > 0.5:
                    g.switch_off(r)
            
            
            
            while g.is_lit() ==0:
                r = random.choice(list(g.vert_dict.keys()))
                g.switch_on(r)
        

# def simulated_annealing_1(g):
#     # adj_dic = {}
#     # ##switching leafs off and counting the edges each node has
#     # M = 0
#     # m = 10**1000
#     # S = 0
#     # j = 0
#     # for i in g.vert_dict.keys():
#     #     l = len(g.vert_dict[i].adjacent)
#     #     adj_dic[i] = len(g.vert_dict[i].adjacent)
#     #     if l > M:
#     #         M = l
#     #     if l < m:
#     #         m = l
#     #     S = S + l
#     #     j+=1
        
#     #     if len(g.vert_dict[i].adjacent) == 1:
#     #         g.vert_dict[i].light = 0
    
#     # Avg = S/j
    
    
#     ###create the lights_list
    
#     while g.is_min_lit() == 0:
#         r = random.choice(list(g.vert_dict.keys()))
#         if g.vert_dict[r].light ==1:
#             if random.random() > 0.1:
#                 g.switch_off(r)
            
#        while g.is_lit() ==0:
#            r = random.choice(list(g.vert_dict.keys()))
#            if g.vert_dict[r].light ==0:
#                g.switch_on(r)
    
    
#     return g
            




def simulated_annealing_2(g):
    adj_dic = {}
    ##switching leafs off and counting the edges each node has
    M = 0
    m = 10**1000
    S = 0
    j = 0
    for i in g.vert_dict.keys():
        l = len(g.vert_dict[i].adjacent)
        adj_dic[i] = len(g.vert_dict[i].adjacent)
        if l > M:
            M = l
        if l < m:
            m = l
        S = S + l
        j+=1
        
        if len(g.vert_dict[i].adjacent) == 1:
            g.vert_dict[i].light = 0
    
    Avg = S/j
    
    
    ###create the lights_list

    r = random.choice(list(g.vert_dict.keys()))
    if g.vert_dict[r] ==1:
            
        if adj_dic[r] < Avg:
            if random.random() > 0.2:
                g.switch_off(r)
        else:
            if random.random() >0.7:
                g.switch_off(r)
        
    while g.is_lit() ==0:
        r = random.choice(list(g.vert_dict.keys()))
        g.switch_on(r)
        
    return g


############################# Naiv algorithm ##################################

def simple_search(g):
    while g.is_min_lit() == 0:
        r = random.choice(list(g.vert_dict.keys())) #complexity???? O(n)
        if g.vert_dict[r].light == 1:  
            g.vert_dict[r].light =0
        if g.is_lit() == 0:
            g.vert_dict[r].light = 1
    return g

############################## End Naiv algorithm ########################



############################ Main algorithm ############################################

def search_min(g):
    adj_dic = {}
    ##counting the edges each node has
    M = 0
    m = 10**1000
    S = 0
    j = 0
    for i in g.vert_dict.keys():
        l = len(g.vert_dict[i].adjacent)
        adj_dic[i] = l
        if l > M:
            M = l
        if l < m:
            m = l
        S = S + l
        j+=1
        
        if len(g.vert_dict[i].adjacent) == 1:
            g.vert_dict[i].light = 0
    
    Avg = S/j
    # print('avg = ', Avg)
    # print('m=',m)
    # print('M=',M)
    if Avg == m:
        while g.is_min_lit_special() == 0:
            r = random.choice(list(g.vert_dict.keys())) #complexity???? O(n)
            if g.vert_dict[r].light == 1:
                if adj_dic[r] <= Avg:
                    # p = 0.1 + 0.4/b-a (x-a)
                    if random.random() >0.1 + (0.4/(Avg-m +1))*(adj_dic[r]-m):
                        g.vert_dict[r].light =0
                # elif adj_dic[r] > Avg:
                #     #p = 0.5 + 0.4/(c-b) (x-b)
                #     if random.random() > 0.5 + ((0.4)/(M-Avg))*(adj_dic[r]- Avg):
                #         g.vert_dict[r].light = 0
        
            if g.is_lit() == 0:
                g.vert_dict[r].light = 1
        
    
    while g.is_min_lit_special() == 0:
        r = random.choice(list(g.vert_dict.keys())) #complexity???? O(n)
        if g.vert_dict[r].light == 1:
            if adj_dic[r] <= Avg:
                # p = 0.1 + 0.4/b-a (x-a)
                if random.random() >0.1 + (0.4/(Avg-m))*(adj_dic[r]-m):
                    g.vert_dict[r].light =0
            elif adj_dic[r] > Avg:
                #p = 0.5 + 0.4/(c-b) (x-b)
                if random.random() > 0.5 + ((0.4)/(M-Avg))*(adj_dic[r]- Avg):
                    g.vert_dict[r].light = 0
        
        if g.is_lit() == 0:
            g.vert_dict[r].light = 1
            
    
    # print('how many lights',g.how_many_lights())
    # if Avg-2 <1:
    #     print('Vert/avg', (1)*(g.num_vertices/Avg))
    # elif Avg-2 >1:
    #     print('Vert/avg', (Avg-2)*(g.num_vertices/Avg))
    
    # K = 0
    # for node in g.vert_dict.keys():
    #     if g.vert_dict[node].light ==1:
    #         K = K+ len(g.vert_dict[node].adjacent)
    # print('K=',K)
            
    return g



######################################## End Main Algorithm ##########################



##########################################

def simple_search_opt(g):
    
    
    for i in range(20):
        #sol_dict = {}
        nr_list = []
        while g.is_min_lit() == 0:
            r = random.choice(list(g.vert_dict.keys())) #complexity???? O(n)
            if g.vert_dict[r].light == 1:  
                g.vert_dict[r].light =0
            if g.is_lit() == 0:
                g.vert_dict[r].light = 1
        #sol_dict[g.how_many_lights] = {g.lit_lists()[2]}
        nr_list.append(g.how_many_lights())
        g.switch_graph_on()
    
    m = min(nr_list)
    return m

def search_opt(g):
    nr_list = []
    for i in range(20):
        search_min(g)
        nr_list.append(g.how_many_lights())
        g.switch_graph_on()
    return min(nr_list)

##########################################



def search_min_plot(g):
    adj_dic = {}
    ##counting the edges each node has
    M = 0
    m = 10**1000
    S = 0
    j = 0
    for i in g.vert_dict.keys():
        l = len(g.vert_dict[i].adjacent)
        adj_dic[i] = len(g.vert_dict[i].adjacent)
        if l > M:
            M = l
        if l < m:
            m = l
        S = S + l
        j+=1
        
        if len(g.vert_dict[i].adjacent) == 1:
            g.vert_dict[i].light = 0
    
    Avg = S/j
    # print('avg = ', Avg)
    # print('m=',m)
    # print('M=',M)
    if Avg == m:
        while g.is_min_lit() == 0:
            r = random.choice(list(g.vert_dict.keys())) #complexity???? O(n)
            if g.vert_dict[r].light == 1:
                if adj_dic[r] <= Avg:
                    # p = 0.1 + 0.4/b-a (x-a)
                    if random.random() >0.1 + (0.4/(Avg-m +1))*(adj_dic[r]-m):
                        g.vert_dict[r].light =0
                # elif adj_dic[r] > Avg:
                #     #p = 0.5 + 0.4/(c-b) (x-b)
                #     if random.random() > 0.5 + ((0.4)/(M-Avg))*(adj_dic[r]- Avg):
                #         g.vert_dict[r].light = 0
        
            if g.is_lit() == 0:
                g.vert_dict[r].light = 1
        
    
    while g.is_min_lit() == 0:
        r = random.choice(list(g.vert_dict.keys())) #complexity???? O(n)
        if g.vert_dict[r].light == 1:
            if adj_dic[r] <= Avg:
                # p = 0.1 + 0.4/b-a (x-a)
                if random.random() >0.1 + (0.4/(Avg-m))*(adj_dic[r]-m):
                    g.vert_dict[r].light =0
            elif adj_dic[r] > Avg:
                #p = 0.5 + 0.4/(c-b) (x-b)
                if random.random() > 0.5 + ((0.4)/(M-Avg))*(adj_dic[r]- Avg):
                    g.vert_dict[r].light = 0
        
        if g.is_lit() == 0:
            g.vert_dict[r].light = 1
            
    
    # print('how many lights',g.how_many_lights())
    # if Avg-2 <1:
    #     print('Vert/avg', (1)*(g.num_vertices/Avg))
    # elif Avg-2 >1:
    #     print('Vert/avg', (Avg-2)*(g.num_vertices/Avg))
    
    # K = 0
    # for node in g.vert_dict.keys():
    #     if g.vert_dict[node].light ==1:
    #         K = K+ len(g.vert_dict[node].adjacent)
    # print('K=',K)
    
    
    
    
    return g, Avg, g.how_many_lights()


def turn_on_connected(g):
    g.switch_graph_on()
    Avg = 2*len(g.edges)/g.num_vertices
    V = g.num_vertices
    F = (Avg-2)*V/Avg
    print(F)
    adj_dic = {}
    for i in g.vert_dict.keys():
        #l = len(g.vert_dict[i].adjacent)
        adj_dic[i] = len(g.vert_dict[i].adjacent)
        
    d = {k: v for k, v in sorted(adj_dic.items(), key=lambda item: item[1])}
    i = 0
    for k in d.keys():
        g.switch_off(k)
        i+=1
        if i >= g.num_vertices - F:
            break
    return g
    
        
        



fop = Graph()

fop.add_vertex(0, 1)
fop.add_vertex(1, 1)
fop.add_vertex(2, 1)
fop.add_vertex(3, 1)
fop.add_vertex(4, 0)
fop.add_vertex(5, 1)


fop.add_edge(0, 1)
fop.add_edge(0, 2)
fop.add_edge(0, 3)
fop.add_edge(0, 4)
fop.add_edge(4, 5)
fop.add_edge(4, 3)
fop.add_edge(2, 3)
fop.add_edge(2, 5)
fop.add_edge(1, 5)
fop.add_edge(1, 3)



if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a',0)
    g.add_vertex('b',0)
    g.add_vertex('c',1)
    g.add_vertex('d',0)
    g.add_vertex('e',1)
    g.add_vertex('f',0)

    g.add_edge('a', 'b')  
    g.add_edge('a', 'c')
    g.add_edge('a', 'f')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('c', 'd')
    g.add_edge('c', 'f')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')
    g.add_edge('a','b')
