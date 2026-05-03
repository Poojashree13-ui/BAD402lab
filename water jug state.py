class WaterJugState:
    def _init_(self,jug1,jug2):
       self.jug1=jug1
       self.jug2=jug2
    def _eq_(self,other):
        return self.jug1==other.jug1 and self.jug2==other.jug2
    def _hash_(self):
        return hash((self.jug1,self.jug2))
def dfs(current_state,visited,jug1_capacity,jug2_capacity,target_volume):
    if current_state.jug1==target_volume or current_state.jug2==target_volume :
        if current_state.jug1==target_volume:
            print("Jug1 now has",target_volume,"liters")
        else:
            print("Jug2 now has",target_volume,"liters")
        return True
    visited.add(current_state)
    operations=[
               ('Fill Jug1',jug1_capacity,current_state.jug2),
               ('Fill Jug2',current_state.jug1,jug2_capacity),
               ('Empty Jug1',0,current_state.jug2),
               ('Empty Jug2',current_state.jug1,0),
               ('Pour Jug1 to Jug2',
                max(0,current_state.jug1+current_state.jug2-jug2_capacity),
                min(jug2_capacity,current_state.jug1+current_state.jug2)),
               ('Pour Jug2 to Jug1',
                min(jug1_capacity,current_state.jug1+current_state.jug2),
                max(0,current_state.jug1+current_state.jug2-jug1_capacity))
               ]
    for operation in operations:
        action,new_jug1,new_jug2=operation
        new_state=WaterJugState(new_jug1,new_jug2)
        if new_state not in visited:
            print(f"Trying:{action}=>({new_jug1},{new_jug2})")
            if dfs(new_state,visited,jug1_capacity,jug2_capacity,target_volume):
                return True
    return False
def solve_water_jug_problem(jug1_capacity,jug2_capacity,target_volume):
    initial_state=WaterJugState(0,0)
    visited=set()
    if dfs (initial_state,visited,jug1_capacity,jug2_capacity,target_volume):
        print("solution found!")
    else:
        print("Solution not possible")
jug1_capacity=int(input("Enter Jug1 capacity:"))
jug2_capacity=int(input("Enter Jug2 capacity:"))
target_volume=int(input("Enter target volume:"))
print(f"Solving Water Jug Problem with capacities({jug1_capacity},{jug2_capacity})to measure{target_volume}liters")
solve_water_jug_problem(jug1_capacity,jug2_capacity,target_volume)