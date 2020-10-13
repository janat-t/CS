#include <iostream>
using namespace std;
int main(){
	int diosmos = 1;
	for(diosmos=1; diosmos<=4; diosmos++){
		switch(diosmos){
			case 1:{cout << "Two ";}
			break;
			case 2:{cout << "gallons ";}
			break;
			case 3:{cout << "of Milk" << endl;}
			break;
		}
	}
	return 0;
}