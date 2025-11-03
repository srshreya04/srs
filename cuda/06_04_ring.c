#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    int rank, size, data;
    int left, right;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    data = 10;
    left  = (rank - 1 + size) % size;   
    right = (rank + 1) % size;          

    if (rank % 2 == 0) {
        MPI_Send(&data, 1, MPI_INT, right, 0, MPI_COMM_WORLD);
        MPI_Recv(&data, 1, MPI_INT, left, 0, MPI_COMM_WORLD, &status);
    } else {
        MPI_Recv(&data, 1, MPI_INT, left, 0, MPI_COMM_WORLD, &status);
        MPI_Send(&data, 1, MPI_INT, right, 0, MPI_COMM_WORLD);
    }

    printf("Process %d sent data to %d and received data from %d\n",
           rank, right, left);

    MPI_Finalize();
    return 0;
}
