#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_whilw - Creates an infinite loop with a sleeo of 1 seconds
 * in each iteration
 * Return: Always 0
 */

int infinite_while(void) {
    while (1) {
        sleep(1);
    }
    return (0);
}

/**
 * main - Entry point of the program
 * Return: Always returns 0
 */

int main(void) {
    pid_t child_pid;

    for (int i = 0; i < 5; i++) {
        child_pid = fork();

        if (child_pid == 0) {
            printf("Zombie process created, PID: %d\n", getpid());
            exit(0);
        } else if (child_pid < 0) {
            perror("Fork failed");
            exit(1);
        }
    }

    infinite_while();

    return (0);
}

