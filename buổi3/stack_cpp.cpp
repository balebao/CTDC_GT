#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    stack<string> stack;

    // Push cac phan tu vao ngan xep
    stack.push("Sach A");
    cout << "Da them 'Sach A' vao ngan xep." << endl;

    stack.push("Sach B");
    cout << "Da them 'Sach B' vao ngan xep." << endl;

    stack.push("Sach C");
    cout << "Da them 'Sach C' vao ngan xep." << endl;

    // Hien thi phan tu o dinh ngan xep
    cout << "Phan tu o dinh ngan xep: " << stack.top() << endl;

    // Pop phan tu khoi ngan xep
    stack.pop();
    cout << "Da lay phan tu ra khoi ngan xep." << endl;

    // Hien thi phan tu o dinh ngan xep sau khi pop
    cout << "Phan tu o dinh ngan xep sau khi pop: " << stack.top() << endl;

    // Kiem tra ngan xep co trong khong
    if (stack.empty()) {
        cout << "Ngan xep trong!" << endl;
    } else {
        cout << "Ngan xep khong trong." << endl;
    }

    return 0;
}
