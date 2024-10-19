def water_jug(x,y,z):
    visited=set()

    def dfs(jug1,jug2):

        print(f"({jug1},{jug2})")

        if (jug1,jug2)in visited:
            return False
        
        visited.add((jug1,jug2))

        if jug1==z or jug2==z or jug1+jug2==z:
            return True
        
        return (dfs(x,jug2) or
                dfs(jug1,y) or
                dfs(0,jug2) or
                dfs(jug1,0) or
                dfs(jug1-min(jug1,y-jug2),jug2+min(jug1,y-jug2)) or
                dfs(jug1+min(jug2,x-jug1),jug2-min(jug2,x-jug1)))
    
    return dfs(0,0)

jug1_capacity=3
jug2_capacity=5
target_amount=4

if water_jug(jug1_capacity,jug2_capacity,target_amount):
    print(f"Yes, it is possible to measure exactly {target_amount} liters")
else:
    print(f"No, it is not possible to measure exactly {target_amount} liters.")