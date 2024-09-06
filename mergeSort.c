//Author:Vaibhav Singh(21BCS128)
#include <stdio.h>

void merge(int a[], int l, int mid, int h)
{
    int i = l, j = mid + 1, k = l;
    int b[100];

    while (i <= mid && j <= h)
    {
        if (a[i] < a[j])
        {
            b[k++] = a[i++];
        }
        else
        {
            b[k++] = a[j++];
        }
    }
    for (; i <= mid; i++)
    {
        b[k++] = a[i];
    }
    for (; j <= h; j++)
    {
        b[k++] = a[j];
    }

    for (int t = l; t <= h; t++)
    {
        a[t] = b[t];
    }
}

void mergesort(int a[], int l, int h)
{
    int mid;
    if (l < h)
    {
        mid = (l + h) / 2;
        mergesort(a, l, mid);
        mergesort(a, mid + 1, h);
        merge(a, l, mid, h);
    }
}

int main()
{
    int a[] = {11, 13, 7, 12, 16, 9, 24, 5, 10, 3}, i;
    /*printf("unsorted array:");
    for (i = 0; i < 10; i++)
    {
        printf("%d,", a[i]);
    }
    printf("\n");*/

    mergesort(a, 0, 9);

    printf("sorted array:");
    for (i = 0; i < 10; i++)
    {
        printf("%d,", a[i]);
    }
    return 0;
}
