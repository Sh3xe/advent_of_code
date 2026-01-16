#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>

int modulo(int n, int mod)
{
	return (n % mod + mod) % mod;
}

int main()
{
	int num = 50;
	int num_zeros = 0;
	int num_clicks = 0;
	std::string line;
	std::fstream f{"t1_1.txt"};

	if(!f) 
	{
		std::cout << "Cannot open the file" << std::endl;
		return -1;
	}

	while(std::getline(f, line))
	{
		int curr_num = std::stoi(line.substr(1));
		if(line[0] == 'L')
			curr_num *= -1;

		int r = (num+curr_num) % 100;
		int div = (num+curr_num-r) / 100;
		if (num + curr_num < 0)
			div -= 1;
		if (num == 0 && num+curr_num < 0)
			div += 1;
		if (num > 0 && num+curr_num == 0)
			div += 1;
		
		num_clicks += abs(div);
		num = ((num + curr_num) % 100 + 100) % 100;
		num_zeros += num == 0;
	}

	std::cout << "part 1: " << num_zeros << std::endl;
	std::cout << "part 2: " << num_clicks << std::endl;

	return 0;
}