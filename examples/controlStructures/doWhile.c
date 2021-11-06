#include <stdio.h>

int cont=0;

int main(void){ 

	do{
		printf("\n\n La variable cont dentro de while vale: %i", cont); 
	}while(cont != 0);
	
	printf("\n\n La variable cont vale: %i", cont); // 6

	return 0;
}
