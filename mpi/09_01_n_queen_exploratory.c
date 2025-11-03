#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int N; 

int is_safe(int row, int col, int *positions) {
    for (int i = 0; i < row; i++) {
        if (positions[i] == col || abs(positions[i] - col) == abs(i - row))
            return 0;
    }
    return 1;
}

void solve(int row, int *positions, long *nodes, int *solutions) {
    (*nodes)++; 
    if (row == N) {
        (*solutions)++;
        return;
    }
    for (int col = 0; col < N; col++) {
        if (is_safe(row, col, positions)) {
            positions[row] = col;
            solve(row + 1, positions, nodes, solutions);
        }
    }
}

int main() {
    printf("Enter the value of N: ");
    scanf("%d", &N);

    double start_seq = omp_get_wtime();
    int seq_solutions = 0;
    long seq_nodes = 0;
    int *positions = (int *)malloc(N * sizeof(int));
    solve(0, positions, &seq_nodes, &seq_solutions);
    free(positions);
    double end_seq = omp_get_wtime();
    double seq_time_ms = (end_seq - start_seq) * 1000;

    printf("\nSequential Execution:\n");
    printf("Solutions = %d, Time = %.2f ms, Nodes visited = %ld\n", seq_solutions, seq_time_ms, seq_nodes);

    int thread_counts[] = {2, 4, 8}; 
    int num_tests = sizeof(thread_counts) / sizeof(thread_counts[0]);

    printf("\np threads\tParallelTime(ms)\tSpeedup\t\tWastedComp(%%)\n");

    for (int t = 0; t < num_tests; t++) {
        int threads = thread_counts[t];
        omp_set_num_threads(threads);

        int par_solutions = 0;
        long par_nodes = 0;

        double start_par = omp_get_wtime();

        #pragma omp parallel
        {
            int thread_solutions = 0;
            long thread_nodes = 0;

            #pragma omp for schedule(dynamic)
            for (int col = 0; col < N; col++) {
                int *positions = (int *)malloc(N * sizeof(int));
                positions[0] = col;
                solve(1, positions, &thread_nodes, &thread_solutions);
                free(positions);
            }

            #pragma omp atomic
            par_solutions += thread_solutions;

            #pragma omp atomic
            par_nodes += thread_nodes;
        }

        double end_par = omp_get_wtime();
        double par_time_ms = (end_par - start_par) * 1000;
        double speedup = seq_time_ms / par_time_ms;
        double wasted_comp = 100.0 * ((double)par_nodes - (double)seq_nodes) / (double)par_nodes;
        if (wasted_comp < 0)
            wasted_comp = 0.0;
        
        printf("%d\t\t%.2f\t\t\t%.2f\t\t%.2f\n", threads, par_time_ms, speedup, wasted_comp);
    }

    return 0;
}
