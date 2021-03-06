#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define ANS 44.723546267557865628157665111058656260226024578742563958198931614

double dabs(double x){
    return x>0? x : -x;
}

double func(double x){
    return pow(2,x);
}

double trapzd(double (*func)(double), double a, double b, int n){
    double x = a;
    double dx = (b-a)/n;
    double ans = 0.0;
    int i;
    for(i=0; i<n; ++i){
        ans += (func(x)+func(x+dx))*0.5*dx;
        x+=dx;
    }
    return ans;
}

double montecarlo(double (*func)(double), double a, double b, int n){
    srand(time(NULL));
    double ans = 0.0;
    double r;
    int i;
    for(i=0; i<n; ++i){
        r = (double)(rand())/RAND_MAX;
        r *= b-a;
        r += a;
        ans += func(r)*(b-a)/n;
    }
    return ans;
}

int main(){
    double a = 0.0;
    double b = 5.0;
    double s10, s100, s1000, s1000000;
    /* FILE *fp; */

    printf("The accurate answer is pi/4 which is %lf\n", ANS);

/* ------------- Trapezoidal ------------- */
    s10 = trapzd(func, a, b, 10);
    s100 = trapzd(func, a, b, 100);
    s1000 = trapzd(func, a, b, 1000);
    s1000000 = trapzd(func, a, b, 1000000);
/* --------------------------------------- */
    printf("\nIntegrate using Trapezoidal Rule\n");
    printf("integral using n=10 f=%lf\n", s10);
    printf("integral using n=100 f=%lf\n", s100);
    printf("integral using n=1000 f=%lf\n", s1000);
    printf("integral using n=1000000 f=%lf\n", s1000000);
    printf("accuracy of n=1000000 is %lf%%\n", 100.0 - dabs(ANS - s1000000)/ANS);
/* --------------------------------------- */


/* ------------- Monte Carlo ------------- */
    s10 = montecarlo(func, a, b, 10);
    s100 = montecarlo(func, a, b, 100);
    s1000 = montecarlo(func, a, b, 1000);
    s1000000 = montecarlo(func, a, b, 1000000);
/* --------------------------------------- */
    printf("\nIntegrate using Monte Carlo Method\n");
    printf("integral using n=10 f=%lf\n", s10);
    printf("integral using n=100 f=%lf\n", s100);
    printf("integral using n=1000 f=%lf\n", s1000);
    printf("integral using n=1000000 f=%lf\n", s1000000);
    printf("accuracy of n=1000000 is %lf%%\n", 100.0 - dabs(ANS - s1000000)/ANS);
/* --------------------------------------- */


    /* fclose(fp); */
    return 0;
}
