#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

#define N 10

sem_t s, t;
int a[N];
int i = 0, j = 0;

void *P0(void *arg) {
    while (i < N) {
	if (i%2 == 0){sem_wait(&s);}
        a[i] = 0;
        if (i%2 != 0){sem_post(&t);}
        ++i;
    }
    pthread_exit(NULL);
}

void *P1(void *arg) {
    while (j < N) {
        if (j%2 != 0){sem_wait(&t);}
        a[j] = 1; 
        if (j%2 == 0){sem_post(&s);}
        ++j;
    }
    pthread_exit(NULL);
}

int main() {
    sem_init(&s, 0, 0);
    sem_init(&t, 0, 0);

    pthread_t thread_P0, thread_P1;

    pthread_create(&thread_P0, NULL, P0, NULL);
    pthread_create(&thread_P1, NULL, P1, NULL);

    pthread_join(thread_P0, NULL);
    pthread_join(thread_P1, NULL);

    // Imprimir el array a[]
    printf("Contenido del array a[] después de ejecutar P0 y P1:\n");
    for (int k = 0; k < N; ++k) {
        printf("%d ", a[k]);
    }
    printf("\n");

    sem_destroy(&s);
    sem_destroy(&t);

    return 0;
}
