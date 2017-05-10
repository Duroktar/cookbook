C++ Cheatsheet
==============

C++ is fucking hard. RTFM_

.. _RTFM: http://www.cplusplus.com/doc/


Index
-----

- `Preprocessor Directives`_
- `Namespaces`_
- `Variables`_
- `Functions`_
- `Constants`_
- `Strings`_
- `Arrays`_
- `Conditionals`_
- `Loops`_
- `Pointers`_
- `Conditional ternary operator`_
- `Disclaimer`_


Preprocessor Directives
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: c++

    #include <iostream>
    #include <string>

    // constants can be defined this way
    #define PI  3.14159     // They don't end with a semicolon
    #define NEWLINE  '\n'
    #define SPACE  ' '


Namespaces
~~~~~~~~~~

Used to group code and avoid name collisions. The std namespace
is a popular example. It is similar to namespaces in Python but
the implementation is different, specifically the syntax.. ie: '::'

.. code-block:: c++
        
    #include <iostream>
    using namespace std;

    namespace foo
    {
     int value() { return 5; }
    }

    namespace bar
    {
        const double pi = 3.1416;
        double value() { return 2*pi; }
    }

    int main () {
        cout << foo::value() << '\n';
        cout << bar::value() << '\n';
        cout << bar::pi << '\n';

        return 0;
    }

using

    .. code-block:: c++

        #include <iostream>
        using namespace std;

        namespace first
        {
            int x = 5;
            int y = 10;
        }

        namespace second
        {
            double x = 3.1416;
            double y = 2.7183;
        }

        int main () {
            using first::x;
            using second::y;

            cout << x << '\n';
            cout << y << '\n';

            cout << first::y << '\n';
            cout << second::x << '\n';

            return 0;
        }

variables
~~~~~~~~~

Variables are assigned at the moment of the assignment operation

.. code-block:: c++


    int a, b;

    a = 10;
    b = a;
    a = 4;

    cout << "a: " << a << NEWLINE;
    cout << "b: " << b << NEWLINE;

.. code-block:: bash

    a: 4
    b: 10   # Gotcha!   (If you're coming from Python anyways..)

Functions
~~~~~~~~~

Declaration

    .. code-block:: c++

        #include <iostream>
        using namespace std;

        void odd (int x);
        void even (int x);

        int main()
        {
            int i;

            do {
                cout << "Please, enter number (0 to exit): ";
                cin >> i;
                odd (i);
            } while (i!=0);

            return 0;
        }

        void odd (int x)
        {
            if ((x%2)!=0)  
                cout << "It is odd.\n";
            else 
                even (x);
        }

        void even (int x)
        {
            if ((x%2)==0) 
                cout << "It is even.\n";
            else 
                odd (x);
        }


Default values

    .. code-block:: c++

        #include <iostream>
        using namespace std;

        int divide (int a, int b=2)
        {
            int r;

            r = a/b;
            return (r);
        }

        int main ()
        {
            cout << divide (12) << '\n';
            cout << divide (20,4) << '\n';

            return 0;   
        }


GOTCHA!! - Arguments passed by value and by reference

    If instead of defining duplicate as:

    .. code-block:: c++
    
        void duplicate (int& a, int& b, int& c)  // modifies original a, b, and c

    Was it to be defined without the ampersand signs as:

    .. code-block:: c++
    
        void duplicate (int a, int b, int c)     // Makes copies of the original.

    The variables would not be passed by reference, but by value, creating instead copies of their values. In this case, the output of the program would have been the values of x, y, and z without being modified (i.e., 1, 3, and 7).

    **I assume this is similar to modifying global variables in Python. ie: Bad.**
        *And no doubt this is only a small part of the picture, so, at least be careful*


Passing arrays as arguments
    To accept an array as parameter for a function, the parameters can be declared as 
    the array type, but with empty brackets, omitting the actual size of the array. 
    For example:

    .. code-block:: c++
    
        #include <iostream>
        using namespace std;

        void printarray (int arg[], int length) {
            for (int n=0; n<length; ++n)
                cout << arg[n] << ' ';
            cout << '\n';
        }

        int main ()
        {
            int firstarray[] = {5, 10, 15};
            int secondarray[] = {2, 4, 6, 8, 10};

            printarray (firstarray,3);
            printarray (secondarray,5);
        }

        // this works for multidimensional arrays also
        // ex: void printarray (int myarray[][2][3]) ...


