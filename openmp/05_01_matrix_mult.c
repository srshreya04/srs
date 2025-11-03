#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

int main() {
    int sizes[] = {2, 3, 4};
    int threads[] = {10, 15, 20};
    int nsizes = sizeof(sizes) / sizeof(sizes[0]);
    int nthreads = sizeof(threads) / sizeof(threads[0]);

    srand(42); 

    for (int s = 0; s < nsizes; s++) {
        int n = sizes[s];

        double *A = (double *)malloc(n * n * sizeof(double));
        double *B = (double *)malloc(n * n * sizeof(double));
        double *C = (double *)malloc(n * n * sizeof(double));

        for (int i = 0; i < n * n; i++) {
            A[i] = rand() % 10;
            B[i] = rand() % 10;
        }

        printf("\nMatrix Size: %d x %d\n", n, n);

        for (int t = 0; t < nthreads; t++) {
            int thread_count = threads[t];
            omp_set_num_threads(thread_count);

            for (int i = 0; i < n * n; i++)
                C[i] = 0;

            double start_time = omp_get_wtime();

            #pragma omp parallel for schedule(static)
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < n; k++) {
                        C[i * n + j] += A[i * n + k] * B[k * n + j];
                    }
                }
            }

            double end_time = omp_get_wtime();
            printf("Threads: %d, Time: %f seconds\n", thread_count, end_time - start_time);
        }

        free(A);
        free(B);
        free(C);
    }

    return 0;
}
