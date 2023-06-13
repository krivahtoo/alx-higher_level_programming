#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer to linked list head
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *old = NULL, *tmp = *head;

	while (tmp && tmp->n < number)
	{
		old = tmp;
		tmp = tmp->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (tmp != NULL)
		new->next = tmp;
	if (old == NULL)
		*head = new;
	else
		old->next = new;

	return (new);
}
