#include<iostream>
#define N 3
using namespace std;
int buffer[3];
int tos = -1;

typedef int semaphore;
semaphore full = 0;
semaphore empty = N;
semaphore mutex = 1;
int down(semaphore *s){
    if(*s>0){
        (*s)--;
        return 1;
    }else{
        return 0;
    }
}
void up(semaphore *s){
    (*s)++;
}
int produce_item(){
    int item;
    cout<<"Enter the item: "<<endl;
    cin>>item;
    return item;
}
void insert_item(int item){
    tos ++;
    buffer[tos] = item;
}
int delete_item(){
    int item;
    item = buffer[tos];
    tos--;
    return item;
}
void consume_item(int item){
    cout<<"Consumed item is: "<<item<<endl;
}
void producer(void){
    int item;
    item = produce_item();
    if(down(&empty)){
        down(&empty);
        insert_item(item);
        up(&mutex);
        up(&full);
    }
    else{
        cout<<"Buffer is full"<<endl;
    }
}
void consumer(void){
    int item;
    if(down(&full)){
        down(&mutex);
        item = delete_item();
        up(&mutex);
        up(&empty);
        consume_item(item);
    }else{
        cout<<"Buffer is empty"<<endl;
    }
}
int main(){
    int choice;
    while(1){
        cout<<"Enter 1 to produce: "<<endl<<"Enter 2 to consume: "<<endl;
        cin>>choice;
        switch(choice){
            case 1:
                producer();
                break;
            case 2:
                consumer();
                break;
            default:
                cout<<"Invalid Choice."<<endl;
                break;
        }
    }
    return 0;
}



