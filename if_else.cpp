#include<iostream>
using namespace std;

int main()
{
    int savings;

    cin >> savings;

    if(savings > 5000)
    { 
        if(savings>10000){
            cout << "Roadtrip \n" << endl;
            }
        else{
            cout << "Shopping \n" << endl;
            }
    }
    else if (savings > 2000)
    { 
        cout << "Sydney \n" << endl;
    }
    else
    {
    cout << "Friends \n" << endl;
    } 
    
    return 0;
}
