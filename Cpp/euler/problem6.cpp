#include <iostream>
#include <cmath>
#include <list>

int sumOfSquares(std::list<int> mylist)
{
    int sum = 0;
    for (std::list<int>::iterator it = mylist.begin(); it != mylist.end(); it++)
    {
        sum += std::pow(*it, 2);
    }
    return sum;
}

int squareOfSum(std::list<int> mylist)
{
    int sum = 0;
    for (std::list<int>::iterator it = mylist.begin(); it != mylist.end(); it++)
    {
        sum += *it;
    }
    return std::pow(sum, 2);
}

int main()
{
    int squareSum, sumSquare, range = 100;

    int myints[range];

    for (int i = 0; i < range; i++)
    {
        myints[i] = i + 1;
    }

    std::list<int> data(myints, myints + sizeof(myints) / sizeof(int));

    squareSum = squareOfSum(data);
    sumSquare = sumOfSquares(data);

    std::cout << "\nThe answer is " << squareSum - sumSquare << "\n";
    return 0;
}
