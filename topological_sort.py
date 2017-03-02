#-*- coding:UTF-8  -*-
# 实现拓扑排序的Kahn's algorithm
def topological_sort(v,e):
    if not len(v) or not len(e):
        return None

    # 没有输入边的节点
    S = set()
    for node in v:
        incoming = True
        for edge in e:
            if node == edge[1]:
                incoming = False
                break
        if incoming is True:
            S.add(node)   

    # 拓扑排序的节点
    L = list()
    print(S)
    while len(S) :
        s = S.pop()
        L.append(s) 
        print("L--->:",L)
        print("S--->:",S)
        # 节点对应所有的节点:key为节点，value为对应边界
        nodes_edges_from_S = {}
        for edge in e:
            if s== edge[0]:
                nodes_edges_from_S[edge[1]] = edge
        print("nodes_edges_from_S--->",nodes_edges_from_S)
        # 遍历s连接的所有的节点:先删除s对应的所有边界，然后判断连接的节点是否还有incoming边界，无则添加
        for node in nodes_edges_from_S.keys():
            e.remove(nodes_edges_from_S.get(node))
        for node in nodes_edges_from_S.keys():
            if isNoIncoming(node,e):
                S.add(node)
        
        print("updated S--->:",S)
        print("===")
    # 如果存在环则报错
    if len(e):
        raise Exception("存在环，无法进行拓扑排序")
    return L

# 判断某个节点是否已无incoming edge
def isNoIncoming(node,e):
    for edge in e:
        if node == edge[1]:
            return False
    return True

# 测试拓扑排序
v=['a','b','c','d','e']   
e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')] 
# adebc or abdec or adbec
print(topological_sort(v,e))
v=['a','b','c','d']  
e=[('a','b'),('a','d'),('b','c'),('d','c'),('a','c')] 
# abdc or adbc 
print(topological_sort(v,e))