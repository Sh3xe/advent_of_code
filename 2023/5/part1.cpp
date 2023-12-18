#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <string>
#include <regex>
#include <map>

using u64 = uint64_t;

struct ValueMap
{
	u64 key_begin;
	u64 value_begin;
	u64 range_len;
};

std::map< std::string, std::vector<ValueMap> > mapping;
std::vector< std::pair<u64, u64> > seeds;

void parse_input( const std::string &path )
{
	std::fstream file {path, std::ios::in};

	std::string line;
	std::getline(file, line);

	std::regex reg("\\d+");
    auto words_begin = std::sregex_iterator(line.begin(), line.end(), reg);
    auto words_end = std::sregex_iterator();
	for(auto it = words_begin; it != words_end; ++it)
	{
		std::cout << it->str() << std::endl;
	}

	file.close();
}