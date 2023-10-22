clothes = [int(x) for x in input().split(" ")]  
raft_capacity = int(input()) 

raft_used = 0  
current_raft_load = 0  

for cloth in clothes:
    if current_raft_load + cloth <= raft_capacity:
        current_raft_load += cloth  
    else:
        raft_used += 1  
        current_raft_load = cloth  
raft_used += 1 

print(raft_used)
