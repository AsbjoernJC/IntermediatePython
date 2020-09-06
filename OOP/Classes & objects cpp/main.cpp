#include <iostream>

using namespace std;

class Book {    //syntax class Classname {public: };. A class is a blueprint of a datatype an object is an instance of that blueprint/class
    public:     //inside public the methods will be stored
        string title;   //method name
        string author;
        int pages;

};


int main()
{
    Book GoT;       //instancing a class in C++. Class Object;
    GoT.title = "Game of Thrones";
    GoT.author = "George R.R. Martin";
    GoT.pages = 700;

    Book HP;       //instancing a class in C++. Class Object;
    HP.title = "Harry Potter";
    HP.author = "JK Rowling";
    HP.pages = 500;

    cout << GoT.pages << endl;
    cout << HP.author << endl;

    return 0;
}
