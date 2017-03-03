#include "omp.h"
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <string>

string word = "";

int main (void)
{


	#pragma omp secitions
		{
			{stringSelector(); }
			#pragma omp section
			{stringA(); }
			#pragma omp section
			{stringB(); }
		}
		
return 0;
}

void stringSelector() 
{
	while (word != "exit") {
	std::cin >> word >> std::endl;
	}
}

void stringA() 
{
	while (word != "exit") {
	std:: stringstream ss;
	ss << word << "A";
	std::string s = ss.str();
	std::cout << s << std::endl;
}
}

void stringB() 
{
	while (word != "exit") {

	std:: stringstream ss;
	ss << word << "B";
	std::string s = ss.str();
	std::cout << s << std::endl;
}
}
