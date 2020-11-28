#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double f(double x){
    return x*x-3;
}

double dfdx(double x){
    return 2*x;
}

double bisection(double a, double b, int n);

double newton(double x, int n);

int main(){
    double a = 1.0;
    double b = 2.0;
    double x0 = 1.0;
    int n = 10;
    printf("The positive root of f(x)=x^2-3=0\n");
    printf("Using Bisection Method: %lf\n", bisection(a, b, n));
    printf("Using Newton-Raphson Method: %lf\n", newton(x0, n));
    return 0;
}

double bisection(double a, double b, int n){
    double c = (a+b)/2;
    if(n==0)
        return c;
    if((f(a)<0&&f(c)>0)||(f(a)>0&&f(c)<0))
        return bisection(a, c, n-1);
    else
        return bisection(c, b, n-1);
}

double newton(double x, int n){
    if(n==0)
        return x;
    return newton(x-f(x)/dfdx(x), n-1);
}

