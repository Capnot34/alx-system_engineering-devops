#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Infinite while loop that sleeps
 * for 1 second in each iteration.
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Creates 5 zombie processes.
 * Return: Always 0.
 */
int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 7; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
			printf("Zombie process created, PID: %d\n", child_pid);
		else
			exit(0);
	}
	infinite_while();

	return (0);
}
