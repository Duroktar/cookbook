#include <iostream>
#include <map>

int solve()
{
    int accum;
    int a = 0;
    int b = 1;
    int limit = 4000 * 1000;
    int sum = 0;

    while (b < limit)
    {
        accum = a + b;
        a = b;
        b = accum;

        if (b % 2 == 0)
        {
            sum += b;
        }
    }
    return sum;
}

int main()
{

    std::cout << "The answer is " << solve() << "\n";
    return 0;
}