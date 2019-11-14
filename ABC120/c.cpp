#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    string S;
    cin >> S;
    vector<int> t(0);
    ll ans = 0;
    for (int i = 0; i < S.size(); i++) {
        if (t.size() != 0 && t.at(t.size()-1) != S.at(i)) {
            t.pop_back();
            ans += 2;
        } else {
            t.push_back(S.at(i));
        }
    }
    cout << ans << endl;
}