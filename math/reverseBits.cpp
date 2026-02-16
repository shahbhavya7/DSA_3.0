#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int reverseBits(int n) {
        string binary = "";
        bitset<32> binary_representation(n);  // Convert the integer to a 32-bit binary representation using bitset
        binary = binary_representation.to_string(); // Convert the bitset to a string
        reverse(binary.begin(), binary.end()); // Reverse the string to get the reversed binary representation
        bitset<32> reversed_binary(binary); // Convert the reversed binary string back to a bitset
        return (int)reversed_binary.to_ulong(); // Convert the reversed bitset back to an unsigned long and return it as an integer
    }
};


int main(){
    Solution sol;
    int n = 43261596;
    int result = sol.reverseBits(n);
    cout << "Reversed Bits: " << result << endl;
    return 0;
}