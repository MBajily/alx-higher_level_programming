#include "lists.h"


void reverse_list(listint_t **head)
{
	listint_t *pr = NULL;
	listint_t *cur = *head;
	listint_t *nx = NULL;

	while (cur)
	{
		nx = cur->next;
		cur->next = pr;
		pr = cur;
		cur = nx;
	}
	
	*head = pr;
}


int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *t = *head, *d = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			d = s->next;
			break;
		}
		if (!f->next)
		{
			d = s->next->next;
			break;
		}
		s = s->next;
	}
	reverse_list(&d);
	while (d && t)
	{
		if (t->n == d->n)
		{
			d = d->next;
			t = t->next;
		}
		else
		{
			return (0);
		}
	}
	if (!d)
	{
		return (1);
	}
	return (0);
}
