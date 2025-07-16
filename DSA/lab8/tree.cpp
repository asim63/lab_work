#include<iostream>
using namespace std;
class Node{
    public:
    Node* left;
    Node* right;
    int data;
    
    Node(int val):left(NULL),right(NULL),data(val){}
};

void in_Order(Node *root){
    if(root == NULL) return;
    in_Order(root->left);
    cout<<root->data<<" ";
    in_Order(root->right);
}

void pre_Order(Node* root){
    if(root == NULL) return;
    cout<<root->data<<" ";
    pre_Order(root->left);
    pre_Order(root->right);
}
void post_Order(Node* root){
    if(root == NULL) return;
    post_Order(root->left);
    post_Order(root->right);
    cout<<root->data<<" ";
}

int main(){
    Node* root = new Node(10);
    root->left = new Node(20);
    root->right = new Node(30);
    root->left->left = new Node(40);
    
    cout<<"In-order Traversal: ";
    in_Order(root);
    
    cout<<"\nPre-order Traversal: ";
    pre_Order(root);
    
    cout<<"\nPost-order Traversal: ";
    post_Order(root);
    
    return 0;
}
