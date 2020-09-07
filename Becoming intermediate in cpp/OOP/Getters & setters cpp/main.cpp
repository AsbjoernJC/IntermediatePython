#include <iostream>

using namespace std;

class Movie{
    private: //only code inside the Movie class can access the rating
        string rating;
    public: //any other program/code can access public's block of code
        string title;
        string director;

        Movie(string aTitle, string aDirector, string aRating){
            title = aTitle;
            director = aDirector;
            setRating(aRating); //will open setRating function
        }
    //getters and setters allow us to control the access to different attributes and elements of classes. Setters used for controlling what can be passed. In this case "Dog" is an invalid rating

        void setRating(string aRating){
            if(aRating == "G" || aRating == "PG" ||aRating == "PG-13" || aRating == "R" || aRating == "NR"){
                rating = aRating;
            } else {
                rating = "NR";
            }

        }

        string getRating(){
            return rating;
        }

};

int main()
{

    Movie avengers("The Avengers", "Joss Whedon", "Pg-13"); //nothing is stopping me for passing non-relevant information when creating the class. This can be enforced

//    cout << avengers.rating; //not possible to access outside of the Movie class scope because rating is private
    avengers.setRating("Dog");

    cout << avengers.getRating();


    return 0;
}
