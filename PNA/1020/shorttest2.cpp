#include <iostream>
using namespace std;

double ratio1(double, double);      						// function prototype
double (*point_ratio)(double, double) = ratio1;				// and its pointer

double product(double, double);								// fundtion prototype
double (*point_product)(double, double) = product;			// and pointer

double addition(double, double);							// funcion prototype
double (*point_addition)(double, double) = addition;		// and pointer

double subtraction(double, double);							// funcion prototype
double (*point_subtraction)(double, double) = subtraction;	// and pointer

double operate(double, double, double(*)(double, double));

int main(){
	int menu;
	double a = 4.0;
	double b = 2.0;
	double result;

	cout << "Please enter\n1 for the ratio\n2 for the product\n3 for the addition\n4 for the subtraction" << endl;
	cout << "q to quit" << endl;
	cout << "q to quit" << endl;

	while (cin >> menu){
		if (menu == 1){
			result = operate(a,b,point_ratio);
			cout << a << " / " << b << " = " << result << endl;
		}
		else if (menu == 2){
			result = operate(a,b,point_product);
			cout << a << " x " << b << " = " << result << endl;
		}
		else if (menu == 3){
			result = operate(a,b,point_addition);
			cout << a << " + " << b << " = " << result << endl;
		}
		else if (menu == 4){
			result = operate(a,b,point_subtraction);
			cout << a << " - " << b << " = " << result << endl;
		}
	}

	return 0;
}

/*---------------- ratio --------------*/

double ratio1(double a, double b){
	double c = a/b;
	return c;
}

/*----------------product--------------*/

double product(double a, double b){
	double c = a*b;
	return c;
}

/*----------------addition--------------*/

double addition(double a, double b){
	double c = a+b;
	return c;
}

/*----------------subtraction--------------*/

double subtraction(double a, double b){
	double c = a-b;
	return c;
}

/*----------------operate---------------*/

double operate(double a, double b, double (*funcall)(double, double)){
	double c = (*funcall)(a,b);
	return c;
}