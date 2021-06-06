#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {
	char c[200];
	char *t;
	FILE* fp = fopen("file.txt", "r");
	while (1) {
		t = fgets(c, 200, fp);
		if (t == NULL) break;
		printf("%s ", c);

	}
}