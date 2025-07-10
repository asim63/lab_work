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
Node* insert(Node* root, int val){
    if(root == NULL)
        return new Node(val);
    if(root->data < val)
        root->right = insert(root->right, val);
    else
        root->left = insert(root->left, val);
    return root;
}
bool search(Node* root,int val){
    if(root == NULL)
        return false;
    if(root->data == val)
        return true;
        
    if(root->data < val)
        return search(root->right, val);
    
    return search(root->left, val);
}
Node* getSuccessor(Node* curr){
    curr = curr->right;
    while(curr != NULL && curr->left != NULL)
        curr = curr->left;
    return curr;
}

void del_Node(Node* &root, int val){
    if(root == NULL)
        return;
    if(root->data > val){
        del_Node(root->left, val);
    }    
    else if(root->data <val){
        del_Node(root->right, val);
    }
    else{
        if(root->left == NULL){
            Node*temp = root->left;
            delete root;
            root = temp;
        }
        else if(root->right == NULL){
            Node*temp = root->left;
            delete root;
            root = temp;
        }
        else{
            Node* succ = getSuccessor(root);
            root->data = succ->data;
            del_Node(root->right, succ->data);
        }
    }
}
int main(){
    Node* root = new Node(50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
    cout<<"In order traversal: ";
    in_Order(root);
    cout<<endl;
    cout<<(search(root, 70) ? "\n70 is found": "70 is not found")<<endl;
    cout<<(search(root, 19) ? "\n19 is found": "19 is not found")<<endl;
    del_Node(root, 40);
    in_Order(root);
    return 0;
}
