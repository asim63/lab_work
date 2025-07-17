#include <iostream>
using namespace std;
int a[5] ={2,5,7,3,8};

void bubbleSort(int a[],int n){
    for(int i= 0; i < n-1; i++){
        for(int j = 0;j < n-1 ;j++){
            if (a[j] > a[j+1]){
                int temp = a[j+1];
                a[j+1] = a[j];
                a[j] = temp;
            }
        }
    }
}
void printArray(int array[], int n){
    for (int i = 0;i <n; i++){
        cout<<" "<<array[i];
    }
    cout<<"\n";
}
int main(){
    bubbleSort(a,5);
    printArray(a,5);
}
