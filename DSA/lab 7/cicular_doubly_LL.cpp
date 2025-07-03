#include<iostream>
using namespace std;
int size =0;
class Node{
    public:
    int data;
    Node *next;
    Node *prev;
    
    Node(int val):data(val),next(this),prev(this){}
};
int getsize(){
    return size;
}
void insertAtHead(Node* &head, int val){
    Node* newnode = new Node(val);
    if(head == NULL)
    {
       head = newnode;
       size++;
       return;
    }
    Node* tail = head->prev;
    head->prev = newnode;
    newnode->next = head;
    newnode->prev = tail;
    tail->next = newnode;
    head = newnode;
    size++;
}
void insertAtTail(Node* &head, int val){
    Node* tail = head->prev;
    Node* newnode = new Node(val);
    head->prev = newnode;
    newnode->prev = tail;
    tail->next = newnode;
    newnode->next = head;
    tail = newnode;
    size++;
}
void insertAtPosition(Node* &head, int val, int pos){
    int i = getsize();
    Node* newnode = new Node(val);
    Node* temp = head;
    if(pos == 0){
        insertAtHead(head,val);
        return;
    }
    if(pos >=i){
        insertAtTail(head,val);
        return;
    }
    int curr_pos = 0;
    while(curr_pos != pos-1){
        temp = temp->next;
        curr_pos++;
    }
    newnode->next = temp->next;
    newnode->prev = temp;
    temp->next = newnode;
    size++;
}
void updateAtPosition(Node* &head,int val, int pos){
    Node*temp = head;
    if(head == NULL)
    {
        cout<<"The list is empty."<<endl;
        return;
    }
    int curr_pos=0;
    while(curr_pos != pos){
        temp = temp->next;
        curr_pos++;
    }
    temp->data = val;
}
void deleteAtHead(Node* &head){
    Node* tail = head->prev;
    Node* temp = head;
    if(head == NULL)
    {
        cout<<"The list is empty."<<endl;
        return;
    }
    tail->next = temp->next;
    head->next->prev = tail;
    head = head->next;
    delete temp;
    size--;
}
void deleteAtTail(Node* &head){
    if(head == NULL)
    {
        cout<<"The list is empty."<<endl;
        return;
    }
    Node* temp = head -> prev;
    head -> prev = temp -> prev;
    temp -> prev -> next = head;
    delete temp;
    size--;
}
void deleteAtPosition(Node* &head,int pos){
    Node* prev = head;
    int i = getsize();
    if(pos == 0){
        deleteAtHead(head);
        return;
    }
    if(pos > i ){
        cout<<"Limit Reached."<<endl;
        return;
    }
    int curr_pos =0;
    while(curr_pos != pos-1)
    {
        prev = prev->next;
        curr_pos++;
    }
    Node* temp = prev->next;
    prev->next = temp ->next;
    temp->next->prev = temp->prev;
    delete temp;
    size--;
}
void display(Node* &head){
    if (head == NULL) {
        cout << "List is empty." << endl;
        return;
    }
    Node* temp = head;
    do {
        cout << "|" << temp->data << "|" << " -> ";
        temp = temp->next;
    } while (temp != head);
    cout << "(head)" << endl;
}
int main(){
    Node* head = NULL;
    display(head);
    insertAtHead(head, 1);
    insertAtHead(head, 2);
    display(head);
    insertAtTail(head, 3);
    display(head);
    deleteAtHead(head);
    display(head);
    deleteAtTail(head);
    display(head);
    insertAtTail(head, 4);
    display(head);
    updateAtPosition(head, 5, 1);
    display(head);
}
