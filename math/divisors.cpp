#include<bits/stdc++.h>
using namespace std;

vector<int> findDivisors(int n){
    vector<int> divisors;
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0){
            divisors.push_back(i);
            if (i != n / i){
                divisors.push_back(n / i); // add complementary divisor if it's different from i i.e for 36 when i=6, we don't want to add 6 again as 
                // it's the same divisor, but for i=2 we also add 18 which is n/i
            }
        }
    }
    sort(divisors.begin(), divisors.end());
    return divisors;
}
// we only need to loop up to sqrt(n) because any divisor larger than sqrt(n) will have a complementary divisor that is smaller than sqrt(n). 
// For example, if n=36, the divisors are 1, 2, 3, 4, 6, 9, 12, 18, 36. When we reach i=6 (which is sqrt(36)), we find that 36 % 6 == 0, 
// so we add both 6 and its complementary divisor 36/6 = 6. However, since they are the same, we only add it once. 
// For i=2, we add both 2 and its complementary divisor 36/2 = 18. This way we efficiently find all divisors without having to check every number up to n.
int main(){
    int n = 36;
    vector<int> divisors = findDivisors(n);
    cout << "Divisors of " << n << ": ";
    for (int divisor : divisors) {
        cout << divisor << " ";
    }
    return 0;
}