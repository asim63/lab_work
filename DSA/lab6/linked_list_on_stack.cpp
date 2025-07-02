#include<iostream>
using namespace std;

class Node{
  public:
  int data;
  Node* next;
  
  Node(int val){
      data = val;
      next = NULL;
  }
};
void push(Node* &head, int val){
    Node* newnode = new Node(val);
    
    newnode->next = head;
    head = newnode;
    
}
void pop(Node* &head)
{
    if(head == NULL){
        cout<<"the stack is empty"<<endl;
       
    }
    Node* temp = head;
    head = head->next;
    delete temp;
}

void display(Node* head){
    Node* temp = head;
    cout<<"Stack(from top to bottom):";
    while(temp!= NULL){
        cout<<"|"<<temp->data<<"|"<<"->";
        temp = temp->next;
    }
    cout<<"NULL"<<endl;
}

int main(){
    Node* head = NULL;
    display(head);
    push(head, 30);
    display(head);
    push(head, 20);
    display(head);
    push(head, 40);
    display(head);
    pop(head);
    display(head);
    pop(head);
    display(head);
    pop(head);
    display(head);
    pop(head);
    display(head);
    return 0;
}
