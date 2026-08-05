// we will create a simple linked list with 3 nodes and print the values of the nodes
#include<bits/stdc++.h>
using namespace std;

class Node{
public:
    int data;
    Node* next;

    Node(int data){
        this->data = data;
        this->next = NULL;
    }
};

class LinkedList{
public:
    Node* head;

    LinkedList(){
        this->head = NULL;
    }

    void insert(int data){
        Node* newNode = new Node(data);
        if(head == NULL){
            head = newNode;
            return;
        }
        Node* temp = head;
        while(temp->next != NULL){
            temp = temp->next;
        }
        temp->next = newNode;
    }

    void print(){
        Node* temp = head;
        while(temp != NULL){
            if (temp->next != NULL){
                cout << temp->data << " -> ";
            } else {
                cout << temp->data;
            }
            temp = temp->next;
        }
        cout << endl;
    }
};

int main(){
    LinkedList list;
    list.insert(1);
    list.insert(2);
    list.insert(3);
    list.print();
    return 0;
}