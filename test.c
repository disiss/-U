#include <stdio.h>
#include <string.h>

int main()
{
	char str[] = "8159100415448631839278649139990730313314399816976859169811137221733780630925521022916235244154220727102011140978562245795632398890623960718493683829047109658275276048372081506381349734904091586132426756394636231787342510222917584152170656204268219610816425911506454286168908232497399522293";
	int init_size = strlen(str);
	char delim[] = "0";

	char *ptr = strtok(str, delim);

	while (ptr != NULL)
	{
		printf("%s, ", ptr);
		ptr = strtok(NULL, delim);
	}

	return 0;
}