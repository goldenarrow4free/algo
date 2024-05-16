class UnionFind:  
    def __init__(self, n):  
        self.parent = list(range(2 * n))  
        self.rank = [1] * (2 * n)  
  
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
  
def main():   
      
    n, q = map(int, input().split())  
    uf = UnionFind(n)  
      
    index = 2  
    results = []  
      
    for _ in range(q):  
        s, a, b = map(int, input().split())  
        index += 3  
  
        if s == 0:  # Friends  
            if uf.find(a) == uf.find(b + n) or uf.find(a + n) == uf.find(b):  
                results.append("NO")  
            else:  
                uf.union(a, b)  
                uf.union(a + n, b + n)  
                results.append("YES")  
        else:  # Enemies  
            if uf.find(a) == uf.find(b) or uf.find(a + n) == uf.find(b + n):  
                results.append("NO")  
            else:  
                uf.union(a, b + n)  
                uf.union(a + n, b)  
                results.append("YES")  
      
    print("\n".join(results))  
      
    max_size = 0  
    component_size = [0] * (2 * n)  
      
    for i in range(n):  
        root = uf.find(i)  
        component_size[root] += 1  
      
    for i in range(n):  
        max_size = max(max_size, component_size[uf.find(i)])  
      
    print(max_size)  
  