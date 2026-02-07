#include <bits/stdc++.h>
using namespace std;

class RandomizedSet
{
    vector<int> s;
    unordered_map<int, int> m; // value to index mapping

public:
    RandomizedSet()
    {
    }

    bool search(int val)
    {
        return m.find(val) != m.end(); // return true if value exists, false otherwise
    }

    bool insert(int val)
    {
        if (search(val))
            return false;      // if value already exists, return false
        s.push_back(val);      // add value to the end of the vector
        m[val] = s.size() - 1; // s.size() - 1 always goes to the last element of the vector, which is the newly added value
        return true;
    }

    bool remove(int val)
    {
        if (!search(val))
            return false;
        auto it = m.find(val);         // find the index of the value to be removed, it->second gives the index of the value to be removed
        s[it->second] = s.back();      // move the last value in the vector to the index of the value to be removed
        s.pop_back();                  // remove the last value from the vector as it is now moved to the index of the value to be removed and it becomes a duplicate value in the vector
        m[s[it->second]] = it->second; // update the index of the last value in the map to new index after moving it to the index of the value to be removed in the vector
        m.erase(val);                  // now we can safely remove the value from the map as it is no longer in the vector
        return true;
    }

    // in remove we basically swap the value to be removed with the last value in the vector and then remove the last value from the
    // vector, this way we can remove the value in O(1) time complexity without leaving any gaps in the vector.

    int getRandom()
    {
        return s[rand() % s.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */

int main()
{
    RandomizedSet *obj = new RandomizedSet();
    bool param_1 = obj->insert(1);
    bool param_2 = obj->remove(2);
    bool param_3 = obj->insert(2);
    bool param_4 = obj->remove(1);
    bool param_5 = obj->insert(2);
    bool param_6 = obj->getRandom();
    cout << param_1 << "\n"; // true
    cout << param_2 << "\n"; // false
    cout << param_3 << "\n"; // true
    cout << param_4 << "\n"; // true
    cout << param_5 << "\n"; // 2
    cout << param_6 << "\n"; // 2
    return 0;
}