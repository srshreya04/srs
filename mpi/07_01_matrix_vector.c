#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

void MatrixVector(int n, double *a, double *b, double *x, MPI_Comm comm){
    int nlocal;
    double *buff;
    int np, myrank;
    MPI_Status status;

    MPI_Comm_size(comm, &np);
    MPI_Comm_rank(comm, &myrank);

    buff = (double *)malloc(n*sizeof(double));

    nlocal = n/np;

    MPI_Allgather(b, nlocal, MPI_DOUBLE, buff, nlocal, MPI_DOUBLE, comm);

    for(int i = 0; i < nlocal; i++){
        x[i] = 0.0;
        for(int j = 0; j < n; j++){
            x[i] += a[i*n+j]*buff[j];
        }
    }
    free(buff);
}

int main(int argc, char *argv[]){
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int n = 10000;
    double *A = NULL;
    double *b = NULL; 
    double *x = NULL; 

    int nlocal = n / size;

    A = (double *)malloc(nlocal * n * sizeof(double)); 
    b = (double *)malloc(nlocal * sizeof(double));
    x = (double *)malloc(nlocal * sizeof(double));

    for(int i = 0; i < nlocal; i++){
        b[i] = 1.0; 
        for(int j = 0; j < n; j++){
            A[i*n + j] = rank*nlocal + i + j + 1; 
        }
    }
    MPI_Barrier(MPI_COMM_WORLD);
    double start = MPI_Wtime();

    MatrixVector(n, A, b, x, MPI_COMM_WORLD);

    MPI_Barrier(MPI_COMM_WORLD);
    double end = MPI_Wtime();

    if(rank == 0){
        printf("Execution time: %f\n", end - start);
    }

    free(A);
    free(b);
    free(x);

    MPI_Finalize();
    return 0;
}