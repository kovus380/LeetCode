#include <string>
using namespace std;
class Solution {
public:
    int subtractProductAndSum(int n) {
        int products = 1;
        int sums = 0;
        while (n > 9) {
            products *= (n % 10);
            sums += (n % 10);
            n /= 10;
        }
        return (products * (n % 10)) - (sums + (n % 10));
    }
};