openmp
gcc -fopenmp filename.c -o fn
./fn

mpi
mpicc filename.c -o fn
mpirun -np 10 ./fn

cuda
!nvcc gpu_properties.cu -o gpu_properties
!./gpu_properties
