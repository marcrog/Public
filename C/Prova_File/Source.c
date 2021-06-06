#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

int main() {
	int c = 0;
	int s = 0;
	FILE* fp = fopen("ollare.txt", "r+");
	if (fp == NULL) printf("Errore");
	else s = fscanf(fp, "%d ", &c);
	printf("%d", c);
}