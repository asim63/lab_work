#include<iostream>
using namespace std;
#include<string>
void THanoi(int n, string source, string destination, string auxillary){
    if(n==1){
        cout<<"Moved disk 1 from " << source<<" to " << destination<< endl;
        return;
    }
    THanoi(n-1,source, auxillary, destination);
    cout<<"Moved disk " <<n<<" from "<<source<< " to " << destination<<endl;
    THanoi(n-1,auxillary,destination,source);
}
int main()
{
    int no_of_discs;
    cout<<"Enter no . of discs: ";
    cin>> no_of_discs;
    THanoi(no_of_discs, "Source", "Destination", "Auxillary");
    return 0 ;
}
