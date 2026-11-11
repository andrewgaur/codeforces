#include <iostream>
using namespace std;

#include <string>
int x = 0;

void execute() {
    string input_current;
    cin >> input_current;
    if (input_current.find("++") != string::npos) {
        x++;
    } else if (input_current.find("--") != string::npos) {
        x--;
    }
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        execute();
    }

    cout << x;
    return 0;
}