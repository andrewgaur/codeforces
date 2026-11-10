#include <iostream>
using namespace std;
#include <string>
#include <vector>

void abbrev(const string& s) {
    vector<char> chars(s.begin(), s.end());
    if (chars.size() > 10) {
        cout << chars.front() << chars.size() - 2 << chars.back() << '\n';
    } else {
        cout << s << '\n';
    }
}


int main() {
    int n;
    cin >> n;
    for (int i = 0; i<n; ++i) {
        string s;
        cin >> s;
        abbrev(s);
    }
    return 0;
}