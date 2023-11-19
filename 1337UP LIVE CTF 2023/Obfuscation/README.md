# Obfuscation

|||
|-|-|
|  **CTF**  |  [1337UP LIVE CTF 2023](https://ctf.intigriti.io/) [(CTFtime)](https://ctftime.org/event/2134)  |
|  **Author** |  0xM4hm0ud |
|  **Category** |  Reversing |
|  **Solves** |  211  |
|  **Difficulty** |  Easy |
| **Files** |  [obfuscation.zip](<obfuscation.zip>)  |

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/58c3ca73-5f90-4573-840f-330f1de27fc5)

# Solution

We get 2 files after unzipping the zip. One is an output file with some weird string the other file is an obfuscated c program:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
int o_a8d9bf17d390687c168fe26f2c3a58b1[]={42, 77, 3, 8, 69, 86, 60, 99, 50, 76, 15, 14, 41, 87, 45, 61, 16, 50, 20, 5, 13, 33, 62, 70, 70, 77, 28, 85, 82, 26, 28, 32, 56, 22, 21, 48, 38, 42, 98, 20, 44, 66, 21, 55, 98, 17, 20, 93, 99, 54, 21, 43, 80, 99, 64, 98, 55, 3, 95, 16, 56, 62, 42, 83, 72, 23, 71, 61, 90, 14, 33, 45, 84, 25, 24, 96, 74, 2, 1, 92, 25, 33, 36, 6, 26, 14, 37, 33, 100, 3, 30, 1, 31, 31, 86, 92, 61, 86, 81, 38};void o_e5c0d3fd217ec5a6cd022874d7ffe0b9(char* o_0d88b09f1a0045467fd9afc4aa07208c,int o_8ce986b6b3a519615b6244d7fb2b62f8){assert(o_8ce986b6b3a519615b6244d7fb2b62f8 == 24);for (int o_b7290d834b61bc1707c4a86bad6bd5be=(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);(o_b7290d834b61bc1707c4a86bad6bd5be < o_8ce986b6b3a519615b6244d7fb2b62f8) & !!(o_b7290d834b61bc1707c4a86bad6bd5be < o_8ce986b6b3a519615b6244d7fb2b62f8);++o_b7290d834b61bc1707c4a86bad6bd5be){o_0d88b09f1a0045467fd9afc4aa07208c[o_b7290d834b61bc1707c4a86bad6bd5be] ^= o_a8d9bf17d390687c168fe26f2c3a58b1[o_b7290d834b61bc1707c4a86bad6bd5be % sizeof((o_a8d9bf17d390687c168fe26f2c3a58b1))] ^ (0x000000000000266E + 0x0000000000001537 + 0x0000000000001B37 - 0x00000000000043A5);};};int o_0b97aabd0b9aa9e13aa47794b5f2236f(FILE* o_eb476a115ee8ac0bf24504a3d4580a7d){if ((fseek(o_eb476a115ee8ac0bf24504a3d4580a7d,(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00),(0x0000000000000004 + 0x0000000000000202 + 0x0000000000000802 - 0x0000000000000A06)) < (0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00)) & !!(fseek(o_eb476a115ee8ac0bf24504a3d4580a7d,(0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00),(0x0000000000000004 + 0x0000000000000202 + 0x0000000000000802 - 0x0000000000000A06)) < (0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00))){fclose(o_eb476a115ee8ac0bf24504a3d4580a7d);return -(0x0000000000000002 + 0x0000000000000201 + 0x0000000000000801 - 0x0000000000000A03);};int o_6a9bff7d60c7b6a5994fcfc414626a59=ftell(o_eb476a115ee8ac0bf24504a3d4580a7d);rewind(o_eb476a115ee8ac0bf24504a3d4580a7d);return o_6a9bff7d60c7b6a5994fcfc414626a59;};int main(int o_f7555198c17cb3ded31a7035484d2431,const char * o_5e042cacd1c140691195c705f92970b7[]){char* o_3477329883c7cec16c17f91f8ad672df;char* o_dff85fa18ec0427292f5c00c89a0a9b4=NULL;FILE* o_fba04eb96883892ddecbb0f397b51bd7;if ((o_f7555198c17cb3ded31a7035484d2431 ^ 0x0000000000000002)){printf("\x4E""o\164 \x65""n\157u\x67""h\040a\x72""g\165m\x65""n\164s\x20""p\162o\x76""i\144e\x64""!");exit(-(0x0000000000000002 + 0x0000000000000201 + 0x0000000000000801 - 0x0000000000000A03));};o_fba04eb96883892ddecbb0f397b51bd7 = fopen(o_5e042cacd1c140691195c705f92970b7[(0x0000000000000002 + 0x0000000000000201 + 0x0000000000000801 - 0x0000000000000A03)],"\x72""");if (o_fba04eb96883892ddecbb0f397b51bd7 == NULL){perror("\x45""r\162o\x72"" \157p\x65""n\151n\x67"" \146i\x6C""e");return -(0x0000000000000002 + 0x0000000000000201 + 0x0000000000000801 - 0x0000000000000A03);};int o_102862e33b75e75f672f441cfa6f7640=o_0b97aabd0b9aa9e13aa47794b5f2236f(o_fba04eb96883892ddecbb0f397b51bd7);o_dff85fa18ec0427292f5c00c89a0a9b4 = (char* )malloc(o_102862e33b75e75f672f441cfa6f7640 + (0x0000000000000002 + 0x0000000000000201 + 0x0000000000000801 - 0x0000000000000A03));if (o_dff85fa18ec0427292f5c00c89a0a9b4 == NULL){perror("\x4D""e\155o\x72""y\040a\x6C""l\157c\x61""t\151o\x6E"" \145r\x72""o\162");fclose(o_fba04eb96883892ddecbb0f397b51bd7);return -(0x0000000000000002 + 0x0000000000000201 + 0x0000000000000801 - 0x0000000000000A03);};fgets(o_dff85fa18ec0427292f5c00c89a0a9b4,o_102862e33b75e75f672f441cfa6f7640,o_fba04eb96883892ddecbb0f397b51bd7);fclose(o_fba04eb96883892ddecbb0f397b51bd7);o_e5c0d3fd217ec5a6cd022874d7ffe0b9(o_dff85fa18ec0427292f5c00c89a0a9b4,o_102862e33b75e75f672f441cfa6f7640);o_fba04eb96883892ddecbb0f397b51bd7 = fopen("\x6F""u\164p\x75""t","\x77""b");if (o_fba04eb96883892ddecbb0f397b51bd7 == NULL){perror("\x45""r\162o\x72"" \157p\x65""n\151n\x67"" \146i\x6C""e");return -(0x0000000000000002 + 0x0000000000000201 + 0x0000000000000801 - 0x0000000000000A03);};fwrite(o_dff85fa18ec0427292f5c00c89a0a9b4,o_102862e33b75e75f672f441cfa6f7640,sizeof(char),o_fba04eb96883892ddecbb0f397b51bd7);fclose(o_fba04eb96883892ddecbb0f397b51bd7);free(o_dff85fa18ec0427292f5c00c89a0a9b4);return (0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);};
```

We can ask ChatGPT to clean the code. The output is:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int key[] = {42, 77, 3, 8, 69, 86, 60, 99, 50, 76, 15, 14, 41, 87, 45, 61, 16, 50, 20, 5, 13, 33, 62, 70, 70, 77, 28, 85, 82, 26, 28, 32, 56, 22, 21, 48, 38, 42, 98, 20, 44, 66, 21, 55, 98, 17, 20, 93, 99, 54, 21, 43, 80, 99, 64, 98, 55, 3, 95, 16, 56, 62, 42, 83, 72, 23, 71, 61, 90, 14, 33, 45, 84, 25, 24, 96, 74, 2, 1, 92, 25, 33, 36, 6, 26, 14, 37, 33, 100, 3, 30, 1, 31, 31, 86, 92, 61, 86, 81, 38};

void decrypt(char *data, int length) {
    assert(length == 24);
    for (int i = 0; i < length; ++i) {
        data[i] ^= key[i % sizeof(key)] ^ 0x7C35;
    }
}

int getFileSize(FILE *file) {
    if (fseek(file, 0x200 + 0x800 - 0xA00, SEEK_SET) < 0) {
        fclose(file);
        return -2;
    }
    int size = ftell(file);
    rewind(file);
    return size;
}

int main(int argc, const char *argv[]) {
    if (argc != 2) {
        printf("Not enough arguments provided!\n");
        return -2;
    }

    FILE *inputFile = fopen(argv[1], "r");
    if (inputFile == NULL) {
        perror("Error opening file");
        return -2;
    }

    int fileSize = getFileSize(inputFile);
    if (fileSize < 0) {
        return fileSize;
    }

    char *data = (char *)malloc(fileSize + 2);
    if (data == NULL) {
        perror("Memory allocation error");
        fclose(inputFile);
        return -2;
    }

    fgets(data, fileSize, inputFile);
    fclose(inputFile);

    decrypt(data, fileSize);

    FILE *outputFile = fopen("output", "wb");
    if (outputFile == NULL) {
        perror("Error opening file");
        free(data);
        return -2;
    }

    fwrite(data, fileSize, sizeof(char), outputFile);
    fclose(outputFile);

    free(data);
    return 0;
}
```

