#include <iostream>
#include <array>

using namespace std;

int main()
{
    int stockPrices[2];
    stockPrices[0] = 298;
    stockPrices[1] = 305;
    stockPrices[2] = 320;
    stockPrices[3] = 301;
    stockPrices[4] = 292; //fucker den op Det er et static array, hvilket vil sige array size er fixed og man kan derfor ikke inserte et element uden for størrelsen

//    int dstockPrices[] = {};
//    dstockPrices[0] = 298;
//    dstockPrices[1] = 305;
//    dstockPrices[2] = 320;
//    dstockPrices[3] = 301;
//    dstockPrices[4] = 292;

    int i,n;
    int * p;
    cout << "How many numbers would you like to type? ";
    cin >> i;
    p= new (nothrow) int[i];
    if (p == nullptr)
        cout << "Error: memory could not be allocated";
    else
    {
        for (n=0; n<i; n++)
    {
            cout << "Enter number: ";
            cin >> p[n];
    }
    cout << "You have entered: ";
    for (n=0; n<i; n++)
      cout << p[n] << ", ";
    delete[] p;
  }
// her bliver memory dynamically allocated via new keyword.

//Der er åbenbart et dynamic array i c++, std::vector
//    cout << dstockPrices[4]; //dynamic arrays er ikke som sådan standard i c++, så ovenstående fungerer ikke.
////    cout << stockPrices[4];


    return 0;
}
