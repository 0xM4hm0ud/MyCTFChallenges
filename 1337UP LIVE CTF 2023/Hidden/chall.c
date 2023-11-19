// gcc -fstack-protector-explicit -w chall.c -o chall
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void _(){
    FILE *fptr;
    char ch;
    
    fptr = fopen("flag.txt","r");
    if (fptr == NULL) 
    {
        perror("flag.txt not found! If this happened on the server, contact the author please!");
        exit(1);
    }
    do 
    {
        ch = fgetc(fptr);
        putchar(ch);

    } while(ch != EOF);
    fclose(fptr);
    return;
}

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}

int input(void){
    char buffer[50] = {0};
	printf("Tell me something:\n");
    read(0, buffer, 0x50);   
    printf("I remember what you said: ");
    puts(buffer);
	return 0;
}

__attribute__((stack_protect))
int main(void){
    init();
	printf("Can you find the hidden truth?\n");
	printf("Lets see!\n");
    input();
	return 0;
}
