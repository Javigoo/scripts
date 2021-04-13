#include <stdio.h>

#define MAXLINE 1000
#define BLANKSTAB 4


/* Replace tabs in the input with the proper number of blanks to space to the next tab stop */

int main() {
    int c, i, j;
    char line[MAXLINE];

    for (i = 0; (c = getchar()) != '\n'; ++i)    // Leer hasta salto de linea
    {
        if(c == '\t')
        {
            for (i = i; i < BLANKSTAB; ++i)
            {
               line[i] = ' ';
            }
            
            printf("Tab\n");
        }
        else
        {
            line[i] = c;
        }
    }

    for (i = 0; line[i] != '\0' ; ++i)
    {
        putchar(line[i]);
    }
    
}