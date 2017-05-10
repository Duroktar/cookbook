#include <iostream>
#include <boost/format.hpp>

bool smallestMultipleOfAll(long n)
{
    for (long i = 1; i <= 20; i++)
    {
        if (n % i != 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    long count = 1;
    long result;

    while (true)
    {
        if (smallestMultipleOfAll(count))
        {
            result = count;
            break;
        }
        count++;
    }

    std::cout << boost::format("The answer is %d") % result;

    return 0;
}