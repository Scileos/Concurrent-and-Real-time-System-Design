#include "omp.h"
#include <iostream>
#include <cmath>
#include <cstdlib>

int main (void)
{
	int n = 3
	int m = 3

	#pragma omp parallel for collapse(2)
		for(x=0;x<n;x++) {
			for(y=0;y<m;y++) {
				int add = x + y
				printf(add)
			}
		}
		
return 0;
}
