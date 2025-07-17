#include <iostream>
using namespace std;
int a[] ={2,5,7,3,8};

void printArray(int array[], int n){
    for (int i = 0;i <n; i++){
        cout<<" "<<array[i];
    }
    cout<<"\n";
}
void Insertion_Sort(int a[],int n){
    for(int i = 1; i < n ;i++){
        int key = a[i];
        int j = i-1;
        while( j >= 0 && key < a[j] ){
            a[j+1] = a[j];
            j = j-1;
        }
        a[j+1] = key;
    }
}
int main(){
    Insertion_Sort(a,5);
    cout<<"Sorted array in Ascending Order: ";
    printArray(a,5);
}
