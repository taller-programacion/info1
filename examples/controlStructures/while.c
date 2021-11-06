#include <stdio.h>

int cont=0;

int main(void){ 

	while(cont != 0){ // 0 != 0 -->false
		printf("\n\n La variable cont dentro de while vale: %i", cont); 
		cont++;
	}
	printf("\n\n La variable cont vale: %i", cont);

	return 0;
}
