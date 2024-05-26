#include <stdio.h>  
#include <stdlib.h>  
  
int find(int parent[], int i) {  
    if (parent[i] != i) {  
        parent[i] = find(parent, parent[i]);  
    }  
    return parent[i];  
}  
  
void unionSet(int parent[], int rank[], int i, int j) {  
    int irep = find(parent, i);  
    int jrep = find(parent, j);  
      
    if (irep != jrep) {  
        if (rank[irep] < rank[jrep]) {  
            parent[irep] = jrep;  
        } else if (rank[jrep] < rank[irep]) {  
            parent[jrep] = irep;  
        } else {  
            parent[irep] = jrep;  
            rank[jrep]++;  
        }  
    }  
}  
  
int main() {  
    int n, q;  
    scanf("%d %d", &n, &q);  
      
    int *p = (int *)malloc(2 * n * sizeof(int));  
    int *r = (int *)malloc(2 * n * sizeof(int));  
    for (int i = 0; i < 2 * n; i++) {  
        p[i] = i;  
        r[i] = 0;  
    }  
      
    for (int i = 0; i < q; i++) {  
        int s, a, b;  
        scanf("%d %d %d", &s, &a, &b);  
        //if friends
        if (s == 0) {  
            if (find(p, a) == find(p, b + n)) {  
                printf("NO\n");  
            } else {  
                printf("YES\n");  
                unionSet(p, r, a, b);  
                unionSet(p, r, a + n, b + n);  
            }  
        } else {  //if enemies
            if (find(p, a) == find(p, b)) {  
                printf("NO\n");  
            } else {  
                printf("YES\n");  
                unionSet(p, r, a, b + n);  
                unionSet(p, r, a + n, b);  
            }  
        }  
    }  
      
    int *sizes = (int *)calloc(2 * n, sizeof(int));  
    for (int i = 0; i < n; ++i) {  
        sizes[find(p, i)]++;  
    }  
      
    int read[2 * n];  
    for (int i = 0; i < 2 * n; i++) {  
        read[i] = 0;  
    }  
    int maximum = 0;  
    for (int i = 0; i < n; ++i) {  
        int e = find(p, i);  
          
        if (!read[e]) {  
            int r1 = find(p, i + n);  
              
            if (sizes[r1] > sizes[e]) {  
                maximum += sizes[r1];  
            } else {  
                maximum += sizes[e];                      
            }  
            read[r1] = 1;  
            read[e] = 1;  
        }  
    }  
    printf("%d\n", maximum);  
      
    free(p);  
    free(r);  
    free(sizes);  
      
    return 0;  
}  
