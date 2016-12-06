#include<stdio.h>
int f(int);
int main(){
	for(int i=0;i<600;i++){
		//if(i%10==0){printf("\n");}
	printf("i = %d %d\n ",i,f(i));
	}
	return 0;
}

int f(int n){
	if(n<10){
	return n;
	}
	else{
	return(f((n/10) + (n % 10)));
	}
}