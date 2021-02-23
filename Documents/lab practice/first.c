#include<stdio.h>
#include "select.h"
int main(){


int arr[10];
int n,i;
printf("enter size\n" );
scanf("%d",&n);
printf("enter elements of the array\n");
for(i=0;i<n;i++){

  scanf("%d",&arr[i]);


}
selection(arr,n);
return 0;
   

		
}