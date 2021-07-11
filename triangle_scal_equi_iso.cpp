#include<iostream>
using namespace std;

int main(){
    int side1,side2,side3;

    cin >> side1 >> side2 >> side3;

    if(side1 == side2)
    {
        if (side2 == side3)
        {
            cout << "The triangle is equilateral triangle" << endl;
        }
        else{
            cout << "the triangle is isoceless triangle" << endl;
        }
    }
    else{
        if((side2 == side3) || (side1 == side3)){
            cout << "the triangle is isoceless triangle" << endl;
        }
        else{
            cout << "The triangle is scalene triangle" << endl;
        }
    }
}