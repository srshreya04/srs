#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Quick sort
void quickSortAsc(int arr[], int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(&arr[i], &arr[j]);
            }
        }
        swap(&arr[i + 1], &arr[high]);
        int pi = i + 1;

        quickSortAsc(arr, low, pi - 1);
        quickSortAsc(arr, pi + 1, high);
    }
}

void quickSortDesc(int arr[], int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] > pivot) {
                i++;
                swap(&arr[i], &arr[j]);
            }
        }
        swap(&arr[i + 1], &arr[high]);
        int pi = i + 1;

        quickSortDesc(arr, low, pi - 1);
        quickSortDesc(arr, pi + 1, high);
    }
}

int main() {
    int n, threads;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter number of threads: ");
    scanf("%d", &threads);

    int A[n], B[n];

    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        A[i] = rand() % 100;
        B[i] = rand() % 100;
    }

    quickSortAsc(A, 0, n - 1);
    quickSortDesc(B, 0, n - 1);

    long min_dot = 0;
    long min_dot_reduction = 0;
    omp_set_num_threads(threads);

    #pragma omp parallel for
    for (int i = 0; i < n; i++) {
        min_dot += (long)A[i] * B[i]; 
    }

    #pragma omp parallel for reduction(+:min_dot_reduction)
    for (int i = 0; i < n; i++) {
        min_dot_reduction += (long)A[i] * B[i];
    }

    printf("\nResult without reduction (may be WRONG): %ld\n", min_dot);
    printf("Result with reduction: %ld\n", min_dot_reduction);

    return 0;
}
