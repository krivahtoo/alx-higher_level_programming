#include "lists.h"
#include <stdint.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node1, *node2;

	if (list == NULL)
		return (0);
	if (list->next && list->next->next)
		node2 = list->next->next;
	else
		return (0);
	node1 = list;
	while (node1->next && (node2->next && node2->next->next))
	{
		if ((uintptr_t)node1 == (uintptr_t)node2)
			return (1);
		node2 = node2->next->next;
		node1 = node1->next;
	}
	return (0);
}