Templates
    Functions could be overloaded for a lot of types, and it could make sense for all 
    of them to have the same body. For cases such as this, C++ has the ability to define 
    functions with generic types using Templates.

    .. code-block:: c++

        template <class SomeType>
        SomeType sum (SomeType a, SomeType b)
        {
            return a+b;
        }

        // call signature: name<template-arguments>(function-arguments) 

        // ex:
        x = sum<int>(10,20);

    Example:

        .. code-block:: c++

            #include <iostream>
            using namespace std;

            template <class T>
            T sum (T a, T b)
            {
                T result;

                result = a + b;
                return result;
            }

            int main () {
                int    i=5, j=6, k;
                double f=2.0, g=0.5, h;

                k = sum<int>(i,j);
                h = sum<double>(f,g);

                cout << k << '\n';
                cout << h << '\n';

                return 0;
            }

            // In some simple cases the type can be inferred automatically
            // so instad of this:
            k = sum<int>(i,j);
            h = sum<double>(f,g);

            // It is possible to instead simply write:
            k = sum(i,j);
            h = sum(f,g);

            // But it can fail and is obviously less explicit

    Advanced example

        .. code-block:: c++

            #include <iostream>
            using namespace std;

            template <class T, class U>
            bool are_equal (T a, U b)
            {
            return (a==b);
            }

            int main ()
            {
            if (are_equal(10,10.0))
                cout << "x and y are equal\n";
            else
                cout << "x and y are not equal\n";
            return 0;
            }


Efficiency considerations and const references


    .. code-block:: c++

        string concatenate (const string& a, const string& b)
        {
            return a+b;
        }

    By qualifying them as const, the function is forbidden to modify the values of 
    neither a nor b, but can actually access their values as references (aliases of 
    the arguments), without having to make actual copies of the strings.

    Therefore, const references provide functionality similar to passing arguments by 
    value, but with an increased efficiency for parameters of large types. That is why
    they are extremely popular in C++ for arguments of compound types. Note though, 
    that for most fundamental types, there is no noticeable difference in efficiency, 
    and in some cases, const references may even be less efficient!


Constants
~~~~~~~~~

.. code-block:: c++

    const double pi = 3.14159;
    const char   newline = '\n';

:NOTE: Constants can also be assigned with Preprocessor statements


Strings
~~~~~~~

string <string>

    .. code-block:: c++

        #include <string>

        string mystring;
        mystring = "test string";   
        // or
        mystring {"test string"};   // Newer & more accepted apparently

        cout << mystring;

        return 0;


stringstream <sstream>

    .. code-block:: c++

        // Simple
        string mystr ("1204");
        int    myint;

        stringstream(mystr) >> myint;

        // More complex
        #include <iostream>
        #include <string>
        #include <sstream>
        using namespace std;

        int main ()
        {
            string mystr;
            float  price  = 0;
            int    quantity = 0;

            cout << "Enter price: ";
            getline (cin,mystr);
            stringstream(mystr) >> price;

            cout << "Enter quantity: ";
            getline (cin,mystr);
            stringstream(mystr) >> quantity;

            cout << "Total price: " << price*quantity << endl;
            return 0;
        }

Strings and null-terminated character sequences

    .. code-block:: c++

        #include <iostream>
        #include <string>
        using namespace std;

        int main ()
        {
            char question1[] = "What is your name? ";
            string question2 = "Where do you live? ";
            char answer1 [80];
            string answer2;
            cout << question1;
            cin >> answer1;
            cout << question2;
            cin >> answer2;
            cout << "Hello, " << answer1;
            cout << " from " << answer2 << "!\n";
            return 0;
        }

Convert C-string to string

    .. code-block:: c++
    
        char myntcs[] = "some text";
        string mystring = myntcs;  // convert c-string to string

        cout << mystring;          // printed as a library string
        cout << mystring.c_str();  // printed as a c-string 

    (note: both c_str and data members of string are equivalent)

Arrays
~~~~~~

An array is a series of elements of the same type placed in contiguous memory 
locations that can be individually referenced by adding an index to a unique 
identifier. Therefore, the foo array, with five elements of type int, can be 
declared as:

.. code-block:: c++
    
    int foo [5];

    // initialise with values
    int foo [5] = { 16, 2, 77, 40, 12071 }; 

    // this will create an array with 2 trailing zeros
    int bar [5] = { 10, 20, 30 };

    // will infer size based on number of arguments
    int foo[] = { 10, 20, 30 };

    // the *universal initialisation* method
    int foo[] { 10, 20, 30 };

