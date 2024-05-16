class UnionFind:  
    def __init__(self, n):  
        self.parent = list(range(n))  
        self.rank = [1] * n  
        self.enemy = [-1] * n  
  
    def find(self, x):  
        if self.parent[x] != x:  
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]  
  
    def union(self, x, y):  
        rootX = self.find(x)  
        rootY = self.find(y)  
        if rootX != rootY:  
            if self.rank[rootX] > self.rank[rootY]:  
                self.parent[rootY] = rootX  
            elif self.rank[rootX] < self.rank[rootY]:  
                self.parent[rootX] = rootY  
            else:  
                self.parent[rootY] = rootX  
                self.rank[rootX] += 1  
            return True  
        return False  
  
    def set_enemy(self, x, y):  
        rootX = self.find(x)  
        rootY = self.find(y)  
        if self.enemy[rootX] == -1:  
            self.enemy[rootX] = rootY  
        else:  
            self.union(self.enemy[rootX], rootY)  
        if self.enemy[rootY] == -1:  
            self.enemy[rootY] = rootX  
        else:  
            self.union(self.enemy[rootY], rootX)  
  
def process_gossips(n, q, gossips):  
    uf = UnionFind(n)  
    results = []  
    for s, a, b in gossips:  
        if s == 0:  
            if uf.find(a) == uf.find(b) or uf.enemy[uf.find(a)] != uf.find(b):  
                results.append("YES")  
                uf.union(a, b)  
            else:  
                results.append("NO")  
        else:  
            if uf.find(a) != uf.find(b) and (uf.enemy[uf.find(a)] == -1 or uf.enemy[uf.find(a)] != uf.find(b)):  
                results.append("YES")  
                uf.set_enemy(a, b)  
            else:  
                results.append("NO")  
      
    # Determine the size of the largest amicable group  
    group_size = {}  
    largest_group = 0  
      
    for i in range(n):  
        root = uf.find(i)  
        if root not in group_size:  
            group_size[root] = 0  
        group_size[root] += 1  
        largest_group = max(largest_group, group_size[root])  
      
    return results, largest_group  
  
# Reading input  
import sys  
input = sys.stdin.read  
data = input().split()  
n, q = int(data[0]), int(data[1])  
gossips = [(int(data[i]), int(data[i+1]), int(data[i+2])) for i in range(2, len(data), 3)]  
  
results, largest_group = process_gossips(n, q, gossips)  
  
# Output results  
for res in results:  
    print(res)  
print(largest_group)  
