#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <string>
#include <regex>
#include <map>
#include <unordered_map>
#include <sstream>
#include <chrono>
#include <algorithm>

// 1st iteration:
// 264.191   secs = 4min 24sec

// 2nd iteration:
// 0.0019534 secs = 1.9ms

using u64 = uint64_t;
using namespace std::chrono_literals;
using fsec = std::chrono::duration<float>;

struct ValueMap
{
	ValueMap() = default;
	ValueMap( u64 key_begin, u64 value_begin, u64 range_len) :
		key_begin(key_begin), value_begin(value_begin), range_len(range_len) {}
	u64 key_begin;
	u64 value_begin;
	u64 range_len;
};

//std::unordered_map< std::string, std::vector<ValueMap> > mapping;
std::vector < std::vector<ValueMap> > mapping;
std::vector< std::pair<u64, u64> > seeds;

u64 min(u64 a, u64 b)
{
	return a < b ? a : b;
}

std::vector< std::tuple<u64, u64, bool> > cut_interval(u64 beg, u64 len, const ValueMap &map)
{
	std::vector< std::tuple<u64, u64, bool> > intervals;
	
	// no cut
	if (beg >= map.key_begin + map.range_len || beg + len <= map.key_begin)
		intervals.emplace_back(beg, len, false);
	else if (beg >= map.key_begin && beg + len <= map.key_begin + map.range_len )
		intervals.emplace_back(map.value_begin + (beg - map.key_begin), len, true);
	// 2 cuts
	else if (beg < map.key_begin && beg + len > map.key_begin + map.range_len)
	{
		intervals.emplace_back(beg, map.key_begin - beg, false);
		intervals.emplace_back(map.value_begin, map.range_len, true);
		intervals.emplace_back(map.key_begin + map.range_len, beg + len - (map.key_begin + map.range_len), false);
	}
	// 1 cut
	else if (beg >= map.key_begin)
	{
		intervals.emplace_back(map.value_begin + (beg - map.key_begin), map.key_begin + map.range_len - beg, true);
		intervals.emplace_back(map.key_begin + map.range_len, beg + len - (map.key_begin + map.range_len), false);
	}
	else
	{
		intervals.emplace_back(map.value_begin, beg + len - map.key_begin, true);
		intervals.emplace_back(beg, map.key_begin - beg, false);
	}

	return intervals;
}

std::vector< std::pair<u64, u64> > split_interval(int id, u64 beg, u64 len)
{
	std::vector < std::tuple<u64, u64, bool> > intervals;

	intervals.emplace_back(beg, len, false);

	for (const auto& inter : mapping[id])
	{
		std::vector < std::tuple<u64, u64, bool> > new_intervals;
		for (const auto& [ibeg, ilen, mapped] : intervals)
		{
			if (mapped)
			{
				new_intervals.emplace_back(ibeg, ilen, true);
				continue;
			}
			auto split = cut_interval(ibeg, ilen, inter);
			new_intervals.insert(new_intervals.end(), split.begin(), split.end());
		}
		intervals = new_intervals;
	}

	std::vector < std::pair<u64, u64> > return_value;
	for (const auto& [ibeg, ilen, _] : intervals)
		return_value.emplace_back(ibeg, ilen);
	return return_value;
}

std::vector< std::pair<u64, u64> > split_intervals(int id, const std::vector< std::pair<u64, u64> > &intervals )
{
	std::vector < std::pair<u64, u64> > res;

	for (const auto& [beg, len] : intervals)
	{
		auto split = split_interval(id, beg, len);
		res.insert(res.begin(), split.begin(), split.end());
	}

	return res;
}

void parse_input(const std::string& path)
{
	std::fstream file{ path, std::ios::in };

	std::string line;
	std::getline(file, line);

	std::stringstream ss;

	std::regex reg("\\d+ \\d+");
	auto words_begin = std::sregex_iterator(line.begin(), line.end(), reg);
	auto words_end = std::sregex_iterator();
	for (auto it = words_begin; it != words_end; ++it)
	{
		u64 v0, v1;
		ss << it->str();
		ss >> v0 >> v1;
		ss.clear();
		seeds.push_back(std::pair<u64, u64>(v0, v1));
	}

	std::vector< ValueMap > current_values;
	std::string current_key;
	while (std::getline(file, line))
	{
		if (line.size() == 0)
			continue;

		current_key = line;
		while (std::getline(file, line))
		{
			ValueMap map;
			if (line.size() == 0)
			{
				mapping.push_back( current_values );
				current_values.clear();
				break;
			}
			else
			{
				std::stringstream ss(line);
				ss >> map.value_begin >> map.key_begin >> map.range_len;
				current_values.push_back(map);
			}
		}

		if (current_values.size() != 0)
		{
			mapping.push_back(current_values);
			current_values.clear();
		}
	}

	file.close();
}

u64 get_correspondance(int id, u64 key)
{
	for (const auto& v : mapping[id])
	{
		if (v.key_begin <= key && key < v.key_begin + v.range_len)
			return v.value_begin + (key - v.key_begin);
	}
	return key;
}

u64 get_min_loc(u64 beg, u64 range)
{
	std::vector < std::pair<u64, u64> > intervals { std::pair<u64, u64>(beg, range) };

	for (int i = 0; i < 7; ++i)
	{
		intervals = split_intervals(i, intervals);
	}

	u64 mini = std::numeric_limits<u64>::max();
	for (const auto& [beg, len] : intervals)
	{
		mini = min(beg, mini);
	}

	return mini;
}

u64 get_location(u64 seed)
{
	u64 res = seed;
	for (int i = 0; i < 7; ++i)
	{
		res = get_correspondance(i, res);
	}
	return res;
}

u64 calculate_min(u64 beg, u64 range, u64 maximum)
{
	u64 minimum = std::numeric_limits<u64>::max();
	for (u64 seed = beg; seed < beg + range && seed < maximum; ++seed)
	{
		minimum = min(get_location(seed), minimum);
	}
	return minimum;
}

int main()
{
	parse_input("input");

	/*ValueMap vm1{ 11, 100, 8 };
	ValueMap vm2{ 0, 100, 9 };
	ValueMap vm3{ 5, 100, 10 };
	ValueMap vm4{ 15, 100, 10 };

	auto res0 = cut_interval(10, 10, vm1);
	auto res1 = cut_interval(10, 10, vm2);
	auto res2 = cut_interval(10, 10, vm3);
	auto res3 = cut_interval(10, 10, vm4);*/

	auto t0 = std::chrono::steady_clock::now();

	u64 minimum = std::numeric_limits<u64>::max();
	for(const auto &[beg, len] : seeds)
	{
		minimum = min(get_min_loc(beg, len), minimum);
	}

	auto t1 = std::chrono::steady_clock::now();
	std::cout << fsec(t1 - t0).count() << "sec" << std::endl;
	std::cout << minimum << std::endl;

	return 0;
}