#include <iostream>
using namespace std;

// === CLASS FRUIT DEFINITION === //

class fruit
{
public:
	fruit();
	fruit(string clr, string shp, float sz);
	string read_color(bool lprint) const;
	void change_color(string newcolor);
private:
	string color;
	string shape;
	float size;
};

fruit::fruit(){
	color = "green";
	shape = "spindle";
	size = 1.2;
}

fruit::fruit(string clr, string shp, float sz){
	color = clr;
	shape = shp;
	size = sz;
}

string fruit::read_color(bool lprint) const{
	if (lprint)
		cout << color << endl;
	return color;
}

void fruit::change_color(string clr){
	color = clr;
}

int main(){
	bool lprint = true;
	fruit fig = fruit("red", "heart", 1.1);
	string fig_color = fig.read_color(lprint); // print
	cout << fig_color << endl;

	fruit apple = fruit("yellow", "round", 2.0);
	string color = apple.read_color(lprint);  // print

	apple.change_color("green");
	string apple_color = apple.read_color(lprint);
	return 0;
}