//wap to search an element in a linked list
#include<stdio.h>
#include<stdlib.h>
struct node{
int data;
struct node *next;
};
struct node *first,*ptr,*cpt;
int main(){
  int ch,search,found=0,pos=1;
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
printf("enter the element to search:");
scanf("%d",&search);
ptr=first;
while(ptr!=NULL){
  if(ptr->data==search){
    printf("element found at position %d",pos);
    found=1;
    break;
  }
  ptr=ptr->next;
  pos++;
}
if(found==0){
  printf("element not found");
}
return 0;}