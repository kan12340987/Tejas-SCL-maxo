#include <stdio.h>


int Binary(int low,int high,int ele,int arr[]){

 if(low> high)
 	return -1;

 else{
 	int mid=(low+high)/2;
    if(arr[mid]==ele)
    	return mid;
    if(arr[mid]>ele)
    	Binary(0,mid-1,ele,arr);
    else{
    	Binary(low+1,high,ele,arr);
    }
 }



}

int main(){
int arr[]={1,2,3,4,5};
int n=5;
int l=0;
int h=n;
int ele;
printf("enter ele");
scanf("%d",&ele);
int pos=Binary(l,h,ele,arr);
if(pos!=-1)
	printf("%d",pos);
else{
	printf("not found");
}
return 0;
}