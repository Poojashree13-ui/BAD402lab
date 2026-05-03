import heapq
class Node:
    def _init_(self,state,parent=None,action=None,cost=0,heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic
    def _lt_(self,other):
        return(self.cost + self.heuristic) < (other.cost + other.heuristic)
def astar_search(initial_state,goal_test,successors,heuristic):
    frontier = []
    heapq.heappush(frontier,Node(initial_state,None,None,0,heuristic(initial_state)))
    explored = set()
    while frontier:
        current_node = heapq.heappop(frontier)
        current_state = current_node.state
        if goal_test(current_state):
            path = []
            while current_node.parent is not None:
                path.append((current_node.action,current_node.state))
                current_node = current_node.parent
            path.reverse()
            return path
        explored.add(current_state)
        for action,successor_state,step_cost in successors(current_state):
            if successor_state not in explored:
                new_cost = current_node.cost+step_cost
                new_node = Node(successor_state,current_node,action,new_cost,heuristic(successor_state))
                heapq.heappush(frontier,new_node)
    return None       
if _name_ == "_main_":
    start_state = "A"
    goal_state = "D"
    def goal_test(state):
        return state == goal_state
    def successors(state):
        if state == "A":
            return[("Move to B","B",1),("Move to C","C",3)]
        elif state == "B":
            return[("Move to A","A",1),("Move to C","C",1),("Move to D","D",2)]
        elif state == "C":
            return[("Move to A","A",3),("Move to B","B",1),("Move to D","D",1)]
        elif state == "D":
            return[("Move to B","B",2)]
        else:
            return[]
    def heuristic(state):
        heuristic_values = {"A": 3,"B": 2,"C": 1,"D": 0}
        return heuristic_values[state]
   
    path=astar_search(start_state,goal_test,successors,heuristic)
    if path:
        print("Path found")
        for action,state in path:
            print(f"Action: {action}, State: {state}")
    else:
        print("No path found.")