#include <iostream>
using namespace std;
int a[] ={2,5,7,3,8};

void printArray(int array[], int n){
    for (int i = 0;i <n; i++){
        cout<<" "<<array[i];
    }
    cout<<"\n";
}
void Selection_Sort(int a[],int n){
    for(int i = 0;i<n-2 ;i++){
        int min_index = i;
        for (int j = i+1; j< n-1; j++){
            if(a[j] < a[min_index]){
                min_index = j;
            }
        }
        int temp = a[i];
        a[i] = a[min_index];
        a[min_index] = temp;
    }
}
int main(){
    Selection_Sort(a,5);
    cout<<"Sorted array in Ascending Order: ";
    printArray(a,5);
}
