#include <iostream>
#define max 10
using namespace std;

struct queue{
	int data[max];
	int front,rear;
};

class Queue{
	struct queue q;
	public :
		Queue(){
			q.front=q.rear=-1;
		}
		int isempty();
		int isfull();
		void enqueue(int);
		int delqueue();
		void display();
};

int Queue::isempty(){
	return (q.front==q.rear)?1:0;
}
int Queue::isfull(){
	return (q.rear==max-1)?1:0;
}
void Queue::enqueue(int x){
	q.data[++q.rear]=x;
}
int Queue::delqueue(){
	return (q.data[++q.front]);
}
void Queue::display(){
	int i;
	cout<<"\n";
	for(i=q.front+1;i<=q.rear;i++){
		cout<<q.data[i]<<" ";
	}
}

int main(){
	Queue obj;
	int ch,x;
	
	do{
		cout<<"\n MENU";
		cout<<"\n 1.insert";
		cout<<"\n 2.delete";
		cout<<"\n 3.display";
		cout<<"\n 4.Exit";
		cout<<"\n Enter your choice : ";
		cin>>ch;
		
		switch(ch){
			case 1:
				if(!obj.isfull() ){
					cout<<"\n Enter job data : ";
					cin>>x;
					obj.enqueue(x);
				}
				else
				{
					cout<<"\n job is overflow ";
				}
				break;
				
			case 2:
				if(!obj.isempty() ){
					cout<<"\n Delete job data : "<<obj.delqueue();
				}
				else
				{
					cout<<"\n job is underflow : ";
				}
				cout<<"\n Remaing jobs : ";
				obj.display();
				break ;
				
			case 3:
				if(!obj.isempty() ){
					cout<<"\n Job Contains : ";
					obj.display();
				}
				else 
				{
					cout<<"\n Job is underflow ";
				}
				break ;
				
			case 4:
				cout<<"\n Exit";
		}
	}while(ch!=4);

}
