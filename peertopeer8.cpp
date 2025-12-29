#include <iostream>
using namespace std;
struct Node{
    int data;
    Node* next;
    Node* prev;
};
class List{
    Node* head;
    Node* tail;

public:
    List(){
        head = tail = NULL;
    }
    void push_back(int val){
        Node* newNode = new Node();
        newNode -> data = val;
        newNode -> next = NULL;
        if(head == NULL){
            head = tail = newNode;
        }else{
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }
    void print(){
        Node* temp = head;
        while(temp != NULL){
            cout<<temp->data<<" ";
            temp = temp->next;
        }
    }
};
int main(){
    List dll;
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        int val;
        cin>>val;
        dll.push_back(val);
    }
    dll.print();
}