#include<iostream>
using namespace std;

int main(){
     // choosing a count variable 
     int n ;
     cin >> n;
    
     int sum =0;
     for(int counter=0; counter<=n; counter++){
         sum = sum + counter;
     } 

     cout << "The sum of n number is: " << sum << endl;
     return 0; 

}