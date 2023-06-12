#include "lists.h"
#include <stdio.h>

/**
 * palindrome_recursive - recursively check if it is a palindrome
 *
 * @h: pointer to left node
 * @n: right node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int palindrome_recursive(listint_t **h, listint_t *n)
{
	int i;

	if (n == NULL)
		return (1);
	i = palindrome_recursive(h, n->next);
	if (i == 0)
		return (0);
	i = (n->n == (*h)->n);
	*h = (*h)->next;

	return (i);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: pointer to the list head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	return (palindrome_recursive(head, *head));
}
