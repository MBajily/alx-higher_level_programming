#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


typedef struct listint_s
{
	struct listint_s *next;
	int n;
} list_t;


void reverse_list(list_t **head);
int is_palindrome(list_t **head);

size_t print_listint(const list_t *h);
listint_t *add_nodeint_end(list_t **head, const int n);
void free_listint(list_t *head);


#endif /* LISTS_H */
