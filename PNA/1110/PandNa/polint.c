#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#define NRANSI
#include "nrutil.h"

void polint(float xa[], float ya[], int n, float x, float *y, float *dy)
{
	int i,m,ns=1;
	float den,dif,dift,ho,hp,w;
	float *c,*d;
	float yy, ddyy;

	printf("n=%d\n", n);
	printf("xa[1]=%f\n", xa[1]);
	printf("ya[1]=%f\n", ya[1]);

	dif=fabs(x-xa[1]);
	c=vector(1,n);
	d=vector(1,n);
	for (i=1;i<=n;i++) {
		if ( (dift=fabs(x-xa[i])) < dif) {
			ns=i;
			dif=dift;
		}
		c[i]=ya[i];
		d[i]=ya[i];
	}

	printf("c[1]=%f\n", c[1]);
	printf("d[1]=%f\n", d[1]);
	printf("c[5]=%f\n", c[5]);
	printf("d[5]=%f\n", d[5]);

	yy=ya[ns];
	*y=ya[ns--];

	printf("ns=%d\n", ns);
	printf("y=%f\n", *y);

	for (m=1;m<n;m++) {
		for (i=1;i<=n-m;i++) {
			ho=xa[i]-x;
			hp=xa[i+m]-x;
			w=c[i+1]-d[i];
			if ( (den=ho-hp) == 0.0) nrerror("Error in routine polint");
			printf("den=%f\n", den);
			den=w/den;
			d[i]=hp*den;
			c[i]=ho*den;
			printf("c[%d]=%f\n", i,c[i]);
			printf("d[%d]=%f\n", i,d[i]);
		}
		printf("2ns=%d\n", ns*2);
		printf("n-m=%d\n", n-m);
		printf("dy=%f\n", (2*ns < (n-m) ? c[ns+1] : d[ns]));
//		ddyy=(2*ns < (n-m) ? c[ns+1] : d[ns--]);
//		printf("dy=%f\n", ddyy);
//		yy += ddyy;
//		printf("y=%f\n", *y);
		*y += (*dy=(2*ns < (n-m) ? c[ns+1] : d[ns--]));
	}
	free_vector(d,1,n);
	free_vector(c,1,n);
/*
	*y = yy;
	*dy = ddyy;
*/
}
#undef NRANSI
/* (C) Copr. 1986-92 Numerical Recipes Software 1+5-5i. */
