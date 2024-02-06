#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>


sem_t s, t;
int n=0;

void *P0(void *arg) {
    while (n<100) {
	sem_wait(&s);
        n=n*2;
        sem_post(&t);
    }
    pthread_exit(NULL);
}

void *P1(void *arg) {
    while (n<100) {
        sem_wait(&t);
        n=n+1;
        sem_post(&s);
    }
    pthread_exit(NULL);
}

int main() {
    sem_init(&s, 0, 0);
    sem_init(&t, 0, 100);

    pthread_t thread_P0, thread_P1;

    pthread_create(&thread_P0, NULL, P0, NULL);
    pthread_create(&thread_P1, NULL, P1, NULL);

    pthread_join(thread_P0, NULL);
    pthread_join(thread_P1, NULL);

    printf("%d \n",n);

    sem_destroy(&s);
    sem_destroy(&t);

    return 0;
}
