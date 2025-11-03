#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

int main() {
    int n = 0;
    int threads;
    float scalar = 2.5;
    float *vec, *res;

    printf("Enter vector size: ");
    scanf("%d", &n);

    printf("Enter number of threads: ");
    scanf("%d", &threads);

    vec = (float*)malloc(n * sizeof(float));
    res = (float*)malloc(n * sizeof(float));

    srand(time(NULL)); // used to make different random numbers every time we run the program

    for (int i = 0; i < n; i++) {
        vec[i] = rand() % 100;
    }

    // printf("Original Vector: ");
    // for (int i = 0; i < n; i++) {
    //     printf("%.1f ", vec[i]);
    // }
    // printf("\nScalar to add: %.1f\n", scalar);
    
    omp_set_num_threads(threads);
    double start = omp_get_wtime();

    #pragma omp parallel for
    for (int i = 0; i < n; i++) {
        res[i] = vec[i] + scalar;
    }

    double end = omp_get_wtime();

    // printf("Result Vector: ");
    // for (int i = 0; i < n; i++) {
    //     printf("%.1f ", res[i]);
    // }
    printf("\nTime taken with %d threads for %d data size: %.6f seconds\n", threads, n, end - start);

    free(vec);
    free(res);
    return 0;
}
