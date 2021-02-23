#include <stdio.h>
#include <stdlib.h>
struct node
{
	int roll;
	float cgpa;
	char arr[25];
};


int main()
{

  struct node *n1;
  int n;
  scanf("%d",&n);
  n1=(struct node *)malloc(sizeof(struct node));
  for(int i=0;i<n;i++){


  scanf("%d",&(n1+i)->roll);
  scanf("%s",&(n1+i)->arr);
  scanf("%f",&(n1+i)->cgpa);
}

for(int i=0;i<n;i++){
 printf("%d%s%f\n",(n1+i)->roll,(n1+i)->arr,(n1+i)->cgpa);  
}

 
	
	return 0;
}