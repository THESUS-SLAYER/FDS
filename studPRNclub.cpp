#include<stdlib.h>
#include <iostream>
using namespace std;
typedef struct node
{
int prn;
char name[10]; //actual data
struct node *next;
}node;
class student
{
public:
node *create();
void print(node *HEAD);
node *insertsec(node *head);
node *insertmem(node *head);
node *insertpres(node *head);
node *reverse(node *head);
node *del(node *head);
node *conca(node *head1,node *head2);
void count(node *head);
};
node *student::create()
{
node *head,*p;
int i,n;
head=NULL;
cout<<"\n Enter the no of node:"<<endl;
cin>>n;
head=new node; //allocate memory for first node and its adress is stored in head
head->next=NULL;
cout<<"\n Enter the student prn no and name:"<<endl;
cin>>head->prn>>head->name; //read the data in first node
p=head; //in case of single node the first and last node are same single node 1 st and last node are same
//insert the remaining nodes
for(i=1;i<n;i++)
{
cout<<"\nStudent"<<i+1<<"prn no. and name";
//new node is inserted as the next node after P
p->next=new node;
p=p->next; //let us move the p to next node
p->next=NULL;
cin>>p->prn>>p->name;
}
return (head);
}
void student::print(node *HEAD)
{
node *p;
cout<<"\nlist of student ";
for(p=HEAD;p!=NULL;p=p->next)
{
cout<<"\n";
cout<<p->prn<<"\t"<<p->name;
}
}
node *student::insertsec(node *head) //insert at the end of the list //insert at the end
{
node *p,*q;
p=new node;
cout<<"\n Enter the prn no of student secre";
cin>>p->prn;
cout<<"\n Enter the name of student";
cin>>p->name;
if(head==NULL)
{
head=p;
return(head);
}
else
{
q=head;
while(q->next!=NULL)
q=q->next;
q->next=p; //next field of node store address of p
p->next=NULL; //as new node is the last node
return(head);
}
cout<<"\n_______Secretary is inserted_______"<<endl;
}
node *student::insertmem(node *head) //insert at middle
{
node *p,*q;
int key;
p=new node;
cout<<"\n Enter the prn no of student mem";
cin>>p->prn;
cout<<"\n Enter the name of student";
cin>>p->name;
if(head==NULL) //link list is empty
{
head=p;
}
else
{
cout<<"\n Enter the prn no of member:";
cin>>key;
q=head;
do
{
if(q->prn==key)
{
p->next=q->next;
q->next=p;
break;
}
else
q=q->next;
}while(q!=NULL);
}
return(head);
}
node *student::insertpres(node *head) //insert at front
{
node *p,*q;
p=new node; //allocate space for new node
cout<<"\n Enter the prn no of student pres";
cin>>p->prn;
cout<<"\n Enter the name of student";
cin>>p->name;
if(head==NULL)
{
head=p;
}
else
{
q=head;
p->next=q;
head=p; //now new inserted node i.e p becomes head node
}
cout<<"\n______President is inserted______";
return(head);
}
node *student::reverse(node *head)
{
if(head!=NULL)
{
reverse(head->next);
cout<<"\n"<<head->prn<<"\t"<<head->name;
}
return (head);
}
node *student::del(node *head)
{
node *p,*q;
int key;
q=new node;
p=head; //store address of first node in p
cout<<"\n Enter the prn of the node u wan 2 del:";
cin>>key;
while(p!=NULL)
{
if(p->prn==key)
break;
q=p;
p=p->next;
}
if(p==NULL)
{
cout<<"\n Node not found";
}
else
{
if(p==head)
head=p->next;
else
q->next=p->next;
delete(p);
cout<<"\n The mem is deleted\n";
}
return (head);
}
node *student::conca(node *head1,node *head2)
{
node *p;
if(head1==NULL)
return(head2);
if(head2==NULL)
return(head1);
p=head1;
while(p->next!=NULL)
p=p->next;
p->next=head2;
return(head1);
}
void student::count(node *head)
{
node *d;
int total=0;
d=head;
if(d==NULL)
{
cout<<"\n The list is empty";
return;
}
while(d!=NULL)
{
total++;
d=d->next;
}
cout<<"\n Total no of member in club are:"<<total;
}
int main()
{
int n,m,ch;
node *st=NULL;
node *s1,*s2;
node *head0=NULL,*head=NULL,*head6=NULL,*head4=NULL,*head5=NULL;
student s;
do
{
cout<<"\n Main menu";
cout<<"\n 1.Create club:";
cout<<"\n 2.Display members of club:";
cout<<"\n 3.Insert:";
cout<<"\n 4.Delete member:";
cout<<"\n 5.Total no of member of club:";
cout<<"\n 6.Display members in reverse order:";
cout<<"\n 7.Concatenate two list:";
cout<<"\n 8.Quit.";
cout<<"\n Enter your choice:";
cin>>m;
switch(m)
{
case 1:
head=s.create();
break;
case 2:
s.print(head);
break;
case 3:
cout<<"\n Members of club are:\n";
s.print(head);
cout<<"\n Insertion main menu:";
cout<<"\n 1.Insert president:";
cout<<"\n 2.Insert member:";
cout<<"\n 3.Insert secretary:";
cout<<"\n Enter your choice:";
cin>>ch;
switch(ch)
{
case 1:
head4=s.insertpres(head);
s.print(head4);
break;
case 2:
head4=s.insertmem(head);
s.print(head4);
break;
case 3:
head4=s.insertsec(head);
s.print(head4);
break;
default:
cout<<"\n Invalid choice.";
}
break;
case 4:
head5=s.del(head4);
s.print(head5);
break;
case 5:
s.count(head5);
break;
case 6:
head6=s.reverse(head5);
s.print(head6);
break;
case 7:
cout<<"\n Enter the members in first division:";
s1=s.create();
s.print(s1);
cout<<"\n Enter the members in second division:";
s2=s.create();
s.print(s2);
cout<<"\n Concatenated division is:";
st=s.conca(s1,s2);
s.print(st);
break;
case 8:
exit(0);
break;
default:
cout<<"\n Invalid choice.";
}
}while(m!=8);
return 0;
}
