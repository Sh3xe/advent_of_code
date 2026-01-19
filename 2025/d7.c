#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

void print_mat(int *mat, int length)
{
	for(int i = 0; i < length; ++i)
	{
		for(int j = 0; j < length; ++j)
		{
			printf("%d ", mat[i*length+j]);
		}
		printf("\n");
	}
}

int part_1(int *mat, int length, int initial_position)
{
	// create a mask of the current waterfalls
	int *curr_mask = malloc(length*sizeof(int));
	int *new_mask = malloc(length*sizeof(int));
	memset(curr_mask, 0, length*sizeof(int));
	curr_mask[initial_position] = 1;

	int num_splits = 0;
	for(int i = 0; i < length; ++i)
	{
		// reset the next mask
		memset(new_mask, 0, length*sizeof(int));

		// construct the next mask
		for(int j = 0; j < length; ++j)
		{
			// printf("%d,%d (%d,%d)\n", i, j, curr_mask[j], mat[i*length + j]);
			if( curr_mask[j] == 1 && mat[i*length + j] == (int)'^' )
			{
				assert(j >= 1 && j < length-1);
				new_mask[j-1] = 1;
				new_mask[j+1] = 1;
				++num_splits;
			}
			else if( curr_mask[j] == 1 )
			{
				new_mask[j] = 1;
			}
		}

		// swap the masks
		memcpy(curr_mask, new_mask, length*sizeof(int));
	}

	free(curr_mask);
	free(new_mask);
	return num_splits;
}

uint64_t part_2(int *mat, int length, int initial_position)
{
	// create a mask of the current waterfalls
	uint64_t *curr_mask = malloc(length*sizeof(uint64_t));
	uint64_t *new_mask = malloc(length*sizeof(uint64_t));
	memset(curr_mask, 0, length*sizeof(uint64_t));
	curr_mask[initial_position] = 1;

	for(int i = 0; i < length; ++i)
	{
		// reset the next mask
		memset(new_mask, 0, length*sizeof(uint64_t));

		// construct the next mask
		for(int j = 0; j < length; ++j)
		{
			if( curr_mask[j] >= 1 && mat[i*length + j] == (int)'^' )
			{
				new_mask[j-1] += curr_mask[j];
				new_mask[j+1] += curr_mask[j];
			}
			else
			{
				new_mask[j] += curr_mask[j];
			}
		}

		// swap the masks
		memcpy(curr_mask, new_mask, length*sizeof(uint64_t));
	}

	uint64_t num_timelines = 0;
	for(int i = 0; i < length;++i)
		num_timelines += curr_mask[i];
	free(curr_mask);
	free(new_mask);
	return num_timelines;
}

int main()
{
	// IO ...
	FILE *f = fopen("./inputs/7.txt", "r");
	if (f == NULL)
	{
		printf("Cannot open the input\n");
		return -1;
	}

	// Scan the first line (contains info about initial position and size of the matrix)
	int *mat = NULL;
	int initial_position = -1;
	int length = -1;
	int c;
	for( int i = 0;i < 1000;++i )
	{
		c = fgetc(f);
		if( c == (int)'S' )
			initial_position = i;
		if( c == (int)'\n')
		{
			length = i;
			mat = malloc(length*length*sizeof(int));
			break;
		}
	}

	// Scan the rest
	for(int i = 0; i < length; ++i)
	{
		for(int j = 0; j < length; ++j)
		{
			c = fgetc(f);
			mat[i*length+j] = c;
		}
		// ignore the newline
		fgetc(f);
	}

	int key_1 = part_1(mat, length, initial_position);
	uint64_t key_2 = part_2(mat, length, initial_position);

	printf("Key 1: %d\nKey 2: %ld\n", key_1, key_2);
	free(mat);
	return 0;
}