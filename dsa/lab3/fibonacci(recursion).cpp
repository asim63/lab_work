#include<iostream>
using namespace std;
int fibonacci(int n){
    if (n==0 || n==1){
        return n;
    }
    else{
        return fibonacci(n-1)+fibonacci(n-2);
    }
}
int main(){
    int num;
    cout<<"Enter no of terms in series:";
    cin>>num;
    cout<<"The fibonacci series is :";
    for(int i=0; i <= num -1; i++)
    {
        cout<<fibonacci(i) << " ";
    }
}
