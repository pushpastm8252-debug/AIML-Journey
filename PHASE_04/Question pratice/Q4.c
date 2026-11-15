//find max and min
#include<stdio.h>
#include<stdlib.h>
struct node{
  int data;
  struct node *next;
};
struct node *first,*ptr,*cpt;
int main(){
  int ch,max,min;
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
    printf("enter 1 is continue and other number is stop:");
    scanf("%d",&ch);
  }while(ch==1);
  cpt->next=NULL;
  ptr=first;
  while(ptr!=NULL){
    printf("%d->",ptr->data);
    ptr=ptr->next;
  }
  max=first->data,min=first->data;
  ptr=first->next;
  while(ptr!=NULL){
    if(ptr->data>max){
    max=ptr->data;
  } if(ptr->data<min){
    min=ptr->data;
  }
  ptr=ptr->next;
  }
  printf("\nmax=%d",max);
  printf("\nmin=%d",min);
 return 0;}