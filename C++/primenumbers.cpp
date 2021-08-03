#include<iostream>
using namespace std;

int main(){

    int n;
    cin>>n; //User input to start the program 

    //Initializing the count variable //Declaring outside for the very reason, if the loop breaks then the scope of the initialized variable will not be utilized 
    int i; //count variable
    for(i=2 ; i<n ; i++){
        if(n%i==0){
            cout<<"Non Prime"<<endl;
            break;
        }
    }

    if(i==n){
        cout<<"Prime"<<endl;
    }
    
    return 0;

}