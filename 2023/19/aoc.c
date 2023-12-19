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
	regmatch_t matches[5];
	int res = regexec(&workflow_cmp, str, 5, matches, 0);
	if(res != REG_NOMATCH)
	{
		out->type = STEP_OPERATOR;
		out->op = str[matches[2].rm_so];
		out->var = str[matches[1].rm_so];
		
		int size = matches[4].rm_eo-matches[4].rm_so;
		char *name = (char*)malloc(sizeof(char)*(size+1));
		if (name == NULL)
		{
			printf("Moi: Cannot allocate memory");
			return false;
		}

		strncpy(name, &str[matches[4].rm_so], size);
		name[size] = '\0';
		out->name = name;

		int scan_count = sscanf(&str[matches[3].rm_so], "%lu", &out->value);

		if (scan_count != 1)
		{
			printf("Moi: Cannot read value");
			return false;
		}

		if(name[0] == 'R')
			out->op_type = STEP_REJECTED;
		if(name[0] == 'A')
			out->op_type = STEP_ACCEPTED;
		else
			out->op_type = STEP_JUMP;
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
	char *line_copy = (char*)malloc(sizeof(char)*(1+strlen(line)));
	strcpy(line_copy, line);
	
	strtok(line_copy, ",");

	return false;
}

bool parse_input( const char *path, workflow_t **workflow_lst, object_t **obj_lst )
{
	int res = regcomp(&workflow_cmp, "([a-z]+)(<|>)([0-9]+):(R|A|[a-z]+)", REG_EXTENDED);
	if (res != 0) return false;

	regfree(&workflow_cmp);
	return false;
}