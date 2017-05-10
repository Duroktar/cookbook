#include <string>
#include <iostream>
#include <boost/format.hpp>
#include <algorithm>

bool isPalindrome(std::string s)
{
    std::string r = s;
    std::reverse(r.begin(), r.end());
    if (r != s)
    {
        return false;
    }
    return true;
}

int solve()
{

    int prod, accum;

    accum = 0;
    for (int x = 0; x < 1000; x++)
    {
        for (int y = 0; y < 1000; y++)
        {
            prod = x * y;
            if (isPalindrome(std::to_string(prod)) &&
                prod > accum)
            {
                accum = prod;
            }
        }
    }
    return accum;
}

int main()
{

    std::cout << boost::format("The answer is %i") % solve() << "\n";
    return 0;
}