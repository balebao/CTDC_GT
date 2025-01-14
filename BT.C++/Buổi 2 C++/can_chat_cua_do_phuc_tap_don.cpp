#include <iostream>
using namespace std;
int sum_1_to_n(int n){
    int s = 0;
    for(int i = 1; i <= n; i++){
        s += i; 
    }
    return s;
}
int main(){
    int n = 5;
    cout << " tong 1..n = " << sum_1_to_n(n) << endl;
    return 0;
}