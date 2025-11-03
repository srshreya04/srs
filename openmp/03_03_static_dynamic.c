#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

int main() {
    int threads = 5;        
    float scalar = 2.5;     

    int sizes[]  = {200, 500, 1000, 5000};   
    int chunks[] = {1, 5, 10, 20};            
    int numSizes  = sizeof(sizes) / sizeof(sizes[0]);
    int numChunks = sizeof(chunks) / sizeof(chunks[0]);

    srand(time(NULL));

    for (int s = 0; s < numSizes; s++) {
        int size = sizes[s];
        float *vector = (float *)malloc(size * sizeof(float));
        float *result = (float *)malloc(size * sizeof(float));

        for (int i = 0; i < size; i++) {
            vector[i] = (float)(rand() % 100);
        }

        printf("\n----------- Vector size: %d -----------\n", size);

        double start_seq = omp_get_wtime();
        for (int i = 0; i < size; i++) {
            result[i] = vector[i] + scalar;
        }
        double end_seq = omp_get_wtime();
        double seq_time = end_seq - start_seq;

        printf("Sequential Time: %f sec\n", seq_time);

        for (int c = 0; c < numChunks; c++) {
            int chunk = chunks[c];

            double start = omp_get_wtime();
            #pragma omp parallel num_threads(threads)
            {
                #pragma omp for schedule(static, chunk) nowait
                for (int i = 0; i < size; i++) {
                    result[i] = vector[i] + scalar;
                }
            }
            double end = omp_get_wtime();
            double static_time = end - start;
            double static_speedup = seq_time / static_time;
            printf("STATIC  | Chunk: %4d | Time: %f sec | Speedup: %.2f\n",
                   chunk, static_time, static_speedup);

            start = omp_get_wtime();
            #pragma omp parallel num_threads(threads)
            {
                #pragma omp for schedule(dynamic, chunk) nowait
                for (int i = 0; i < size; i++) {
                    result[i] = vector[i] + scalar;
                }
            }
            end = omp_get_wtime();
            double dynamic_time = end - start;
            double dynamic_speedup = seq_time / dynamic_time;
            printf("DYNAMIC | Chunk: %4d | Time: %f sec | Speedup: %.2f\n",
                   chunk, dynamic_time, dynamic_speedup);
        }

        free(vector);
        free(result);
    }

    return 0;
}
