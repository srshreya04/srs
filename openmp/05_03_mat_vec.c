#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

int main() {
    int sizes[] = {2, 4, 6};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
    int threads[] = {10, 15, 20};
    int num_threads = sizeof(threads) / sizeof(threads[0]);

    srand(0); 

    for (int s = 0; s < num_sizes; s++) {
        int size = sizes[s];
        
        int **matrix = (int **)malloc(size * sizeof(int *));
        int *vector = (int *)malloc(size * sizeof(int));
        int *result = (int *)malloc(size * sizeof(int));

        for (int i = 0; i < size; i++) {
            matrix[i] = (int *)malloc(size * sizeof(int));
        }

        for (int i = 0; i < size; i++) {
            vector[i] = rand() % 10;
            for (int j = 0; j < size; j++) {
                matrix[i][j] = rand() % 10;
            }
        }

        printf("\nMatrix Size: %d x %d\n", size, size);

        for (int t = 0; t < num_threads; t++) {
            int thread_count = threads[t];
            omp_set_num_threads(thread_count);

            for (int i = 0; i < size; i++)
                result[i] = 0;

            double start_time = omp_get_wtime();

            #pragma omp parallel for schedule(static)
            for (int i = 0; i < size; i++) {
                int sum = 0;
                for (int j = 0; j < size; j++) {
                    sum += matrix[i][j] * vector[j];
                }
                result[i] = sum;
            }

            double end_time = omp_get_wtime();

            printf("  Threads=%d, Time=%f sec\n", thread_count, end_time - start_time);
        }

        for (int i = 0; i < size; i++) {
            free(matrix[i]);
        }
        free(matrix);
        free(vector);
        free(result);
    }

    return 0;
}
