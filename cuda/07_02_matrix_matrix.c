#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

void MatrixMultiply(int n, double *A, double *B, double *C, MPI_Comm comm) {
    int nlocal;
    double *buffB;
    int np, myrank;
    MPI_Comm_size(comm, &np);
    MPI_Comm_rank(comm, &myrank);

    buffB = (double *)malloc(n * n * sizeof(double));
    for (int i = 0; i < n*n; i++) buffB[i] = 0.0;

    MPI_Bcast(B, n*n, MPI_DOUBLE, 0, comm);

    nlocal = n / np;  

    for (int i = 0; i < nlocal; i++) {
        for (int j = 0; j < n; j++) {
            C[i*n + j] = 0.0;
            for (int k = 0; k < n; k++) {
                C[i*n + j] += A[i*n + k] * B[k*n + j];
            }
        }
    }

    free(buffB);
}

int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int n = 1000;
    int nlocal = n / size;

    double *A = (double *)malloc(nlocal * n * sizeof(double)); 
    double *B = (double *)malloc(n * n * sizeof(double));    
    double *C = (double *)malloc(nlocal * n * sizeof(double));

    for (int i = 0; i < nlocal; i++) {
        for (int j = 0; j < n; j++) {
            A[i*n + j] = rank*nlocal + i + j + 1;  
        }
    }
    if (rank == 0) {
        for (int i = 0; i < n*n; i++) {
            B[i] = 1.0; 
        }
    }

    MPI_Barrier(MPI_COMM_WORLD);
    double start = MPI_Wtime();

    MatrixMultiply(n, A, B, C, MPI_COMM_WORLD);

    MPI_Barrier(MPI_COMM_WORLD);
    double end = MPI_Wtime();

    if (rank == 0) {
        printf("Execution time: %f\n", end - start);
    }

    free(A);
    free(B);
    free(C);

    MPI_Finalize();
    return 0;
}
