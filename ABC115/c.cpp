#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll N, K;
    cin >> N >> K;
    vector<ll> H(N);
    for (int i = 0; i < N; i++) cin >> H.at(i); 
    sort(H.rbegin(), H.rend());

    vector<ll> ans(0);
    for (int i = 0; i < N; i++) {
        if (N > i+K-1) {
            ans.push_back(H.at(i) - H.at(i+K-1));
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.at(0) << endl;
}