#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

int main() {
    int sizes[] = {10, 100, 1000};   
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
    int threads[] = {2, 4, 8};        
    int num_threads = sizeof(threads) / sizeof(threads[0]);

    srand(42);  

    for (int s = 0; s < num_sizes; s++) {
        int n = sizes[s];
        int *arr = (int *)malloc(n * sizeof(int));
        int *prefix = (int *)malloc(n * sizeof(int));

        for (int i = 0; i < n; i++)
            arr[i] = rand() % 10;

        printf("\nArray Size: %d\n", n);

        for (int t = 0; t < num_threads; t++) {
            int thread_count = threads[t];
            omp_set_num_threads(thread_count);

            int *temp = (int *)malloc(n * sizeof(int));
            for (int i = 0; i < n; i++)
                prefix[i] = arr[i]; 
            double start_time = omp_get_wtime();

            int d;
            for (d = 1; d < n; d *= 2) {
                #pragma omp parallel for schedule(static)
                for (int i = 0; i < n; i++) {
                    if (i >= d)
                        temp[i] = prefix[i] + prefix[i - d];
                    else
                        temp[i] = prefix[i];
                }
                #pragma omp parallel for schedule(static)
                for (int i = 0; i < n; i++)
                    prefix[i] = temp[i];
            }

            double end_time = omp_get_wtime();
            printf("  Threads=%d, Time=%f sec\n", thread_count, end_time - start_time);

            free(temp);
        }

        free(arr);
        free(prefix);
    }

    return 0;
}
