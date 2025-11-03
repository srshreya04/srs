#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

void generate_matrix(int **mat, int n) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            mat[i][j] = rand() % 100;
}

void matrix_add(int **A, int **B, int **C, int n, int threads) {
    #pragma omp parallel for collapse(2) num_threads(threads)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
}

int main() {
    int sizes[] = {250, 500, 750, 1000, 2000};
    int thread_counts[] = {1, 2, 4, 8};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
    int num_threads = sizeof(thread_counts) / sizeof(thread_counts[0]);
    double base_time; // time for 1 thread

    srand(time(NULL));

    for (int s = 0; s < num_sizes; s++) {
        int n = sizes[s];
        printf("\n--- Matrix Size: %d x %d ---\n", n, n);

        int **A = malloc(n * sizeof(int *));
        int **B = malloc(n * sizeof(int *));
        int **C = malloc(n * sizeof(int *));
        for (int i = 0; i < n; i++) {
            A[i] = malloc(n * sizeof(int));
            B[i] = malloc(n * sizeof(int));
            C[i] = malloc(n * sizeof(int));
        }

        generate_matrix(A, n);
        generate_matrix(B, n);

        for (int t = 0; t < num_threads; t++) {
            int threads = thread_counts[t];
            double start = omp_get_wtime();

            matrix_add(A, B, C, n, threads);

            double end = omp_get_wtime();
            double time_taken = end - start;

            if (threads == 1) {
                base_time = time_taken; 
            }

            double speedup = base_time / time_taken;
            printf("Threads: %d, Time: %.6f s, Speedup: %.2f\n",
                   threads, time_taken, speedup);
        }

        for (int i = 0; i < n; i++) {
            free(A[i]);
            free(B[i]);
            free(C[i]);
        }
        free(A);
        free(B);
        free(C);
    }

    return 0;
}
