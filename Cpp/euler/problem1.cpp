#include <iostream>

bool isMultOf3or5(int n) {
    if (n % 3 == 0 || n % 5 == 0) {
        return true;
    }
    return false;
}

int solve(int n) {
    int sum;
    std::cout << "Counting to " << n << std::endl;
    for (int i = 1; i < n; i++) {
        if (isMultOf3or5(i)) {
            std::cout << i << " is a multiple of 3 or 5." << std::endl;
            sum += i;
        }
    }
    return sum;
}

int main() {
    int rv;

    rv = solve(1000);
    std::cout << rv << std::endl;

    return 0;
}
