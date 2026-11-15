//wap to concatination
//wap to count nodes in linked list
#include<stdio.h>
#include<stdlib.h>
struct node{
  int data;
  struct node *next;
};
struct node *first,*ptr,*cpt;
struct node *first1,*ptr1,*cpt1;
int main(){
  int ch,ch1;
ptr=(struct node*)malloc(sizeof(struct node));
printf("enter the data:");
scanf("%d",&ptr->data);
first=ptr;
do{
  cpt=(struct node*)malloc(sizeof(struct node));
  printf("enter the data:");
  scanf("%d",&cpt->data);
  ptr->next=cpt;
  ptr=cpt;
  printf("enter the 1 continue and other is stop:");
  scanf("%d",&ch);
}while(ch==1);
cpt->next=NULL;
ptr=first;
while(ptr!=NULL){
  printf("%d->",ptr->data);
  ptr=ptr->next;
}
ptr1=(struct node*)malloc(sizeof(struct node));
printf("enter the data:");
scanf("%d",&ptr1->data);
first1=ptr1;
do{
  cpt1=(struct node*)malloc(sizeof(struct node));
  printf("enter the data:");
  scanf("%d",&cpt1->data);
  ptr1->next=cpt1;
  ptr1=cpt1;
  printf("enter the 1 continue and other is stop:");
  scanf("%d",&ch1);
}while(ch1==1);
cpt1->next=NULL;
ptr1=first1;
while(ptr1!=NULL){
  printf("%d->",ptr1->data);
  ptr1=ptr1->next;
}
ptr=first;
while(ptr->next!=NULL){
  ptr=ptr->next;
}
  ptr->next=first1;
  printf("\nconcatination linked list:");
  ptr=first;
while(ptr!=NULL){
  printf("%d->",ptr->data);
  ptr=ptr->next;
}
  return 0;
}