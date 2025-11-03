#include <stdio.h>
#include <omp.h>

int main() {
    int size, n;

    printf("Enter buffer size: ");
    scanf("%d", &size);

    printf("Enter number of items to produce/consume: ");
    scanf("%d", &n);

    int buffer[size];
    int count = 0; 
    #pragma omp parallel sections shared(buffer, count)
    {
        #pragma omp section
        {
            for (int i = 1; i <= n; i++) {
                int produced = 0;
                while (!produced) {
                    #pragma omp critical
                    {
                        if (count < size) {
                            buffer[count] = i;
                            count++;
                            printf("Producer produced: %d | Buffer count: %d\n", i, count);
                            produced = 1;
                        } else {
                            printf("Producer waiting - Buffer full\n");
                        }
                    }
                    #pragma omp flush(buffer, count)
                }
            }
        }

        #pragma omp section
        {
            for (int i = 1; i <= n; i++) {
                int consumed = 0;
                while (!consumed) {
                    #pragma omp critical
                    {
                        if (count > 0) {
                            int item = buffer[count - 1];
                            count--;
                            printf("Consumer consumed: %d | Buffer count: %d\n", item, count);
                            consumed = 1;
                        } else {
                            printf("Consumer waiting - Buffer empty\n");
                        }
                    }
                    #pragma omp flush(buffer, count)
                }
            }
        }
    }

    return 0;
}
