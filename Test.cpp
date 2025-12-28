#include <iostream>
#include <list>
using namespace std;

int main() {
    // Create a list of integers
    list<char> myList = { 'W', 'B', 'W', 'W', 'R', 'G', 'Y', 'W'};
    char x;

    // Display elements
    cout << "List elements: ";
    for (char n : myList)
    {
        x = myList[n];
        if (x == 'B') {
            cout << n << " ";
            question(x); 
        } else if (x == 'R') {
            cout << n << " ";
        } else if (x == 'G') {
            cout << n << " ";
        } else if (x == 'Y') {
            cout << n << " ";
        } else if (x == 'W') {
            cout << n << " ";
        }
    }
    cout << endl;

    return 0;
}

int randomNumber(int low, int high) {
    return low + (rand() % (high - low + 1));
}

int question(char x) {
    int low = randomNumber(1, 9);
    int high = randomNumber(1, 9);
    int move = randomNumber(4, 6);
    int answer;
    
    if (x == 'B') {
        cout << " What is " << low << " + " << high;
        cin >> answer;
        
        if (answer == (low + high)) {
            cout << "Correct! You can move up " << move << " spaces.";
        } else {
            cout << "Sorry...";
        }
    } else if (x == 'R') {
        cout << "What is " << low << " - " << high;
        cin >> answer;
        
        if (answer == (low + high)) {
            cout << "Correct";
        } else {
            cout << "Sorry... You can move back " << move << " spaces.";
        }
    } else if (x == 'G') {
        cout << "What is " << low << " * " << high;
        cin >> answer;
        
        if (answer == (low * high)) {
            cout << "Correct! You can move up " << move << " spaces.";
        } else {
            cout << "Sorry...";
        }
    } else if (x == 'Y') {
        cout << " What is " << high << " / " << low;
        cin >> answer;
        
        if (answer == (high / low)) {
            cout << "Correct";
        } else {
            cout << "Sorry...";
        }
    } else if (x == 'W') {
        cout << "Nothing to answer here.";
    }
}