/*
You've got a 5 × 5 matrix, consisting of 24 zeroes and a single number one. Let's index the matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by numbers from 1 to 5 from left to right. In one move, you are allowed to apply one of the two following transformations to the matrix:

Swap two neighboring matrix rows, that is, rows with indexes i and i + 1 for some integer i (1 ≤ i < 5).
Swap two neighboring matrix columns, that is, columns with indexes j and j + 1 for some integer j (1 ≤ j < 5).
You think that a matrix looks beautiful, if the single number one of the matrix is located in its middle (in the cell that is on the intersection of the third row and the third column). Count the minimum number of moves needed to make the matrix beautiful.

Input
The input consists of five lines, each line contains five integers: the j-th integer in the i-th line of the input represents the element of the matrix that is located on the intersection of the i-th row and the j-th column. It is guaranteed that the matrix consists of 24 zeroes and a single number one.

Output
Print a single integer — the minimum number of moves needed to make the matrix beautiful.

Examples
InputCopy
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
OutputCopy
3
InputCopy
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
OutputCopy
1

*/

#include <iostream>
using namespace std;

#include <vector>

int moves = 0;
vector<int> center(2,2);

vector<int> locate_num() {
    // location vector named position; initialized as vector of two integers, both zero.
    vector<int> position(2);

    // for each row
    for (int i = 0; i < 5; i++) {
        
        // for each column
        for (int j = 0; j < 5; j++) {
            // read value at pos (i, j)
            int value;
            cin >> value;

            if (value == 1) {
                position[0] = i;
                position[1] = j;
            }
        }
    }
    return position;
}

void calc_moves(vector<int> position) {
    int x_diff = abs(position[0] - center[0]);
    int y_diff = abs(position[1] - center[1]);
    moves = x_diff + y_diff;
}

int main() {
    // init position
    vector<int> pos = locate_num();

    // calculate minimum moves and output
    calc_moves(pos);
    cout << moves << endl;
    return 0;
}
