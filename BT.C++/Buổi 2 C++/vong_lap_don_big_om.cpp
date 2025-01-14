#include <iostream>
using namespace std;

void pritNumbers(int n){
    for(int i = 1; i <= n; i++){
        cout << i << " ";
    }
    cout << endl; 
}
int main(){
    int n = 5;
    pritNumbers(n);
    return 0;
}