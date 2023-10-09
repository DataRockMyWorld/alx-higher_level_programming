#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * *reverse_listint - reverses a linked list.
 * @head: pointer to the first element in the list
 *
 *
 * Return: 1 (Success), or -1 (Fail)
 */
listint_t *reverse_listint(listint_t *head)
{
	listint_t *prev, *step;

	prev = NULL;
	step = NULL;

	while (head != NULL)
	{
		step = (head)->next;
		(head)->next = prev;
		prev = (head);
		(head) = step;
	}

	(head) = prev;

	return (head);
}
/**
 * is_palindrome - check the code for
 * @head: linked list
 *
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp_s = *head;
	listint_t *temp_f = *head;
	listint_t *temp = *head, *sec_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (temp_f->next != NULL && temp_f->next->next != NULL)
	{
		temp_s = temp_s->next;
		temp_f = temp_f->next->next;
	}

	temp_s->next = reverse_listint(temp_s->next);
	sec_half = temp_s->next;

	while (sec_half != NULL)
	{
		if (sec_half->n != temp->n)
		{
			return (0);
		}
		sec_half = sec_half->next;
		temp = temp->next;
	}
	temp_s->next = reverse_listint(temp_s->next);
	return (1);
}
