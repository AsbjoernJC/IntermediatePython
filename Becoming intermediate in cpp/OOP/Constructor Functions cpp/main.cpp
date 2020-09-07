#include <iostream>

using namespace std;

class Book {    //syntax class Classname {public: };. A class is a blueprint of a datatype an object is an instance of that blueprint/class
    public:     //inside public the methods will be stored.
        string title;   //method name.
        string author;
        int pages;

        Book(){ //it can be beneficial to create a constructor function where the closed parenthesis is passed no arguments. So it is possible to create a class with no args
            title = "No title";
            author = "No author";
            pages = 0;
        }

        Book(string aTitle, string aAuthor, int aPages){ //this is a constructor function. It will be called whenever we instantiate a class. Kinda seems like the dunder method __init__ in python
            //now an argument is expected when instancing a class
            title = aTitle;
            author = aAuthor;
            pages = aPages;
            //Not sure why this will return the attributes when called. But title = title won't.
        }

//        Book(string title, string author, int pages){ //this is a constructor function. It will be called whenever we instantiate a class. Kinda seems like the dunder method __init__ in python
//            //now an argument is expected when instancing a class
//            title = title;
//            cout << title << endl;        does print title....
//            author = author;
//            pages = pages;
//        }
        //a constructor is a basic function that will be called whenever we create an object of a class

};


int main()
{
    Book GoT("Game of Thrones", "George R.R. Martin", 700);       //instancing a class in C++. Class Object;

//    Book HP("Harry Potter");       //instancing a class in C++. Class Object;
//    HP.title = "Harry Potter";
//    HP.author = "JK Rowling";
//    HP.pages = 500;

    cout << GoT.title << endl;
//    cout << HP.author << endl;

    return 0;
}
