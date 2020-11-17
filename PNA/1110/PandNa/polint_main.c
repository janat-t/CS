/* Driver for routine for polint.c  */
/* Program polint_main.c           */ 
#include <stdio.h>
#include <stdlib.h>
#include "nr.h"
#include "nrutil.h" /* Utilities program, listed in Appendix B of NRC book */ 
                    /* NRC stands for Numerical Recipes in C */ 
 
#define NDATA  5
#define NDATA1 NDATA+1
 
int main(void)
{
	int n = NDATA;
	float xa[NDATA1]={0.0, -1.0, -0.5, 0.0, 0.5, 1.0};
	float ya[NDATA1]={0.0,  0.0, -1.0, 0.0, 1.0, 0.0};
	float x1, x2;
	float y1, y2, dy1, dy2;
//        FILE *fp;
/*
* set x
*/ 
	printf("set x \n");
	x1= -2.0; x2= 2.0;
                /* Call polint */
	printf("x1=%f\n", x1);
	printf("x2=%f\n", x2);
/*--------------------------------------------------------------------- */  
	polint(xa, ya, n, x1, &y1, &dy1); 
	polint(xa, ya, n, x2, &y2, &dy2); 
/*--------------------------------------------------------------------- */ 
	printf("f(%f)= %f\n", x1, y1);
	printf("f(%f)= %f\n", x2, y2);
//        fclose(fp);
        return 0;
}
