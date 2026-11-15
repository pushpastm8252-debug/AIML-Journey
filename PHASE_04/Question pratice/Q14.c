
#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};

struct node *front=NULL,*rear=NULL,*ptr,*temp;

void create(){
    while(front!=NULL){
        temp=front;
        front=front->next;
        free(temp);
    }
    rear=NULL;
    printf("Queue created successfully");
}

void enqueue_rear(){
    ptr=(struct node*)malloc(sizeof(struct node));

    if(ptr==NULL){
        printf("Memory allocation failed");
        return;
    }

    printf("Enter data: ");
    scanf("%d",&ptr->data);

    ptr->next=NULL;

    if(front==NULL){
        front=rear=ptr;
    }
    else{
        rear->next=ptr;
        rear=ptr;
    }

    printf("Enqueue at rear successful");
}

void enqueue_first(){
    ptr=(struct node*)malloc(sizeof(struct node));

    if(ptr==NULL){
        printf("Memory allocation failed");
        return;
    }

    printf("Enter data: ");
    scanf("%d",&ptr->data);

    ptr->next=front;
    front=ptr;

    if(rear==NULL){
        rear=ptr;
    }

    printf("Enqueue at first successful");
}

void dequeue(){
    if(front==NULL){
        printf("Queue Underflow");
    }
    else{
        temp=front;

        printf("Deleted element=%d",front->data);

        front=front->next;

        if(front==NULL){
            rear=NULL;
        }

        free(temp);
    }
}

void traverse(){
    if(front==NULL){
        printf("Queue is empty");
    }
    else{
        ptr=front;

        printf("\nQueue elements:\n");

        while(ptr!=NULL){
            printf("%d\n",ptr->data);
            ptr=ptr->next;
        }
    }
}

int main(){
    int ch;

    do{
        printf("\n\n1. Create");
        printf("\n2. Enqueue at Rear");
        printf("\n3. Enqueue at First");
        printf("\n4. Dequeue");
        printf("\n5. Traverse");
        printf("\n6. Exit");

        printf("\nEnter your choice: ");
        scanf("%d",&ch);

        switch(ch){

            case 1:
                create();
                break;

            case 2:
                enqueue_rear();
                break;

            case 3:
                enqueue_first();
                break;

            case 4:
                dequeue();
                break;

            case 5:
                traverse();
                break;

            case 6:
                create();
                printf("Exiting...");
                break;

            default:
                printf("Invalid choice");
        }

    }while(ch!=6);

    return 0;
}
