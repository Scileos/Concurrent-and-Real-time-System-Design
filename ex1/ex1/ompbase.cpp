#include "omp.h"
#include <iostream>
#include <cmath>
#include <cstdlib>

int main (void)
{
	#pragma omp parallel
	{
		int i = omp_get_thread_num();
		std::cout << omp_get_thread_num() << std::endl;
	}
return 0;
}