NOTE: 
    *The elements field within square brackets [], representing the number of 
    elements in the array, must be a constant expression, since arrays are blocks 
    of static memory whose size must be determined at compile time, before the program 
    runs.*

Example

    .. code-block:: c++
    
        #include <iostream>
        using namespace std;

        int foo [] = {16, 2, 77, 40, 12071};
        int n, result=0;

        int main ()
        {
            for ( n=0 ; n<5 ; ++n )
            {
                result += foo[n];
            }

        cout << result;

        return 0;
        }

Multidimensional

    .. code-block:: c++
    
        #define WIDTH 5
        #define HEIGHT 3

        int jimmy [HEIGHT][WIDTH];
        int n, m;

        int main ()
        {
            for (n=0; n<HEIGHT; n++)
                for (m=0; m<WIDTH; m++)
                {
                    jimmy[n][m]=(n+1)*(m+1);
                }
        }

Passing as arguments to funcitions
    **In C++, it is not possible to pass the entire block of memory represented by an 
    array to a function directly as an argument. What should be passed instead is its 
    address.**

    To accept an array as parameter for a function, the parameters can be declared as 
    the array type, but with empty brackets, omitting the actual size of the array. 
    For example:

    .. code-block:: c++
    
        void procedure (int arg[])

    Complete example:

        .. code-block:: c++
        
            #include <iostream>
            using namespace std;

            void printarray (int arg[], int length) {
                for (int n=0; n<length; ++n)
                    cout << arg[n] << ' ';
                cout << '\n';
            }

            int main ()
            {
                int firstarray[] = {5, 10, 15};
                int secondarray[] = {2, 4, 6, 8, 10};

                printarray (firstarray,3);
                printarray (secondarray,5);
            }

library array <array>

    .. code-block:: c++

        #include <iostream>
        #include <array>
        using namespace std;

        int main()
        {
            array<int,3> myarray {10,20,30};

            for (int i=0; i<myarray.size(); ++i)
                ++myarray[i];

            for (int elem : myarray)
                cout << elem << '\n';
        }


Conditionals
~~~~~~~~~~~~

switch

    .. code-block:: c++

        switch (x) {
        case 1:
            cout << "x is 1";
            break;
        case 2:
            cout << "x is 2";
            break;
        default:
            cout << "value of x unknown";
        }

if/else

    .. code-block:: c++
    
        if (x > 0)
            cout << "x is positive";
        else if (x < 0)
            cout << "x is negative";
        else
            cout << "x is 0";


Loops
~~~~~

for

    .. code-block:: c++

        // basic
        #include <iostream>
        using namespace std;

        int main ()
        {
            for (int n=10; n>0; n--) {
                cout << n << ", ";
            }
            cout << "liftoff!\n";
        }

        // complex
        for ( n=0, i=100 ; n!=i ; ++n, --i )
        {
            // whatever here...
        }

while

    .. code-block:: c++

        #include <iostream>
        using namespace std;

        int main ()
        {
            int n = 10;

            while (n>0) {
                cout << n << ", ";
                --n;
            }

            cout << "liftoff!\n";
        }

do-while

    .. code-block:: c++

        #include <iostream>
        #include <string>
        using namespace std;

        int main ()
        {
            string str;

            do {
                cout << "Enter text: ";
                getline (cin,str);
                cout << "You entered: " << str << '\n';
            } while (str != "goodbye");
        }

Range-based for loop

    The for-loop has another syntax, which is used exclusively with ranges:

    for ( declaration : range ) statement;

    This kind of for loop iterates over all the elements in range, where declaration declares some variable able to take the value of an element in this range. Ranges are sequences of elements, including arrays, containers, and any other type supporting the functions begin and end; Most of these types have not yet been introduced in this tutorial, but we are already acquainted with at least one kind of range: strings, which are sequences of characters.

    An example of range-based for loop using strings:

    .. code-block:: c++

        #include <iostream>
        #include <string>

        using namespace std;

        int main ()
        {
            string str {"Hello!"};

            for (char c : str)
            {
                cout << "[" << c << "]";
            }

            cout << '\n';

            }

            // with auto
            for (auto c : str)
            {
                cout << "[" << c << "]";
            }
        }


Pointers
~~~~~~~~

tl;dr
    - & is the address-of operator, and can be read simply as "address of"
    - \* is the dereference operator, and can be read as "value pointed to by"

