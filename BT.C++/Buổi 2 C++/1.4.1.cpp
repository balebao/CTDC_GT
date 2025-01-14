#include <iostream>
using namespace std;

int sum_1_to_n(int n){
    int s = 0;
    for(int i = 1; i <= n ;i++){
        s += i;
    }
    return s;
}
int main(){
    cout <<" nhap n: ";
    int n;
    cin >> n;
    int result = sum_1_to_n(n);
    cout << "tong 1..n = " << result << endl;
}

