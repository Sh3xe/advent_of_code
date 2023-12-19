#include <stdio.h>
#include <stdlib.h>
#include "aoc.h"

bool test()
{
	object_t obj;
	bool ok = parse_object("{x=30,m=12,a=1223,s=1089}", &obj);

	printf("%ld %ld %ld %ld %d\n", obj.a, obj.m, obj.s, obj.x, ok);

	return true;
}

int main()
{
	/*
	workflow_t *workflows;
	object_t *objects;
	bool res = parse_input("test_input.txt", &workflows, &objects);

	if(!res)
	{
		printf("impossible de récupérer l'entrée");
		return 1;
	}

	if( !test() )
	{
		printf("Tests non passées");
		return -1;
	}
	*/
	parse_input("", NULL, NULL);

	return 0;
}