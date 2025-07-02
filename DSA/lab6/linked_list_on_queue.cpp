#include<iostream>
using namespace std;
class Node{
    public:
    Node* next;
    int data;
    
    Node(int val){
        data = val;
        next = NULL;
    }
};

void insertAtTail(Node* &head,int val)
{
    Node* newnode = new Node(val);
    if (head == NULL) { 
        head = newnode;
        return;
    }
    Node* temp = head;
    while(temp->next != NULL)
    {
        temp= temp->next;
    }
    temp->next = newnode;
}
void deleteAtHead(Node* &head)
{
    if (head == NULL) {
        cout << "Queue is already empty!" << endl;
        return;
    }
    Node* temp = head;
    head = head->next;
    delete temp;
}
void enqueue(Node* &head,int val){
    insertAtTail(head,val);
}
void dequeue(Node* &head){
    deleteAtHead(head);
}
void display(Node* &head){
    Node* temp = head;
    cout<<"Queue (from Front to Rear): ";
    while(temp != NULL){
        cout<<"|"<<temp->data<<"|"<<"->";
        temp = temp->next;
    }
    cout<<"NULL"<<endl;
}

int main(){
    Node* head = NULL;
    enqueue(head, 3);
    display(head);
    enqueue(head, 4);
    display(head);
    dequeue(head);
    display(head);
    dequeue(head);
    dequeue(head);
    enqueue(head, 6);
    display(head);
}
