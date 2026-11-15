//deletion at hte beginning,eng,given information
#include<stdio.h>
#include<stdlib.h>
struct node{
  int data;
  struct node *next;
};
struct node *first,*ptr,*cpt;
int main(){
  int ch,choice,info;
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
    printf("enter 1 is conitnue and other number press false:");
    scanf("%d",&ch);
  }while(ch==1);
  cpt->next=NULL;
  ptr=first;
  while(ptr!=NULL){
    printf("%d->",ptr->data);
    ptr=ptr->next;
  }
  printf("\n1.deletion at the beginning:\n");
  printf("\n2.deletion at the end:\n");
  printf("\n3.deletion at the given information:\n");
  printf("enter your choice");
  scanf("%d",&choice);
  switch(choice){
    case 1:
    printf("\n deletion at the beginning\n");
    if(first==NULL){
      printf("linked list is empty\n");
    } else{
      cpt=first;
      first=first->next;
      free(cpt);
    }
    break;
    case 2:
    if(first==NULL){
      printf("\n linked list is empty\n");
    } else if(first->next==NULL){
      free(first);
      first=NULL;
    } else{
      ptr=first;
      while(ptr->next->next!=NULL){
        ptr=ptr->next;
      }
      cpt=ptr->next;
      ptr->next=NULL;
      free(cpt);
    }
    break;
    case 3:
    printf("\n at the given information\n");
    printf("enter the position:");
    scanf("%d",&info);
    if(info<=0){
      printf("\n invalid position\n");
    } else if(info==1){
      cpt=first;
      first=first->next;
      free(cpt);
    } else{
      ptr=first;
      int i=1;
      while(ptr->next!=NULL && i<info-1){
        ptr=ptr->next;
        i++;
      } if(ptr->next==NULL){
      printf("\n invalid position\n");
      }else{
        cpt=ptr->next;
        ptr->next=cpt->next;
        free(cpt);
      }
    }
    break;
    default:
    printf("\n invalid choice:\n");
  }
  ptr=first;
  while(ptr!=NULL){
    printf("%d->",ptr->data);
    ptr=ptr->next;
  }
  return 0;
}