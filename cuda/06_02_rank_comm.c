#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    int rank, size, group_size;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    MPI_Group world_group;
    MPI_Comm_group(MPI_COMM_WORLD, &world_group);
    MPI_Group_size(world_group, &group_size);

    int ranks[group_size];
    for (int i = 0; i < group_size; i++) {
        ranks[i] = i;
    }

    if (rank == 0) {
        printf("MPI_COMM_WORLD group has %d processes: ", group_size);
        for (int i = 0; i < group_size; i++) {
            printf("%d ", ranks[i]);
        }
        printf("\n");
    }

    printf("Hello from process %d out of %d\n", rank, size);

    MPI_Group_free(&world_group);
    MPI_Finalize();
    return 0;
}
