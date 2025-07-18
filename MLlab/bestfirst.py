def best_first_search(graph, start, goal,heuristic,path=None):
    if path is None:
        path=[]
    
    ol=[(0,start)]
    close_l=set()
    close_l.add(start)

    while ol:
        ol.sort(key=lambda x: heuristic[x[1]],reverse=True)
        cost,node=ol.pop()
        path.append(node)

        if node==goal:
            return cost,path
        
        close_l.add(node)
        for neighbor, neighborcost in graph[node]:
            if neighbor not in close_l:
                ol.append((cost + neighborcost,neighbor))
                close_l.add(neighbor)
            
    return None

graph= {'S':[('A',4),('B',5),('C',6)],'A':[],'B':[('D',6),('H',10)],'C':[],'D':[],'H':[('E',11),('G',4)],'F':[],'G':[('E',11)]}
heuristic={'S':10,'A':9,'B':7,'C':8,'D':8,'H':6,'F':6,'G':3,'E':0}
start='S'
end='E'

result=best_first_search(graph,start,end,heuristic)

if result:
    print(f'the minimum cost between {start} to {end} is {result}')
    print(f'cost {result[0]}')
else:
    print(f'there is no minimum path between {start} to {end}')
