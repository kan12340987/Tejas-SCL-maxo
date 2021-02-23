#include <stdio.h>
#include <time.h>
#include<stdlib.h>
void randa(int n, int low,int up){

int i;
for(i=0;i<n;i++){
	int num = (rand() % 
           (up - low + 1)) + low; 
	printf("%d\t",num);
}

}

int main(){
	int n,u,l;
	scanf("%d%d%d",&n,&l,&u);
	printf("\n");
	randa(n,l,u);
	return 0;
}