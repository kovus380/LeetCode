class Solution {
public:
    int climbStairs(int n) {
        int answer = 0;
        int one = 1;
        int two = 2;
        if (n == 1) answer = 1;
        else if (n == 2) answer = 2;
        else {
            for (int i=3 ; i < (n+1) ; i++){
                answer = one + two;
                one = two;
                two = answer;
            }
        }
        return answer;
    }
};