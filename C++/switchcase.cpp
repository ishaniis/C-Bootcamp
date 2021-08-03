#include<iostream>
using namespace std;

int main(){
    // initializing the variables required
    char button;
    cout<<"Please press the button as per your choice: ";
    cin>>button;
    
    switch(button){
        case 'a':
        cout<<"Heya" << endl ;
        break;
        case 'b':
        cout << "Hello" << endl;

        default:
        cout << "I guess it didn't worked out well for you! Sorry for the inconvenience!" << endl;
        break;
    }

    return 0;
}