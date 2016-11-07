#include <stdio.h>
#include <stdint.h>

#define MSG_BITLEN 45   // 45 bits in the message
#define MSG_SYMLEN 9    // 9 symbols in the message
#define SYM_BITLEN 5    // 5 bits per symbol

#define LFSR_DEGREE 6
#define LFSR_INIT 0x3f

const uint8_t bit_rev[32] = {
    0x00, 0x10, 0x08, 0x18, 0x04, 0x14, 0x0c, 0x1c,
    0x02, 0x12, 0x0a, 0x1a, 0x06, 0x16, 0x0e, 0x1e,
    0x01, 0x11, 0x09, 0x19, 0x05, 0x15, 0x0d, 0x1d,
    0x03, 0x13, 0x0b, 0x1b, 0x07, 0x17, 0x0f, 0x1f
};

uint8_t stob(char s)
{
    return (s >= 'A') ? s - 65: s - 22;
}

char btos(uint8_t b)
{
    return (b < 26) ? b + 65: b + 22;
}

int main(void)
{
    /* Generate a sufficiently-long LFSR sequence */
    uint64_t lfsr = LFSR_INIT; // sequence
    uint64_t bit;
    uint8_t state = LFSR_INIT;
    int offset = LFSR_DEGREE;
    do { 
        bit = (state ^ (state >> 1)) & 1; // coefs: {1, 1, 0, 0, 0, 0}
        state = (state >> 1) | (bit << (LFSR_DEGREE-1));
        lfsr += (bit << offset++);
    } while (offset < MSG_BITLEN);

    /* Convert the ciphertext into plaintext */
    char ct_s[MSG_SYMLEN] = "J5A0EDJ2B";
    char pt_s[MSG_SYMLEN];
    uint64_t ct_b = 0;
    uint64_t pt_b;
    for (int i=0; i<MSG_SYMLEN; i++) {
        ct_b += (uint64_t) bit_rev[stob(ct_s[i])] << i*SYM_BITLEN;
        pt_b = ct_b ^ lfsr; // sub-optimal :(
        pt_s[i] = btos(bit_rev[pt_b >> (i*SYM_BITLEN) & 0x1f]);
        printf("%c", pt_s[i]);
    }
    puts("");
    
    return 0;
}
