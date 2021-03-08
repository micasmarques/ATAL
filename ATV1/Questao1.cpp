#include <iostream>

using namespace std;

int main() {
	int n, soma, somaMax, i, aux;
	
	std::cin >> n;
	while(n > 0){
		soma = 0;
		somaMax = 0;
		for(i = 0; i < n; i++) {
			std::cin >> aux;

			soma += aux;
			if(soma < 0) soma = 0;
			if(soma > somaMax) somaMax = soma;
		}
		if(somaMax == 0) std::cout << "Losing streak." << endl;
		else std::cout << "The maximum winning streak is " << somaMax << "." << endl;
		std::cin >> n;
	}
	return 0;
}
