//create linked list and triverse
#include<stdio.h>
#include<stdlib.h>
struct node{
  int data;
  struct node *next;
};
struct node *first,*ptr,*cpt;
int ch;
int main(){
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
    printf("enter 1 to continue and other number press stop:");
    scanf("%d",&ch);
  }while(ch==1);
  cpt->next=NULL;
  ptr=first;
  while(ptr!=NULL){
    printf("%d->",ptr->data);
    ptr=ptr->next;
  }
  return 0;
}