#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = NULL;

	if (list == NULL)
	{
		return (0);
	}

	temp = list;

	while (temp->next != NULL)
	{
		if (temp->next == list)
		{
			return (1);
		}
		else
		{
			temp = temp->next;
		}

	}
	return (0);
}
