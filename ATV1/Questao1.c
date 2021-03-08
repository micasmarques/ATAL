#include <iostream>
int main(){
	int n, soma, somaMax, i, aux;
	while(scanf("%n", n) > 0) {
		soma = 0;
		somaMax = 0;
		for(i = 0; i < n; i++){
			scanf("%i", aux);
			soma += aux;
			if(soma < 0) soma = 0;
			if(soma > somaMax) somaMax = soma;
		}
		if(somaMax == 0) 
			printf("Losing streak.\n");
		else 
			printf("The maximum winning streak is %i." ,somaMax);
	}
	return 0;
}
