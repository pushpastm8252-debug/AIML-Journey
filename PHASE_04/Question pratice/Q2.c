//insertion at the beginning ,end and given position
#include<stdio.h>
#include<stdlib.h>
struct node{
  int data;
  struct node *next;
};
struct node *first,*ptr,*cpt;
int main(){
  int ch,info,choice;
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
    printf("enter 1 continu and other number is stop:");
    scanf("%d",&ch);
  }while(ch==1);
  cpt->next=NULL;
  ptr=first;
  while(ptr!=NULL){
    printf("%d->",ptr->data);
    ptr=ptr->next;
  }
  printf("\n1.insertion at the biginning\n");
  printf("2.insertion at the end\n");
  printf("\n3.insertion at the given position\n");
  printf("enter the choice of number:");
  scanf("%d",&choice);
  switch(choice){
    case 1:
    cpt=(struct node*)malloc(sizeof(struct node));
    printf("enter the data:");
    scanf("%d",&cpt->data);
    cpt->next=first;
    first=cpt;
    printf("insertion at the beginning:\n");
    break;
    case 2:
    cpt=(struct node*)malloc(sizeof(struct node));
    printf("enter the data:");
    scanf("%d",&cpt->data);
    cpt->next=NULL;
    ptr=first;
    while(ptr->next!=NULL){
      ptr=ptr->next;
    }
    ptr->next=cpt;
    printf("\ninsertion at the end\n");
    break;
    case 3:
    cpt=(struct node*)malloc(sizeof(struct node));
    printf("enter  the data:");
    scanf("%d",&cpt->data);
    ptr=first;
    printf("enter the given position:");
    scanf("%d",&info);
    while(ptr!=NULL && ptr->data!=info){
      ptr=ptr->next;
    }
    if(ptr==NULL){
      printf("\n given information not found\n");
    }else{
      cpt->next=ptr->next;
      ptr->next=cpt;
    }
    printf("\n node inserted succefully\n");
    ptr=first;
    printf("\n linked list after insertion\n");
    break;
    default:
    printf("\n invalid choice\n");
  }
  ptr=first;
  while(ptr!=NULL){
    printf("%d->",ptr->data);
    ptr=ptr->next;
  }
  return 0;
}