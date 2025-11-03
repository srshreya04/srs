#include <stdio.h>
#include <omp.h>

int main() {
    int n;

    printf("Enter the number of threads: ");
    scanf("%d", &n);

    omp_set_num_threads(n);

    for (int i = 0; i < n; i++) {
        printf("Thread No.: %d Hello, World!\n", i);
    }
    printf("---------------\n");
    #pragma omp parallel
    {
        int thread = omp_get_thread_num();
        printf("Thread No.: %d Hello, World!\n", thread);
    }

    return 0;
}
