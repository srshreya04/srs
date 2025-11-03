#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    int rank;
    int data1 = 100, data2 = 200;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        MPI_Send(&data1, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
        printf("Process 0 sent first message with tag 0\n");

        MPI_Send(&data2, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
        printf("Process 0 sent second message with tag 1\n");
    }
    else if (rank == 1) {
        int recv1, recv2;

        MPI_Recv(&recv2, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
        printf("Process 1 received message with tag 1\n");

        MPI_Recv(&recv1, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
        printf("Process 1 received message with tag 0\n");
    }

    MPI_Finalize();
    return 0;
}
