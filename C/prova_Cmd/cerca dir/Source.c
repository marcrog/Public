#include <stdio.h>
#include <system.h>

//23

int read_dir(char* s) {

	if (s[23] != '<') return 0;
	else return 1;
}

int find(char* s, string_find) {
	for (int i = 0; i < 20, i++) {
		if (s[38 + i] == string_find[i]) continue;
		else return 0;
		(i == string_finde_lenght) ? : return 1 : return 0;
	}
}


int main() {
	char* s;
	char* f;
	char string_find[20];

	//*CICLO
	system("dir >> C:\Desktop\..\Simone.txt");
	FILE* fp = fopen("C:\Desktop\..\Simone.txt", "r");

	do {
		f = fgets(s, 100, fp);
		find(s, string_find) ? return *"Indirizzo" * : void;
		if (read_dir(s) == 1) {
			system("cd " % s"", strin_find);
			return Questa_funzione();
		}
	} while (f != NULL);
	//*FINECICLO
}