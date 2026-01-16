#include <fstream>
#include <iostream>
#include <cstdint>

size_t part_1(std::string left, std::string right)
{
	size_t hash = 0;

	std::string subpatern = "";
	std::string s_i = "";
	for( size_t i = std::stoll(left); i <= std::stoll(right); ++i)
	{
		s_i = std::to_string(i);

		for( size_t k = 1; k <= s_i.size() / 2; ++k)
		{
			if( s_i.size() % k != 0 ) continue;
			// for part 1
			if( k != s_i.size() / 2 || s_i.size() % 2 != 0) continue;

			bool all_good = true;
			subpatern = s_i.substr(0,k);
			for(size_t j = 1; j < s_i.size() / k; ++j )
				all_good &= s_i.substr(j*k,k)==subpatern;

			if(all_good) {
				std::cout << i << std::endl;
				hash += i;
				break;
			}
		}
	}

	return hash;
}

size_t part_2(std::string left, std::string right)
{
	size_t hash = 0;

	std::string subpatern = "";
	std::string s_i = "";
	for( size_t i = std::stoll(left); i <= std::stoll(right); ++i)
	{
		s_i = std::to_string(i);

		for( size_t k = 1; k <= s_i.size() / 2; ++k)
		{
			if( s_i.size() % k != 0 ) continue;

			bool all_good = true;
			subpatern = s_i.substr(0,k);
			for(size_t j = 1; j < s_i.size() / k; ++j )
				all_good &= s_i.substr(j*k,k)==subpatern;

			if(all_good) {
				std::cout << i << std::endl;
				hash += i;
				break;
			}
		}
	}

	return hash;
}

int main()
{
	size_t key2 = 0;
	size_t key1 = 0;

	std::fstream f{"input2.txt"};
	std::string right;
	std::string left;
	std::string buf;
	char c;
	while(f.get(c))
	{
		if( c == ',')
		{
			right = buf;
			buf = "";
			key1 += part_1(left, right);
			key2 += part_2(left, right);
		}
		else if( c == '-')
		{
			left = buf;
			buf = "";
		}
		else
			buf += c;
	}

	std::cout << "part 1:" << key1 << std::endl;
	std::cout << "part 2:" << key2 << std::endl;
}

// 39832618337