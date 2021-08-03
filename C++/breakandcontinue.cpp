#include<iostream>
using namespace std;

int main(){

int Pocketmoney=3000;
    for(int date=1; date<=31; date++){
        
        if(date%2==0){
            continue;
        }
        if(Pocketmoney==0){
            break;
        }

        cout<<"Go out today"<<endl;
        Pocketmoney = Pocketmoney - 300;
        
        
    }
    return 0;
}

