#include <stdio.h>
#include <math.h>
#include <omp.h>

int main() {
    double x;
    printf("Enter value of x: ");
    scanf("%lf", &x);

    double result_seq, result_spec;
    double start, end;
    double seq_time, par_time;

    int p_values[] = {2, 4, 8};
    int num_cases = 3;

    printf("\nSequential Execution:\n");

    start = omp_get_wtime();
    if (x > 0)
        result_seq = sqrt(x);
    else
        result_seq = log(fabs(x));
    end = omp_get_wtime();

    seq_time = (end - start) * 1000.0;
    printf("Result = %.6f, Time = %.2f ms\n\n", result_seq, seq_time);

    printf("p threads\tParallelTime(ms)\tSpeedup\t\tWastedComp(%%)\n");

    for (int i = 0; i < num_cases; i++) {
        int p = p_values[i];
        omp_set_num_threads(p);

        double sqrt_val = 0.0, log_val = 0.0;
        start = omp_get_wtime();

        #pragma omp parallel sections
        {
            #pragma omp section
            {
                sqrt_val = sqrt(fabs(x));
            }
            #pragma omp section
            {
                log_val = log(fabs(x));
            }
        }

        if (x > 0)
            result_spec = sqrt_val;
        else
            result_spec = log_val;

        end = omp_get_wtime();
        par_time = (end - start) * 1000.0;

        double speedup = seq_time / par_time;
        double wasted = 50.0; 

        printf("%d\t\t%.2f\t\t\t%.2f\t\t%.2f\n", p, par_time, speedup, wasted);
    }

    return 0;
}
