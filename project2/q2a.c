#include <stdio.h>

#define GETBIT(x, n) ((x&(1<<n))>>n)

int sym2vec(char s)
{
    if (s >= 'A' && s <= 'Z') // letter
        return s - 'A';
    else // number
        return s - '0' + 26;
}

int main(void)
{
    char *ct_hdr = "J5A", *pt_hdr = "WPI", k_hdr[3];
    
    for (int i = 0; i < 3; i++)
        k_hdr[i] = sym2vec(pt_hdr[i]) ^ sym2vec(ct_hdr[i]);

    char init_vec = (k_hdr[0] << 1) + GETBIT(k_hdr[1], 4); // first 6 bits
    printf("question 2a\n");
    printf("initialization vector = %d\n", init_vec);
    
    return 0;
}
