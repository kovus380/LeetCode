#include <numeric>
class Solution {
public:
    double average(vector<int>& salary) {
        double num = sum(salary);
        double mid = num - (*max_element(salary.begin(), salary.end())) - (*min_element(salary.begin(), salary.end()));
        return mid / (salary.size() - 2);
    }
    double sum(vector<int>& nums) {
        double num = 0;
        for(int i = 0 ; i < nums.size() ; i++) {
            num += nums[i];
        }
        return num;
    }
};