#include <cstdio>
#include <tuple>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;
using pp = pair<int, int>;

const int N_MAX = (int)1e5;

int n, m, treeNum;
bool visited[N_MAX + 1];
bool isLeaf[N_MAX + 1];

vector<pp> edges[N_MAX + 1];
vector<int> treeNodes[N_MAX + 1];
vector<int> treeEdges[N_MAX + 1];

void go(int now, int idx){
    visited[now] = true;
    treeNodes[idx].push_back(now);
    bool leaf = true;
    for (pp e: edges[now]){
        int next = e.first;
        int edgeNum = e.second;
        if (!visited[next]){
            treeEdges[idx].push_back(edgeNum);
            leaf = false;
            go(next, idx);
        }
    }
    isLeaf[now] = leaf;
    
    return;
}

void print(vector<int> v){
    sort(v.begin(), v.end());
    for (int x: v){
        printf("%d ", x);
    }
    printf("\n");
}

int main(){
    scanf("%d %d", &n, &m);
    
    for (int i = 1; i <= m; i++){
        int u, v; scanf("%d %d", &u, &v);
        edges[u].push_back({v, i});
        edges[v].push_back({u, i});
    }
    
    for (int i = 1; i <= n; i++){
        if (!visited[i]){
            go(i, treeNum);
            treeNum += 1;
        }
    }
    
    // 이미 그래프가 세 개 이상의 부분으로 분리되어 있으면
    if (treeNum > 2){
        printf("-1\n");
        return 0;
    }
    
    int startV = 0, selected = 0;
    
    // 그래프를 두 개의 트리로 분래해야 하면
    if (treeNum < 2){
        // 리프 노드 하나 골라서 분리
        for (int x: treeNodes[0]){
            if (isLeaf[x]){
                selected = x;
            }
            else {
                startV = x;
            }
        }
        
        treeNodes[0].clear();
        treeEdges[0].clear();
        memset(visited, false, sizeof(visited));
        visited[selected] = true;
        go(startV, 0);
        
        treeNodes[1].push_back(selected);
    }
    
    
    if ((int)treeNodes[0].size() == (int)treeNodes[1].size()){
        printf("-1\n");
        return 0;
    }
    printf("%d %d\n", (int)treeNodes[0].size(), (int)treeNodes[1].size());
    
    print(treeNodes[0]);
    print(treeEdges[0]);
    
    print(treeNodes[1]);
    print(treeEdges[1]);
    
    return 0;
}
