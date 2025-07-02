#include<iostream>
#include<string>
using namespace std;

#define max 15

template<class t>
class stack{
    t data[max];
    int tos;
    public:
    stack():tos(-1){}
    
    void push(t value)
    {
        if(tos==max-1)
        {
            cout<<"stack overflow!!"<<endl;
        
        }
        else
        {
            data[++tos]=value;
        }
    }
    
    t pop()
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
    t peek()
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

string infix_to_postfix(string infix)
{
    stack <char> s;
    string postfix;
    
    s.push('('); // push ( onto stack
    infix += ')';
    
    for (auto x: infix)
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
        }
        else if (x=='^'|| x =='/'|| x=='*'|| x=='+'||x=='-')
        {
            while (precision_check(x) <= precision_check(s.peek())&& s.peek()!='(')
            postfix+=s.pop();
            s.push(x);
        }
        else
        {
            postfix += x;
        }
    }
    return postfix;
}

int main()
{
    string infix_expression;
    cout<<"Enter the infix expression"<<endl;
    getline(cin,infix_expression);
    if(infix_expression.empty())
    {
        cout<<"Empty expression entered!"<<endl;
        return 1;
    }
    string postfix_expression = infix_to_postfix(infix_expression);
    cout<<"The equivalent postfix expression is :"<<postfix_expression;
    return 0;
}

