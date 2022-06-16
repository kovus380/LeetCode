class Solution {
public:
    int fib(int n) {
        int answer = 0;
        int one_step_before = 1;
        int two_steps_before = 0;
        
        if (n==0) answer = 0;
        else if (n==1) answer = 1;
        
        else {
            for(int i=2 ; i<(n+1) ; i++){
                answer = one_step_before + two_steps_before;
                two_steps_before = one_step_before;
                one_step_before = answer; 
                cout << answer << two_steps_before << one_step_before << endl;
            }
        }
        return answer;
        
        
    }
};