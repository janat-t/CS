#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int main(){
    long i;
    float eps=1.0e-8, huge=1.0e10;
    float s1=0, s2=huge;
    for (i=0; i<10000000; i++){
        s1 += eps;
        s2 += eps;
    }
    s1 += huge;
    cout << s1 << ' ' << s2 << endl;


    float B[5]={5.0, 5.1, 5.2, 5.3, 5.4};
    float *pointer1 = B;
    float *pointer2 = &B[2];
    cout << *pointer1 << endl << *pointer2 << endl << *(B+4) << endl;


    float a = 1/2;
    float b = (float)(1/2);
    float c = (float)1/2;
    float d = (float)1/(float)2;
    cout << a << ' ' << b << ' ' << c << ' ' << d << endl;
    return 0;
}
