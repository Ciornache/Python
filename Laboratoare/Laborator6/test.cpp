#include <iostream>
#include <fstream>
#pragma warning(disable : 4996)
using namespace std;
int n, m, a[10][10], b[10][10], suma, i, j, cnt, uz[10][10];
const int di[] = {1, 0, -1, 0}, dj[] = {0, 1, 0, -1};
int inmat(int i, int j)
{
    return i >= 1 && j >= 1 && j <= m && i <= n;
}
pair<int, int> v[1001];
void afis()
{
    for (int i = 1; i <= suma; i++)
    {
        cout << v[i].first << ',' << v[i].second << " " << b[v[i].first][v[i].second] << endl;
    }
    cout << endl;
}
void back(int i, int j, int pas)
{
    for (int k = 0; k < 4; k++)
    {
        int iv = i + di[k], jv = j + dj[k];
        if (b[iv][jv])
        {
            b[iv][jv]--;
            if (inmat(iv, jv) && a[iv][jv])
            {
                v[pas] = make_pair(iv, jv);
                if (pas == suma)
                    cnt++; // afis();
                else
                    back(iv, jv, pas + 1);
            }
            b[iv][jv]++;
        }
    }
}
int main()
{
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> a[i][j], suma += a[i][j], b[i][j] = a[i][j];
    cin >> i >> j;
    b[i][j] = a[i][j] - 1;
    v[1] = make_pair(i, j);
    back(i, j, 2);
    if (cnt)
        cout << cnt;
    else
        cout << "Mr. Anderson wins!";
    return 0;
}