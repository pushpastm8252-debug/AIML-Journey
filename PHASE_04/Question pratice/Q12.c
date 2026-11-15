
#include<stdio.h>

int main(){
    int front=-1, rear=-1, ch, data, n;
    int queue[100];

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
            front=-1;
            rear=-1;

            printf("Enter size of queue (max 100): ");
            scanf("%d",&n);

            if(n<=0 || n>100){
                printf("Invalid size");
                break;
            }

            printf("Queue created successfully");
            break;

        case 2:
            if(n<=0 || n>100){
                printf("First create queue");
                break;
            }

            if(rear==n-1){
                printf("Queue Overflow");
            }
            else{
                printf("Enter data: ");
                scanf("%d",&data);

                rear++;

                queue[rear]=data;

                if(front==-1){
                    front=0;
                }

                printf("Enqueue successful");
            }
            break;

        case 3:
            if(n<=0 || n>100){
                printf("First create queue");
                break;
            }

            if(rear==n-1){
                printf("Queue Overflow");
            }
            else{
                printf("Enter data: ");
                scanf("%d",&data);

                if(front==-1){
                    front=0;
                    rear=0;
                    queue[front]=data;
                }
                else{
                    for(int i=rear;i>=front;i--){
                        queue[i+1]=queue[i];
                    }

                    queue[front]=data;
                    rear++;
                }

                printf("Inserted at first successfully");
            }
            break;

        case 4:
            if(front==-1){
                printf("Queue Underflow");
            }
            else{
                printf("Deleted element=%d",queue[front]);

                if(front==rear){
                    front=-1;
                    rear=-1;
                }
                else{
                    front++;
                }
            }
            break;

        case 5:
            if(front==-1){
                printf("Queue is empty");
            }
            else{
                printf("\nQueue elements:\n");

                for(int i=front;i<=rear;i++){
                    printf("%d\n",queue[i]);
                }
            }
            break;

        case 6:
            printf("Exiting...");
            break;

        default:
            printf("Invalid choice");
        }

    }while(ch!=6);

    return 0;
}
