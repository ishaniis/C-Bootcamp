   // for loop practice
   #include<iostream>
   using namespace std;

   int main(){

       int input_number;
       cin>>input_number;

       int sum;
       //initializing the counter variable before though it can be done in the for block too
       int count;
       for(count = 0 ; count<=input_number ; count++){
           sum = sum + count;
       }
       cout<<sum<<endl;
       return 0;
   }