We can see it does a simple xor with the input we give. We can do the reverse to get the flag:

```c
#include <stdio.h>
#include <stdlib.h>

int arr[] = {42, 77, 3, 8, 69, 86, 60, 99, 50, 76, 15, 14, 41, 87, 45, 61, 16, 50, 20, 5, 13, 33, 62, 70, 70, 77, 28, 85, 82, 26, 28, 32, 56, 22, 21, 48, 38, 42, 98, 20, 44, 66, 21, 55, 98, 17, 20, 93, 99, 54, 21, 43, 80, 99, 64, 98, 55, 3, 95, 16, 56, 62, 42, 83, 72, 23, 71, 61, 90, 14, 33, 45, 84, 25, 24, 96, 74, 2, 1, 92, 25, 33, 36, 6, 26, 14, 37, 33, 100, 3, 30, 1, 31, 31, 86, 92, 61, 86, 81, 38};

void deobfuscate(char *enc) {
    for (int i = 0; i < 24; ++i) {
        enc[i] ^= 0x1337 ^ arr[i % sizeof(arr)];
    }
}

int main(void)
{
	FILE *fp;
	char *enc = NULL;

	fp = fopen("output", "rb");
    if (fp == NULL) {
        perror("Error opening file");
        return -1;
    }

    enc = (char *)malloc(24);
    if (enc == NULL) {
        perror("Memory allocation error");
        fclose(fp);
        return -1;
    }

    fgets(enc, 24, fp);
    fclose(fp);

    deobfuscate(enc);
    printf("%s\n", enc);
    free(enc);
    return 0;
}
```

After compiling and running we get:

![image](https://github.com/0xM4hm0ud/MyCTFChallenges/assets/80924519/65f99475-c94f-4447-a08f-f80c0c9d1821)
