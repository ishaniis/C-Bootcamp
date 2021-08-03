#include<iostream>
using namespace std;

int main(){

    int n;
    cin >> n;
    // at least it'll execute for first time and then it'll depend
    do{
        cout << n << endl;
    }
    while(n>0);
    return 0;
}