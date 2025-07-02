#include<iostream>
using namespace std;
long double fact(int n){
    long double fact;
    for(int i = 1;i<=n;i++)
    {
        fact= fact*i;    
    }
    return fact;
}
int main(){
    int num;
    cout<<"Enter number:";
    cin>>num;
    cout<<"The factorial is :"<<fact(num);
    
}
