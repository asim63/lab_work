#include <iostream>
#define MAX 5
using namespace std;

template <class T>
class CQUEUE {
    T data[MAX];
    int f, r;

public:
    CQUEUE() : f(-1), r(-1) {}

    void Enqueue(T value) {
        if ((r + 1) % MAX == f) {
            cout << "Queue Overflow" << endl;
            return;
        }
        if (f == -1) {
            f = r = 0;
        } else {
            r = (r + 1) % MAX;
        }
        data[r] = value;
    }

    T Dequeue() {
        if (f == -1) {
            cout << "Queue Underflow" << endl;
            return -1;
        }
        T val = data[f];
        if (f == r) {
            f = r = -1;
        } else {
            f = (f + 1) % MAX;
        }
        return val;
    }

    void Display() {
        if (f == -1) {
            cout << "Queue is empty" << endl;
            return;
        }
        cout << "Queue elements: ";
       int i = f;
       while (true) {
        cout << data[i] << " ";
        if (i == r) break;
        i = (i + 1) % MAX;
        }
        cout << endl;
    }
};

int main() {
    CQUEUE<int> q;
    q.Enqueue(10);
    q.Enqueue(20);
    q.Enqueue(30);
    q.Enqueue(40);
    q.Enqueue(50);
    q.Display();
    cout << "Dequeued: " << q.Dequeue() << endl;  
    cout << "Dequeued: " << q.Dequeue() << endl;  
    q.Display();    
    q.Enqueue(60);
    q.Enqueue(70);
    q.Display();    

    q.Enqueue(80);  

    return 0;
}
