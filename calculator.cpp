#include<iostream>
using namespace std;


int main(){
    int input_1, input_2;
    char input_3;
    
    cout<<"What's your input A? : "<<endl;
    cin>>input_2 >> input_1;
    
    cout<<"What is the operation you would like to proceed with? : ";
    cin>>input_3;

    switch(input_3){
        case '+':
        cout<<"The result of the computation is: " << input_2 + input_1 << endl;
        break;

        case '*':
        cout<<"The result of the computation is: " << input_2 * input_1 << endl;
        break;

        case '-':
        if(input_1>input_2){
            cout<<"The result of the computation is: " << input_1 - input_2 << endl;
        }
        else{
            cout<<"The result of the computation is: " << input_2 - input_1 << endl;
        }

        case '/':
        cout<<"The result of the computation is: " << input_2 / input_1 << endl;
        break;

        default:
        cout<<"Invalid Operation"<<endl;
        break;        
    }

    return 0;

}