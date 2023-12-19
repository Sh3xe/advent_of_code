#include "aoc.h"
#include <stdio.h>
#include <string.h>
#include <regex.h>
#include <stdlib.h>

static char buffer[512];
static regex_t workflow_cmp;

bool parse_object(const char *line, object_t *out)
{
	int res = sscanf(line,
		"{x=%ld,m=%ld,a=%ld,s=%ld}", 
		&out->x,
		&out->m,
		&out->a,
		&out->s
	);
	return res == 4;
}

bool parse_step(const char *str, step_t *out)
{
	int res = regexec(&workflow_cmp, str, 0, NULL, 0);
	if(res != REG_NOMATCH)
	{
		out->type = STEP_OPERATOR;

	}
	else if (str[0] == 'A')
	{
		out->type = STEP_ACCEPTED;
	}
	else if (str[0] == 'R')
	{
		out->type = STEP_REJECTED;
	}
	else
	{
		out->type = STEP_JUMP;
		int length = strlen(str);
		out->name = (char*)malloc(sizeof(char) * (length+1));
		strcpy(out->name, str);
	}
	return true;
}

bool parse_workflow(const char *line, workflow_t *out)
{
	return false;
}

bool parse_input( const char *path, workflow_t **workflow_lst, object_t **obj_lst )
{
	int res = regcomp(&workflow_cmp, "([a-z]+)(<|>)(\\d+):(R|A|[a-z]+)", REG_EXTENDED);

	regmatch_t matches[2];
	matches[0].rm_eo=-1;
	matches[0].rm_so=-1;
	matches[1].rm_eo=-1;
	matches[1].rm_so=-1;
	int rb = regexec(&workflow_cmp, "aazbd<998:R", 2, matches, 0);
	printf("%d %d\n", matches[0].rm_eo, matches[0].rm_so);
	printf("%d %d\n", matches[1].rm_eo, matches[1].rm_so);
	printf("%d\n", rb);

	if (res != 0) return false;

	regfree(&workflow_cmp);
	return false;
}