#include<stdio.h>
int main(){
int n,ch;
printf("enter the size of stack:");
scanf("%d",&n);
int stack[n];
int top=-1;
do{
  printf("\n1.push");
  printf("\n2.pop");
  printf("\n3.display");
  printf("\n4.exit");
  printf("enter your choice");
  scanf("%d",&ch);
switch(ch){
  case 1:
  if(top==n-1){
    printf("stack overflow");
  }else{
    top++;
    printf("enter data");
    scanf("%d",&stack[top]);
    printf("push successful");
  }
  break;
  case 2:
  if(top==-1){
    printf("stack underflow");
  }
  else{
    printf("deleted element=%d",stack[top]);
    top--;
  }
  break;
  case 3:
  if(top==-1){
    printf("stack is empty");
  } else{
    printf("\nstack element\n");
    for(int i=top;i>=0;i--){
      printf("%d\n",stack[i]);
    }
  }
  break;
  case 4:
  printf("exit");
  break;
  default:
  printf("invalid choice");
}
}
while(ch!=4);

return 0;}