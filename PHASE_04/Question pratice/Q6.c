//wap to count nodes in linked list
#include<stdio.h>
#include<stdlib.h>
struct node{
  int data;
  struct node *next;
};
struct node *first,*ptr,*cpt;
int main(){
  int ch,count=0;
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
ptr=first;
while(ptr!=NULL){
  count++;
  ptr=ptr->next;
}
printf("\n total number of nodes=%d",count);
  return 0;
}