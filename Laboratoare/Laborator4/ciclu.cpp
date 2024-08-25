#include <fstream>

int n, m, a, b, current;
int nr[1001], c[1001];
/// nr[i] - numarul de noduri a celei de a i-a componenta conexa
/// c[i] - componenta conexa a nodului i

bool mat[1001][1001], v[1001];

void dfs(int x)
{
    c[x] = current;
    nr[current]++;
    v[x] = 1;
    for(int i = 1;i <= n; i++)
        if(mat[x][i] && !v[i])
            dfs(i);
}

int main()
{
    std::ifstream cin("componenteconexe5.in");
    std::ofstream cout("componenteconexe5.out");
    cin >> n >> m;
    for(int i = 1;i <= m; i++)
        {
            cin >> a >> b;
            mat[a][b] = mat[b][a] = 1;
        }
    for(int i = 1;i <= n; i++)
        if(!v[i])
            current++, dfs(i);
    int q;
    cin >> q;
    while(q--)
    {
        int x;
        cin >> x;
        cout << nr[c[x]] << '\n';
    }
}