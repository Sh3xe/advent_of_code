#pragma once

#include <stdint.h>
#include <stdbool.h>

typedef enum step_types_t
{
	STEP_ACCEPTED,
	STEP_REJECTED,
	STEP_JUMP,
	STEP_OPERATOR
} step_types_t;

typedef struct step_t
{
	// the variable on which the operation is performed
	char var;
	// the operation to perform
	char op;
	// the next step's name
	char *name;
	// the value to compare to
	uint64_t value;
	// the type of step
	step_types_t type;
	// the type of the operation to perform in case where type == STEP_OPERATOR
	step_types_t op_type;
} step_t;

typedef struct object_t
{
	uint64_t s;
	uint64_t a;
	uint64_t m;
	uint64_t x;
} object_t;

typedef struct workflow_t
{
	char *name;
	uint32_t step_count;
	step_t *steps;
} workflow_t;

bool parse_object(const char *line, object_t *out);

bool parse_step(const char *str, step_t *out);

bool parse_workflow(const char *line, workflow_t *out);

bool parse_input( const char *path, workflow_t **workflow_lst, object_t **obj_lst );