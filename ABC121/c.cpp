#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll N, M;
    cin >> N >> M;
    vector<vector<ll>> AB(N, vector<ll>(2));
    for (ll i = 0; i < N; i++) cin >> AB.at(i).at(0) >> AB.at(i).at(1);
    sort(AB.begin(), AB.end());
    ll ans = 0;
    for (ll i = 0; i < N; i++) {
        ll a = AB.at(i).at(0);
        ll b = AB.at(i).at(1);
        if (M <= b) {
            ans += a * M;
            break;
        } else {
            ans += a * b;
            M -= b;
        }
    }
    cout << ans << endl;
}