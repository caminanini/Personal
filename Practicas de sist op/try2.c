#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define L 20

int main(int argc, char **argv) {
    char buf[L] = {"\0"};

    if (argc <= 1) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 0;
    }

    int rc = fork();

    if (rc < 0) {
        perror("Error in fork");
        return -1;
    }

    if (rc == 0) {
        // Proceso hijo
        close(0);
        if (open(argv[1], 0) < 0) {
            perror("Error opening file in child process");
            return -1;
        }

        read(0, buf, L);
        write(1, buf, L);
    } else {
        // Proceso padre
        argv[argc - 1] = NULL;
        if (execvp(argv[1], argv + 1) < 0) {
            perror("Error in execvp");
            return -1;
        }
    }

    return 0;
}
