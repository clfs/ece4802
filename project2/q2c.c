#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

#define MSG_BITLEN 45   // 45 bits in the message
#define MSG_SYMLEN 9    // 9 symbols in the message
#define SYM_BITLEN 5    // 5 bits per symbol

#define GETBIT(x, n) ((x&(1<<n))>>n)

const uint8_t bit_rev[32] = {
    0x00, 0x10, 0x08, 0x18, 0x04, 0x14, 0x0c, 0x1c,
    0x02, 0x12, 0x0a, 0x1a, 0x06, 0x16, 0x0e, 0x1e,
    0x01, 0x11, 0x09, 0x19, 0x05, 0x15, 0x0d, 0x1d,
    0x03, 0x13, 0x0b, 0x1b, 0x07, 0x17, 0x0f, 0x1f
};

void printBits(size_t const size, void const * const ptr)
{
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    for (i=size-1;i>=0;i--)
    {
        for (j=7;j>=0;j--)
        {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
    }
    puts("");
}

uint8_t stob(char s)
{
    if (s >= 'A' && s <= 'Z')   // letter
        return s - 'A';
    else                        // number
        return s - '0' + 26;
}

char btos(uint8_t b)
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
    /* problem parameters */

    uint8_t lfsr_init = 0b111111;
    uint8_t lfsr_coefs = 0b000011;   
    char *ct_symbols = "J5A0EDJ2B";

    /* generate a sufficiently-long LFSR sequence */

    uint64_t bit;
    uint8_t state = lfsr_init;
    uint8_t seq[MSG_BITLEN] = {1, 1, 1, 1, 1, 1};
    uint8_t seq_i = 6;
    uint64_t testing = 0b111111;

    do { 
        printf("At start of state %d:\n", seq_i);
        printf("state\t%s%s\n", bit_rep[(state & 0xf0) >> 4], bit_rep[(state & 0x0f)]);
        printf("bit\t%" PRIu64 "\n", bit);
        printf("seq[]\t");
        for (int i = 0; i < MSG_BITLEN; i++) {
            printf("%d", seq[i]);
        }
        printf("\n");
        printf("testing\t");
        printBits(sizeof(testing), &testing);
        //printf("testing\t%" PRIx64 "\n", testing);
        
        bit = ((state >> 0) ^ (state >> 1)) & 1;
        state = (state >> 1) | (bit << 5);
        testing += (bit << seq_i);
        seq[seq_i++] = bit;
    } while (seq_i < MSG_BITLEN);

    printf("The truncated LFSR cycle:\n");
    for (int i = 0; i < MSG_BITLEN; i++) {
        printf("%d", seq[i]);
    }
    printf("\n");
    printf("testing\n%" PRIu64 "\n", testing);
    
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
    
    uint64_t ct_bits = 0;
    uint8_t symbol_as_bits;
    printf("The ciphertext as bits, attempt 2:\n");
    for (int i = 0; i < MSG_SYMLEN; i++) {
        printf("at start of i=%d\n", i);
        printBits(sizeof(ct_bits), &ct_bits);
        printf("char\t%d\n", ct_symbols[i]);
        printf("stob\t%d\n", stob(ct_symbols[i]));
        printf("stobr\t%d\n", bit_rev[stob(ct_symbols[i])]);
        ct_bits += ((uint64_t) bit_rev[stob(ct_symbols[i])]) << i*SYM_BITLEN;
    }
    printf("ct_bits\t%" PRIu64 "\n", ct_bits);

    
    uint8_t pt_b[MSG_BITLEN];
    for (int i = 0; i < MSG_BITLEN; i++) {
        pt_b[i] = ct_b[i] ^ seq[i];
    }
    printf("The plaintext as bits:\n");
    for (int i = 0; i < MSG_BITLEN; i++) {
        printf("%d", pt_b[i]);
    }
    printf("\n");
    

    uint64_t pt_bits = ct_bits ^ testing;
    printf("plaintext as bits, test\n");
    printBits(sizeof(uint64_t), &pt_bits);
    
    char pt_symbols[MSG_SYMLEN];
    printf("plaintext as symbols, test\n");
    for (int i = 0; i < MSG_SYMLEN; i++) {
        pt_symbols[i] = btos(bit_rev[((pt_bits >> (i*SYM_BITLEN))) & 0x1f]);
        printf("%c", pt_symbols[i]);
    }
/*
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
    */    
return 0;
}
