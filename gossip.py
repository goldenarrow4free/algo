class DisjointSet:  
    def __init__(self, n):  
        self.parent = list(range(n))  
        self.rank = [0] * n  
        self.size = [1] * n  # Each set initially has one element  
  
    def find(self, x):  
        if self.parent[x] != x:  
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]  
  
    def union(self, x, y):  
        xroot = self.find(x)  
        yroot = self.find(y)  
        if xroot != yroot:  
            if self.rank[xroot] < self.rank[yroot]:  
                xroot, yroot = yroot, xroot  
            self.parent[yroot] = xroot  
            if self.rank[xroot] == self.rank[yroot]:  
                self.rank[xroot] += 1  
            self.size[xroot] += self.size[yroot]  
            self.size[yroot] = 0  
        return xroot  
  
n, q = map(int, input().split())  
friends_ds = DisjointSet(n)  
enemies = [set() for _ in range(n)]  
  
for _ in range(q):  
    s, a, b = map(int, input().split())  
    if s == 0:  # Friends  
        if b in enemies[a]:  # Inconsistent gossip  
            print("NO")  
        else:  
            # Merge the two sets of friends and their enemies  
            aroot = friends_ds.find(a)  
            broot = friends_ds.find(b)  
            if aroot != broot:  
                for enemy in enemies[aroot] | enemies[broot]:  
                    enemies[friends_ds.union(a, b)].add(enemy)  
                enemies[aroot].clear()  
                enemies[broot].clear()  
            print("YES")  
    else:  # Enemies  
        if friends_ds.find(a) == friends_ds.find(b):  # Inconsistent gossip  
            print("NO")  
        else:  
            enemies[friends_ds.find(a)].add(friends_ds.find(b))  
            enemies[friends_ds.find(b)].add(friends_ds.find(a))  
            print("YES")  
  
largest_amicable_group = max(friends_ds.size)  
  
print(largest_amicable_group)  
