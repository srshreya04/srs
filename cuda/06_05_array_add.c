#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    int rank, size;
    const int n = 10;             
    int A[10] = {1,2,3,4,5,6,7,8,9,10};  
    int sum_0 = 0, total_sum = 0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size != 2) {
        if (rank == 0) {
            printf("Please run with 2 processes only.\n");
        }
        MPI_Finalize();
        return 0;
    }

    int half = n / 2;

    if (rank == 0) {
        for (int i = 0; i < half; i++) {
            sum_0 += A[i];
        }
        printf("Sum of first half by process P0 = %d\n", sum_0);

        int recv_sum;
        MPI_Recv(&recv_sum, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        total_sum = sum_0 + recv_sum;

        printf("Final Sum = %d\n", total_sum);
    }
    else if (rank == 1) {
        for (int i = half; i < n; i++) {
            sum_0 += A[i];
        }
        printf("Sum of second half by process P1 = %d\n", sum_0);

        MPI_Send(&sum_0, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
    }

    MPI_Finalize();
    return 0;
}
