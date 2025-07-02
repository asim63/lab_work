#include<iostream>
using namespace std;
int size = 0;
class Node{
    public:
    int data;
    Node* next;
    
    Node(int val){
        data = val;
        next = NULL;
    }
};
int getsize(){
    return size;
}
void insertAtHead(Node* &head, int val){
    Node* newnode = new Node(val);
    newnode->next = head;
    head = newnode;
    size++;
}
void insertAtTail(Node* &head, int val){
    Node* newnode = new Node(val);
    Node* temp = head;
    
    while(temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newnode;
    size++;
}
void insertAtPosition(Node* &head, int val, int pos)
{
    Node* newnode = new Node(val);
    int i = getsize();
    if(pos == 0){
        insertAtHead(head,val);
        return;
    }
    Node* temp = head;
    int curr_pos = 0;
    if(pos >= i){
        insertAtTail(head,val);
        return;
    }
    while(curr_pos != pos-1){
        temp = temp->next;
        curr_pos++;
    }
    newnode->next = temp->next;
    temp->next = newnode;
    size++;
}
void updateAtPosition(Node* &head, int val, int pos){
    Node* temp = head;
    int curr_pos = 0;
    while(curr_pos != pos){
        temp = temp->next;
        curr_pos++;
    }
    temp->data = val;
}
void deleteAtHead(Node* &head){
    Node* temp = head;
    head = head->next;
    delete temp;
    size--;
}
void deleteAtTail(Node* &head){
    Node* temp = head;
    while(temp->next->next != NULL){
        temp = temp->next;
    }
    Node* temp2 = temp->next;
    temp->next = NULL;
    delete temp2;
    size--;
}
void deleteAtPosition(Node* &head, int pos){
    Node* prev = head;
    int i = getsize();
    if(pos==0){
        deleteAtHead(head);
        return;
    }
    if(pos>i){
        cout<<"Limit reached. The size of linked list is lesser."<<endl;
        return;
    }
    int curr_pos=0;
    while(curr_pos != pos-1){
        prev = prev->next;
        curr_pos++;
    }
    Node* temp = prev->next;
    prev->next = temp->next;
    delete temp;
    size--;
}
void display(Node* &head){
    Node* temp = head;
    while(temp !=NULL){
        cout<<"|"<<temp->data<<"|"<<" -> ";
        temp=temp->next;
    }
    cout<<"NULL"<<endl;
}
int main(){
    Node* head = NULL;
    display(head); 
    
    insertAtHead(head, 1);
    display(head);
    
    insertAtHead(head, 2);
    display(head);
    
    insertAtTail(head, 3);
    display(head);
    
    insertAtPosition(head, 5, 3);
    display(head);
    
    insertAtPosition(head, 4, 20); 
    display(head);
    
    updateAtPosition(head, 9, 2);
    display(head);
    
    deleteAtHead(head);
    display(head);
    
    deleteAtTail(head);
    display(head);
    
    deleteAtPosition(head, 2);
    display(head);
    
    deleteAtPosition(head, 10); 
    
    deleteAtPosition(head, 1);
    display(head);
    
    deleteAtPosition(head, 0);
    display(head);
    
    return 0;
}
