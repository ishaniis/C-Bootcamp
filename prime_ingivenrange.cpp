#include<iostream>
using namespace std;

int main(){
    int a , b;
    cout<<"The input range a is:" << endl;
    cin>>a;
    cout << "the input range b is:"<< endl;
    cin >>b;

    int j;
    for(int num=a ; num<=b ; num++){
        for(j=2 ; j<num ; j++){
            if(num%j==0){
                cout<<"This number "<< num << " is not prime"<<endl;
                break;
            }
        }
        if (j==num){
            cout<<"The number "<<num<<" is prime"<<endl;
        }
    }
    return 0;
}