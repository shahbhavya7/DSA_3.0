#include <iostream>
using namespace std;

int main() {
    int n = 4;

    // Upper part
    for (int i = 1; i <= n; i++) {

        // spaces
        for (int j = 1; j <= n - i; j++)
            cout << " ";

        // increasing numbers
        for (int j = 1; j <= i; j++)
            cout << j;

        // decreasing numbers
        for (int j = i - 1; j >= 1; j--)
            cout << j;

        cout << endl;
    }

    // Lower part
    for (int i = n; i >= 1; i--) {

        for (int j = 1; j <= n - i; j++)
            cout << " ";

        for (int j = 1; j <= i; j++)
            cout << j;

        for (int j = i - 1; j >= 1; j--)
            cout << j;

        cout << endl;
    }

    return 0;
}
