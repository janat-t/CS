#include <iostream>
#include <cmath>
using namespace std;

// ------- CIRCLE CLASS DEFINITION ------- //

class circle{
  public:
    circle(double, double, double);
    void print() const;
    double area() const;
  private:
    double center[2], rad;
};

// ------- SQUARE CLASS DEFINITION ------- //

class square{
  public:
    square(double, double, double);
    void print() const;
    double area() const;
  private:
    double center[2], side;
};

// ---- CIRCLE CLASS IMPLEMENTATION ---- //

circle::circle(double center_x, double center_y, double radius){
  center[0] = center_x;
  center[1] = center_y;
  rad = radius;
}

double circle::area() const{
  return M_PI * rad * rad;
}

void circle::print() const{
  cout << center[0] << " " << center[1] << " " << rad << endl;
}

// ---- SQUARE CLASS IMPLEMENTATION ---- //

square::square(double center_x, double center_y, double edge){
  center[0] = center_x;
  center[1] = center_y;
  side = edge;
}

double square::area() const{
  return side * side ;
}

void square::print() const{
  cout << center[0] << " " << center[1] << " " << side << endl;
}

int main(){
  circle A = circle(0.1, 0.2, 0.3);
  A.print();
  cout << "The area of the circle is: " << A.area() << endl;

  square B = square(0.9, 1.2, 5.3);
  B.print();
  cout << "The area of the square is: " << B.area() << endl;

  return 0;
}