Minimal example

    .. code-block:: c++

        int foo, bar, baz;

        bar = 25;
        foo = &bar;  // we say the address is 1776, but in reality, it's probably not
        baz = foo;   // baz equal to foo (1776)
        baz = *foo;  // baz equal to value pointed to by foo (25)

        // these all evaluate to true
        bar == 25
        &bar == 1776
        foo == 1776
        *foo == 25

Declaring pointers

.. code-block:: c++

    #include <iostream>
    using namespace std;

    int main ()
    {
        int firstvalue = 5, secondvalue = 15;
        int * p1, * p2;

        p1 = &firstvalue;  // p1 = address of firstvalue
        p2 = &secondvalue; // p2 = address of secondvalue
        *p1 = 10;          // value pointed to by p1 = 10
        *p2 = *p1;         // value pointed to by p2 = value pointed to by p1
        p1 = p2;           // p1 = p2 (value of pointer is copied)
        *p1 = 20;          // value pointed to by p1 = 20
        
        cout << "firstvalue is " << firstvalue << '\n';
        cout << "secondvalue is " << secondvalue << '\n';

        return 0;
    }


Tip: You declare the pointers with the asterisk on the left side, but when in use their behavior becomes slightly more dynamic and can be thought of like this:

    - If there's an ampersand on the right side of the expression it means your telling the pointer which target it will be setting
    - If there's an asterisk on the left side of the operand it means you're using the pointer to set that target

More elaborate example

    .. code-block:: c++

        #include <iostream>
        using namespace std;

        int main ()
        {
            int numbers[5];
            int * p;

            p = numbers;

            *p = 10;
            p++;
            *p = 20;

            p = &numbers[2];  *p = 30;
            p = numbers + 3;  *p = 40;
            p = numbers;  *(p+4) = 50;

            for (int n=0; n<5; n++)
                cout << numbers[n] << ", ";

            return 0;
        }

    prints:

    .. code-block:: shell
    
        10, 20, 30, 40, 50, 

Pointer initialization

    Pointers can be initialized to point to specific locations at the very moment they are defined:

        .. code-block:: c++
        
            int myvar;
            int * myptr = &myvar;


    The resulting state of variables after this code is the same as after:

        .. code-block:: c++

            int myvar;
            int * myptr;
            myptr = &myvar;


Pointers to functions

    C++ allows operations with pointers to functions. The typical use of this is for passing a function as an argument to another function. Pointers to functions are declared with the same syntax as a regular function declaration, except that the name of the function is enclosed between parentheses () and an asterisk (*) is inserted before the name:

    .. code-block:: c++
    
        #include <iostream>
        using namespace std;

        int addition (int a, int b)
        { 
            return (a+b); 
        }

        int subtraction (int a, int b)
        { 
            return (a-b); 
        }

        int operation (int x, int y, int (*functocall)(int,int))
        {
            int g;
            g = (*functocall)(x,y);
            return (g);
        }

        int main ()
        {
            int m,n;
            int (*minus)(int,int) = subtraction;

            m = operation (7, 5, addition);
            n = operation (20, m, minus);
            cout << n;

            return 0;
        }

    In the example above, minus is a pointer to a function that has two parameters of type int. It is directly initialized to point to the function subtraction:

        .. code-block:: c++

            int (* minus)(int,int) = subtraction;

**PRO-TIP**

    Just go to the site. There's *waaay* to much about pointers for me to copy over.

    - http://www.cplusplus.com/doc/tutorial/pointers/


Conditional ternary operator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: c++

    // 7==5 ? 4 : 3     // evaluates to 3, since 7 is not equal to 5.
    // 7==5+2 ? 4 : 3   // evaluates to 4, since 7 is equal to 5+2.
    // 5>3 ? a : b      // evaluates to the value of a, since 5 is greater than 3.
    // a>b ? a : b      // evaluates to whichever is greater, a or b. 

    int a = 4, b = 10;

    char humanize_bool;
    humanize_bool = (a<b) ? "is" : "isn't";

    cout << "variable a: " << a << " "
         << humanize_bool << " "
         << "smaller than variable b: " << b << " "
         << "\n";

.. code-block:: bash

    $ variable a: 4 is smaller than variable b: 10


Disclaimer
----------

Most of this is from the docs/tutorial at http://www.cplusplus.com/doc/tutorial/. I have merely compiled some learning points to assist me.
