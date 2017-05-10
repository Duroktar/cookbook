#include <iostream>
#include <cmath>

bool isPrime(int64_t n)
{
    for (int64_t i = 2; i <= std::sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int solve()
{
    int64_t rv, target;

    target = 600851475143;

    for (int64_t i = 1; i <= std::sqrt(target); i++)
    {
        if (isPrime(i) && target % i == 0)
        {
            rv = i;
        }
    }

    return rv;
}

int main()
{

    std::cout << "The answer is " << solve() << "\n";

    return 0;
}