// Last updated: 29/07/2026, 01:07:50
class Solution {
public:
    int lengthOfLastWord(string s) {
        int end= s.length()-1;
        while(end>=0 && s[end]==' '){
            end--;
        }
        int start=end;
        while(start>=0 && s[start]!=' '){
            start--;
        }
        return end-start;
    }
};