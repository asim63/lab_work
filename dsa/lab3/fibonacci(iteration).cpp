#include<iostream>
using namespace std;

int main(){
    int a = 0;
    int  b = 1,c;
    int num;
    cout<<"Enter no of terms in series more than 2:";
    cin>>num;
    cout<<"The fibonacci series is :";
    cout<<a<<" " << b <<" ";
   
    for(int i=1; i <= num -2; i++)
    {   
        c =a+b;
        a= b;
        b = c;
        cout<< c<< " ";
    }
};
