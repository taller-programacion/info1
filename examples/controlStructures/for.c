#include <stdio.h>

int cont;

int main(void){ 

	for(cont = 1; cont > 5; cont++){ // cont =6 ; 6 <= 5-> true
		printf("\n\t %i --> Te amo <3", cont);  //5 -- Te amo <3
	}
	
	printf("\n\n La variable cont vale: %i", cont); // 6

	return 0;
}
