#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"


/**
 * insert_node - check the code for
 * @head: head of node
 * @number: number to insert
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *temp;

	current = *head;
	new = NULL;
	temp = NULL;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	if (*head == NULL)
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}

	if (current->n > number)
	{
		new->n = number;
		new->next = current;
		*head = new;
		return (*head);
	}

	while (current->n < number || current->next != NULL)
	{
		if (current->next->n >= number)
			break;
		current = current->next;
	}

	new->n = number;
	temp = current->next;
	current->next = new;
	new->next = temp;

	return (NULL);
}
