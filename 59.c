#include <stdlib.h>
#include <stdio.h>
#include <strings.h>

float alphaPercent(char *input) {
    int x, a;
    int alphaCounter = 0;
    int totalCounter = 0;
    float percent;
    for(x = 0; *(input+x) != '\0'; x++) {
        a = *(input+x);
        if((a >= 97 && a <= 122) || (a >= 65 && a <= 90)) 
            alphaCounter++;
        if(a != 32)
            totalCounter++;
    }
    return(((float)alphaCounter / (float)totalCounter) * 100);
}

int length(FILE *fp) {
    int len;
    int topPos = ftell(fp);
    fseek(fp, 0, SEEK_END);
    len = ftell(fp);
    fseek(fp, topPos, SEEK_SET);
    return(len); 
}

int decryptfile(char *key) {
    FILE *fp = fopen("cipher.txt", "r");
    if(fp == NULL) { 
        puts("input file failure");
        exit(EXIT_FAILURE);
    }
    char *tokens;
    char *comma = ",";
    int counter = 0;
    int len = length(fp);
    char line[len];
    int curValue, keyValue;
    char newstring[len];
    int index = 0;

    bzero(newstring, len);
    while((fgets(line, sizeof(line), fp)) != NULL) {
        tokens = strtok(line, comma);
        while(tokens && strncmp(tokens, "\n", 2)) {
            keyValue = key[counter];
            curValue = atoi(tokens);
            newstring[index] = (curValue ^ keyValue);
            index++;
            if(counter == strlen(key) - 1)
                counter = 0;
            else 
                counter++;
            tokens = strtok(NULL, comma);
        }
    }
    fclose(fp);
    if(alphaPercent(newstring) > 90) {
        printf("%s\n", newstring);
        printf("KEY: %s\n", key);
        return(1);
    }
    return(0);
}

int main(int argc, char *argv[]) {
    int a, b, c;
    char key[4];

    for(a = 97; a <= 122; a++) {
        for(b = 97; b <= 122; b++) {
            for(c = 97; c <= 122; c++) {
                key[0] = a;
                key[1] = b;
                key[2] = c;
                key[3] = '\0';
                if(decryptfile(key))
                   return(0); 
            }
        }
    }
    puts("didn't find a key");
    return(0);
}
