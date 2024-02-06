#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

sem_t s, t;
int a[32];
int i = 0, j = 0;

void *P0(void *arg) {
    while (i < 32) {
	sem_wait(&s);
        a[i] = j;
        sem_post(&t);
        ++i;
    }
    pthread_exit(NULL);
}

void *P1(void *arg) {
    while (j < 32) {
        sem_wait(&t);
        ++j;
        sem_post(&s);
    }
    pthread_exit(NULL);
}

int main() {
    sem_init(&s, 0, 0);
    sem_init(&t, 0, 1);

    pthread_t thread_P0, thread_P1;

    pthread_create(&thread_P0, NULL, P0, NULL);
    pthread_create(&thread_P1, NULL, P1, NULL);

    pthread_join(thread_P0, NULL);
    pthread_join(thread_P1, NULL);

    // Imprimir el array a[]
    printf("Contenido del array a[] después de ejecutar P0 y P1:\n");
    for (int k = 0; k < 32; ++k) {
        printf("%d ", a[k]);
    }
    printf("\n");

    sem_destroy(&s);
    sem_destroy(&t);

    return 0;
}
