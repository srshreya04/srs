#include <stdio.h>
#include <omp.h>

int main() {
    int threads;
    long n;

    printf("Enter number of threads: ");
    scanf("%d", &threads);

    printf("Enter data size (number of intervals): ");
    scanf("%ld", &n);
    // divide the interval 0 to 1 in n equal parts
    double step = 1.0 / (double)n;
    double sum = 0.0, pi = 0.0;

    omp_set_num_threads(threads);
    double start = omp_get_wtime();

    #pragma omp parallel for reduction(+:sum)
    for (long i = 0; i < n; i++) {
        double x = (i + 0.5) * step;
        sum += 4.0 / (1.0 + x * x);
    }
    // height = x, width = step
    pi = sum * step;
    double end = omp_get_wtime();

    printf("Threads\tDataSize\tPi Value\tTime(s)\n");
    printf("%d\t%ld\t%.15f\t%f\n", threads, n, pi, end - start);

    return 0;
}
