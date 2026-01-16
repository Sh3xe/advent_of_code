#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <utility>

std::pair<size_t,size_t> find_line_key(
	const std::string &line,
	size_t current_index,
	size_t remaining_digits)
{
	if( remaining_digits == 0 )
		return std::make_pair(0,1);

	size_t max_idx = current_index;
	for(int i = current_index+1; i < line.size()-remaining_digits + 1; ++i)
	{
		if(line[i] > line[max_idx])
			max_idx = i;
	}

	int digit = line[max_idx] - '0';
	auto [curr_key, curr_pow] = find_line_key(line, max_idx+1, remaining_digits-1);
	return std::make_pair(curr_key + curr_pow*digit, curr_pow*10);
}

int main()
{
	int num = 50;
	size_t key_1 = 0, key_2 = 0;

	std::string line;
	std::fstream f{"input3.txt"};

	if(!f) 
	{
		std::cout << "Cannot open the file" << std::endl;
		return -1;
	}

	while(std::getline(f, line))
	{
		auto [curr_key1, exp_1] = find_line_key(line, 0, 2);
		key_1 += curr_key1;

		auto [curr_key2, exp_2] = find_line_key(line, 0, 12);
		key_2 += curr_key2;
	}

	std::cout << "part 1: " << key_1 << std::endl;
	std::cout << "part 2: " << key_2 << std::endl;

	return 0;
}