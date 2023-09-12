#include <stdio.h>

/**
 * Prints the sign of a number and
 * returns a corresponding value.
 *
 * @param n The number to check the sign of.
 * @return 1 and prints '+' if n is greater
 * than zero 0 and prints '0' if n is zero.
 * -1 and prints '-' if n is less than zero.
 */
int print_sign(int n)
{
	if (n > 0)
	{
		printf("+");
		return (1);
	}
	else if (n == 0)
	{
		printf("0");
		return (0);
	}
	else
	{
		printf("-");
		return (-1);
	}
}