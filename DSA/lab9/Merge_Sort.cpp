#include <iostream>
#include<vector>
using namespace std;
int a[] ={2,5,7,3,8};

void printArray(int array[], int n){
    for (int i = 0;i <n; i++){
        cout<<" "<<array[i];
    }
    cout<<"\n";
}
void merge(int arr[], int p , int q, int r){
    int n1 = q-p+1;
    int n2 = r - q;
    
    vector<int> L(n1);
    vector<int> M(n2);
    
    for(int i = 0; i<n1 ; i++){
        L[i] = arr[p+i];
    }
    for (int j = 0; j<n2; j++){
        M[j] = arr[q+1+j];
    }
    int i = 0,j = 0, k = p;
    while(i <n1 &&j<n2){
        if(L[i] <= M[j]){
            arr[k] = L[i];
            i++;
        }else{
            arr[k] = M[j];
            j++;
        }
        k++;
    }
    while (i<n1){
        arr[k] =L[i];
        i++;
        k++;
    }
    while(j<n2){
        arr[k] = M[j];
        j++;
        k++;
    }
}
void Merge_Sort(int a[], int l, int r){
    if(l<r){
    int m = l + (r-l)/2;
    Merge_Sort(a,l,m);
    Merge_Sort(a,m+1,r);
    merge(a,l,m,r);
    }
}
int main(){
    Merge_Sort(a,0,4);
    cout<<"Sorted array in Ascending Order: ";
    printArray(a,5);
}
