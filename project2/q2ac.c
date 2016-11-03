#include <stdio.h>
#include <stdint.h>

#define MSG_BITLEN 45   // 45 bits in the message
#define MSG_SYMLEN 9    // 9 symbols in the message
#define SYM_BITLEN 5    // 5 bits per symbol

#define GETBIT(x, n) ((x&(1<<n))>>n)

uint8_t stob(uint8_t s)
{
    if (s >= 'A' && s <= 'Z')   // letter
        return s - 'A';
    else                        // number
        return s - '0' + 26;
}

uint8_t btos(uint8_t b)
{
    if (b < 26)                 // letter
        return b + 'A';
    else                        // number
        return b + '0' - 26; 
}

const char bit_rep[16][5] = {
    "0000", "0001", "0010", "0011",
    "0100", "0101", "0110", "0111",
    "1000", "1001", "1010", "1011",
    "1100", "1101", "1110", "1111"
};

int main(void)
{
    /* 1. Use the known plaintext to find the initial LFSR state. */

    uint8_t *ct_s_hdr = "J5A";
    uint8_t *pt_s_hdr = "WPI";
    uint8_t k_b_hdr[3];

    for (int i = 0; i < 3; i++) {
        k_b_hdr[i] = stob(pt_s_hdr[i]) ^ stob(ct_s_hdr[i]);
    }

    uint8_t init_state = (k_b_hdr[0] << 1) + GETBIT(k_b_hdr[1], 4); // 111111
 
    /* 2. Find the LFSR coefficients. */
   
    // q2b.jl gives the LFSR coefficients: 110000

    /* 3. Generate the LFSR sequence to find the plaintext. */

    uint8_t bit;
    uint8_t state = init_state;
    uint8_t seq[MSG_BITLEN] = {1, 1, 1, 1, 1, 1};
    uint8_t seq_i = 6;

    do { 
        //printf("%s%s\n", bit_rep[(state & 0xf0) >> 4], bit_rep[(state & 0x0f)]);
        bit = ((state >> 0) ^ (state >> 1)) & 1;
        state = (state >> 1) | (bit << 5);
        seq[seq_i++] = bit;
    } while (seq_i < MSG_BITLEN);

    printf("The truncated LFSR cycle:\n");
    for (int i = 0; i < MSG_BITLEN; i++) {
        printf("%d", seq[i]);
    }
    printf("\n");
        
    uint8_t *ct_s = "J5A0EDJ2B";
    uint8_t ct_b[MSG_BITLEN];
    uint8_t bits; 
    printf("The ciphertext as bits:\n");
    for (int i = 0; i < MSG_SYMLEN; i++) {
        bits = stob(ct_s[i]);
        for (int j = 0; j < SYM_BITLEN; j++) {
            ct_b[i*SYM_BITLEN+j] = GETBIT(bits, SYM_BITLEN-j-1);
        }
    }
    for (int i = 0; i < MSG_BITLEN; i++) {
        printf("%d", ct_b[i]);
    }
    printf("\n");

    uint8_t pt_b[MSG_BITLEN];
    for (int i = 0; i < MSG_BITLEN; i++) {
        pt_b[i] = ct_b[i] ^ seq[i];
    }
    printf("The plaintext as bits:\n");
    for (int i = 0; i < MSG_BITLEN; i++) {
        printf("%d", pt_b[i]);
    }
    printf("\n");

    uint8_t pt_s[MSG_SYMLEN];
    printf("The plaintext as symbols:\n");
    for (int i = 0; i < MSG_BITLEN; i++) {
        bits = 0;
        for (int j = 0; j < SYM_BITLEN; j++) {
            bits += pt_b[i*SYM_BITLEN+j] << (SYM_BITLEN-j-1);
        }
        pt_s[i] = btos(bits);
    }
    for (int i = 0; i < MSG_SYMLEN; i++) {
        printf("%c", pt_s[i]);
    }
    printf("\n");

    return 0;
}
