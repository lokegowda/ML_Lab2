import random

def obj_value(x):

    return -x**2+10*x

def hill_climbing(start,step_size=0.1,mx_iteration=100):
    current=start
    currentV=obj_value(current)
    bestnode=current
    bestvalue=currentV

    history=[]

    for i in range(mx_iteration):
        nextnode=current+step_size
        nextv=obj_value(nextnode)
        nextnode2=current-step_size
        nextv2=obj_value(nextnode2)

        history.append({'step':i+1,'current_node':current,'current_value':currentV,'neighbours':[{'x':nextnode,'value':nextv},{'x':nextnode2,'value':nextv2}]})
        if nextv>currentV:
            current=nextnode
            currentV=nextv
        elif nextv2>current:
            current=nextnode2
            currentV=nextv2
        else:
            break
        
        if currentV>bestvalue:
            bestnode=current
            bestvalue=currentV
    return bestnode,bestvalue,history

start=random.uniform(0,10)
best_x,best_v,his=hill_climbing(start)

print(f'bestnode:{best_x},best value:{best_v}')



    