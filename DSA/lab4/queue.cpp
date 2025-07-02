#include<iostream>
#define MAX 5
using namespace std;
template<class T>
class Queue{
    T data[MAX];
    int f,r;
    public:
    Queue():f(-1),r(-1){}
    void Enqueue( T value)
    {
        if(r==MAX-1){
            cout<<"Queue Overflow!"<<endl;
            return;
        }
        else if(f==-1 &&r==-1){
            f=r=0;
        }
        else{
            r++;
        }
        data[r]= value;
    }
    T Dequeue(){
        if (f==-1 || f > r){
            cout<<"Queue is Empty."<<endl;
            return 1;
        }
        else{
            T val = data[f];
            f = f+1;
            return val;
        }
    }
    void Display(){
        if(f == -1 || f>r){
            cout<<"Queue is empty."<<endl;
            return;
        }
        for(int i=f;i<=r;i++){
            cout<<data[i]<<" ";
        }
        cout<<endl;
    }
};
int main(){
    Queue<int>q;
    q.Enqueue(10);
    q.Enqueue(12);
    q.Enqueue(14);
    q.Enqueue(16);
    q.Enqueue(18);
    q.Display();
    q.Dequeue();
    q.Dequeue();
    q.Display();
    return 0;
}
