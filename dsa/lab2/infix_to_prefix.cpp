#include<iostream>
#include<string>
using namespace std;

#define MAX 15

template<class T>
class Stack{
    T data[MAX];
    int tos;
    public:
    Stack():tos(-1){}
    
    void push(T value)
    {
        if(tos==MAX-1)
        {
            cout<<"stack overflow!!"<<endl;
        
        }
        else
        {
            data[++tos]=value;
        }
    }
    
    T pop()
    {
        if (tos==-1)
        {
            cout<<"Stack underflow"<<endl;
            return 0;
        }
        else{
            return data[tos--];
        }
    }
    T peek()
    {
        if (tos==-1)
        {
            cout<<"Stack underflow"<<endl;
            return 0;
        }
        else{
            return data[tos];
        }
    }
    
};

int precision_check(char x) //for priority where higher priority is 3
{
    if (x=='^')
    {
        return 3;
    }
    else if (x== '/' || x== '*')
    {
        return 2;
    }
    else if ( x== '+' || x=='-')
    {
        return 1;
    }
    return -1;
}

string infix_to_postfix(string expression)
{
    Stack <char> s;
    string postfix;
    
    s.push('('); // push ( onto stack
    expression += ')';
    
    for (auto x: expression)
    {
        if (x== '(') //if left parenthesis add it to stack
        {
            s.push(x);
        }
        else if (x == ')') // if right parenthesis then pop every operator until right parenthesis
        {
            while(s.peek() != '(') 
            {
                postfix += s.pop();
            }
            s.pop();
        }
        else if (x=='^'|| x =='/'|| x=='*'|| x=='+'||x=='-')
        {
            if(precision_check(x) == precision_check(s.peek())){
             s.push(x);
        }
        
        else{
         while (precision_check(x) < precision_check(s.peek()) && s.peek() != '(') {
         postfix += s.pop();
        }
            s.push(x);
        }
        }
        else
        {
            postfix += x;
        }
    }
    return postfix;
}
string infix_to_prefix(string expression) {
    string reversed_expr, prefix;
    
    for(int i = expression.length() - 1;i>= 0; --i){
        if(expression[i] ==')'){
            reversed_expr+= '(';
        } else if(expression[i] == '('){
            reversed_expr += ')';
        }else {
            reversed_expr += expression[i];
        }
    }
    string postfix = infix_to_postfix(reversed_expr);
    
    for(int i= postfix.length() - 1 ; i >= 0; --i){
        prefix += postfix[i];
    }
    return prefix;
}


int main()
{
    string expression;
    cout<<"Enter the infix expression [Put '^' as an exponent]: "<<endl;
    getline(cin,expression);
    if(expression.empty())
    {
        cout<<"Empty expression entered!"<<endl;
        return 1;
    }
    string prefix_expression = infix_to_prefix(expression);
    cout<<"The equivalent prefix expression is :"<<prefix_expression;
    return 0;
}

