#include <stdio.h>
#include <stdlib.h>

#define LBIT  0b00100000
#define MBITS 0b00011110
#define RBIT  0b00000001

#define OUTER2(x) ((x & LBIT) >> 4 + (x & RBIT))
#define INNER4(x) ((x & MBITS) >> 1)

static const char S2[4][16] =
{
    {15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10},
    { 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5},
    { 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15},
    {13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9}
};

char out_S2(char x)
{
    return S2[OUTER2(x)][INNER4(x)];
}

int main(void)
{
    printf("problem 3a, verify DES S_2\n");
    
    printf("x\tout_S2(x)\n");
    printf("%d\t%d\n",  4, out_S2( 4));
    printf("%d\t%d\n",  8, out_S2( 8));
    printf("%d\t%d\n", 24, out_S2(24));
    printf("%d\t%d\n", 56, out_S2(56));
 
    printf("problem 3b, compute SAC\n");

    int i, j, k, sum, SAC_coef[6][4] = {0};

    /* fill SAC_coef */
    for (i = 0; i < 64; i++) {
        for (j = 0; j < 6; j++) {
            sum = out_S2(i) ^ out_S2(i ^ (1 << j));
            for (k = 0; k < 4; k++)
                SAC_coef[j][k] += (sum >> k) & 1;
        }
    }

    /* print SAC_coef */
    printf("i\tSAC_coef:\n");
    for (i = 0; i < 6; i++) {
        printf("%d\t", i);
        for (j = 0; j < 4; j++) {
            printf("%d\t", SAC_coef[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
