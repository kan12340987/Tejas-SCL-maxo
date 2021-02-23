#include <stdio.h>



int main()
{
	int arr[10];
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
	  scanf("%d",&arr[i]);


	}
	int *ptr=&arr[n-1];
	for(){
      printf("%d\n",*(ptr));
     
	}
	
	return 0;

}