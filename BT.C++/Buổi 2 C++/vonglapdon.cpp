#include <iostream>
using namespace std;

    void printNumbers(int n){
        for(int i = 1; i <= n ; i++){
            cout << i << " ";
        }
        cout << endl;
    }
    int main(){
        int n = 5;
        printNumbers(n);
        return 0;
    }
