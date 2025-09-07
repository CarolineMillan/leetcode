#include <string>
#include <map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> s_hash;
        map<char, int> t_hash;

        for ( char s_ch : s ) {
            s_hash[s_ch]++;
        }

        for ( char t_ch : t ) {
            t_hash[t_ch]++;
        }
        if (s_hash == t_hash) {
            return true;
        }
        else {
            return false;
        }
    }
};