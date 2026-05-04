#include <iostream>
#include <list>
#include <cmath>
#include <string>
using namespace std;

int randomNumber(int low, int high);
void question(char x);
void rules();

int main() {
    rules();
    
    // Create a list of integers
    list<char> myList = {'B', 'W', 'W', 'W', 'W', 'W', 
                         'W', 'W', 'B', 'W', 'B', 'G', 'W', 'W', 'Y', 
                         'B', 'W', 'W', 'W', 'Y', 'R', 'W', 
                         'W', 'W', 'G', 'B', 'P', 'B', 'W', 'W', 'W', 'M', 'B', 'R', 'Y', 'W', 'B', 'G', 'Y', 'W', 
                         'W', 'B', 'R', 'M', 'W', 'G', 
                         'W', 'B', 'G', 'W', 'B', 'W', 'B', 'Y', 'W', 'W', 
                         'W', 'B', 'G', 'W', 'W', 'B', 'W', 'Y', 'R', 'W', 'P', 'Y', 'W', 'W', 'W', 'Y', 'R', 'W', 'W', 'M', 'W', 'W', 'B', 'G', 'Y', 'R', 'W', 'W', 'W', 'W', 'W', 'R', 'B', 'M', 'W', 'W', 'W', 'P', 'W', 'W', 'W', 'R', 'Y', 'W', 'E'};

    // Display elements
    for (char n : myList) {
        if (n == 'B') {
            cout << n << " ";
            question(n); 
        } else if (n == 'R') {
            cout << n << " ";
            question(n); 
        } else if (n == 'G') {
            cout << n << " ";
            question(n); 
        } else if (n == 'Y') {
            cout << n << " ";
            question(n);
        } else if (n == 'E') {
            cout << n << " Congradulations! You have completed the board. Feel free to play again and improve your math skills. ";
            break;  
        } else {
            // if n == W
            cout << n << " ";
        }
    }
    cout << endl;

    return 0;
}

void rules() {
    cout << "HELLO! WELCOME TO BIOLOGY ISLAND. IN CASE IF YOU ARE WONDERING, YES. \nTHIS IS BASICALLY BOARD GAME ISLAND FROM WII PARTY. \nDO YOU WANT TO KNOW THE RULES? (TYPE YES OR NO) ";
    string responce;
    cin >> responce;
    if ((responce == "YES") || (responce == "Yes") || (responce == "yes")) {
        cout << "OKAY! HERE ARE THE RULES: \n1. YOU WILL ROLL A DICE TO DETERMINE HOW MANY SPACES YOU WILL MOVE. \n2. EACH SPACE HAS A COLOR THAT WILL DETERMINE WHAT TYPE OF MATH QUESTION YOU WILL GET. \n3. IF YOU ANSWER THE QUESTION CORRECTLY, YOU WILL EITHER GET TO MOVE FORWARD OR STAY WHERE YOU ARE. \n4. IF YOU ANSWER THE QUESTION INCORRECTLY, YOU WILL EITHER STAY WHERE YOU ARE OR HAVE TO MOVE BACKWARDS. \n5. THE GAME ENDS WHEN YOU REACH THE END OF THE BOARD. GOOD LUCK!\n\n";
    } else if ((responce == "NO") || (responce == "No") || (responce == "no")) {
        cout << "OKAY THEN, LET'S PLAY BIOLOGY ISLAND!\n\n";
    } else {
        cout << "I'M SORRY, I DIDN'T UNDERSTAND THAT. I GUESS YOU DON'T WANT TO KNOW THE RULES. \nLET'S PLAY BIOLOGY ISLAND!\n\n";
    }
}

int randomNumber(int low, int high) {
    return low + (rand() % (high - low + 1));
}

void question(char x) {
    int low = randomNumber(1, 9);
    int high = randomNumber(1, 9);
    int move = randomNumber(4, 6);
    int answer;
    
    if (x == 'B') {
        cout << " What is " << low << " + " << high << " ";
        cin >> answer;
        
        if (answer == (low + high)) {
            cout << "Correct! You can move up " << move << " spaces.\n";
        } else if (answer == 1721920) {
            return;
        } else {
            cout << "Sorry...";
        }
    } else if (x == 'R') {
        cout << "What is " << low << " - " << high << " ";
        cin >> answer;
        
        if (answer == (low + high)) {
            cout << "Correct";
        } else if (answer == 1721920) {
            return;
        } else {
            cout << "Sorry... You'll have to move back " << move << " spaces.\n";
        }
    } else if (x == 'G') {
        cout << "What is " << low << " * " << high << " ";
        cin >> answer;
        
        if (answer == (low * high)) {
            cout << "Correct! You can move up 10 spaces.\n";
        } else if (answer == 1721920) {
            return;
        } else {
            cout << "Sorry...";
        }
    } else if (x == 'Y') {
        cout << " What is " << high << " / " << low << " ? (Round to the nearest whole number) ";
        cin >> answer;
        
        if (answer == round((high / low))) {
            cout << "Correct You can move up " << move << " spaces.\n";
        } else if (answer == 1721920) {
            return;
        } else {
            cout << "Sorry... You'll have to move back " << move << " spaces.\n";
        }
    } // else if (x == 'W') {
    //     cout << "Nothing to answer here.";
    // }
}