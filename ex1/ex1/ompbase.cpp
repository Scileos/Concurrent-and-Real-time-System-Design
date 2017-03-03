#include "omp.h"
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <string>

int main (void)
{
	string word = "";


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
	cout << s << endl;
}
}

void stringB() 
{
	while (word != "exit") {

	std:: stringstream ss;
	ss << word << "B";
	std::string s = ss.str();
	cout << s << endl;
}
}
