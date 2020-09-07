#include <iostream>

using namespace std;

class Chef { //super class
    public:
        void makeChicken(){
            cout << "The chef makes chicken" << endl;
        }
        void makeSalad(){
            cout << "The chef makes salad" << endl;
        }
        void makeSpecialDish(){
            cout << "The chef makes bbq ribs" << endl;
        }
};

class ItalianChef : public Chef{          //the Italian chef can make everything the normal Chef can do and more. Subclass
    //creating a child class syntax: class ChildClassName : public ParentClassName{};
    public:
        void makePasta(){
            cout << "The Italian chef makes pasta" << endl;
        }
        void makeSpecialDish(){     //overwriting an instance function
            cout << "The Italian chef makes chicken parm" << endl;      //not sure how to access the parent class from inside a method of a child class in c++
//            cout << Chef().makeSpecialDish() << endl;   //doesn't work
        }
};

int main()
{

    Chef chef;
    chef.makeChicken();

    ItalianChef italianchef;
    italianchef.makeChicken();
    italianchef.makePasta();
    italianchef.makeSpecialDish();
    return 0;
}
