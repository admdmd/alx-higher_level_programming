#include "lists.h"

/**
 * check_cycle - checks for cycle in linked list
 * @list: subject linked list
 * Return: 1 if cycle exists, otherwise 0
**/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
