#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
    int limite = 0;

    while (1) {
        int rc = fork();
        
        if (rc < 0) {
            fprintf(stderr, "Error en fork()\n");
            return -1;
        } else if (rc == 0) {
            // Proceso hijo
            fprintf(stderr, "Hijo: %s , %s\n", argv[0], argv[1]);
            limite = limite + 1;
            if (limite == 10) {
                fprintf(stderr, "Hijo alcanzó el límite. Saliendo.\n");
                exit(0); // Puedes proporcionar un código de salida aquí
            }
            execvp(argv[0], argv);
            fprintf(stderr, "Error en execvp()\n");
        } else {
            // Proceso padre
            fprintf(stderr, "Padre: %s , %s\n", argv[0], argv[1]);
            limite = limite + 1;
            if (limite == 10) {
                fprintf(stderr, "Padre alcanzó el límite. Saliendo.\n");
                exit(0); // Puedes proporcionar un código de salida aquí
            }
            waitpid(rc, NULL, 0); // Esperar a que el proceso hijo termine
            execvp(argv[0], argv);
            fprintf(stderr, "Error en execvp()\n");
        }
    }

    return 0;
}
