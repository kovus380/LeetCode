class Solution {
public:
    int countOdds(int low, int high) {
        int end;
        end = (low % 2 == 1) + (high % 2 == 1);
        if (end == 0) {
            return (high - low) / 2;
        }
        else if (end == 1) {
            return (high - low + 1) / 2;
        }
        else {
            return (high - low + 2) / 2;
        }
    }
};