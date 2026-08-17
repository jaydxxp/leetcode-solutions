// Last updated: 18/08/2026, 02:13:55
class Solution {
private:
    bool valid(char ch) {
        if (ch >= 'a' && ch <= 'z' || ch >= '0' && ch <= '9' ||
            ch >= 'A' && ch <= 'Z') {
            return 1;
        } else {
            return 0;
        }
    }
    char lowercase(char ch) {
        if (ch >= 'a' && ch <= 'z' || ch >= '0' && ch <= '9') {
            return ch;
        } else {
            char temp = ch + ('a' - 'A');
            return temp;
        }
    }
    bool ispalindrome(string s)
    {
        int l=0;
        int r= s.size()-1;
        while(l<r)
        {
            if(s[l]!=s[r])
            {
                return false;
                break;
            }
            else{l++;
            r--;}
           
        }
        return true;
    }
public:
    bool isPalindrome(string s) {
        string Og="";
        for(int i=0;i<s.size();i++)
        {
            if(valid(s[i]))
            {
                Og.push_back(s[i]);
            }
        }
        for(int i=0;i<Og.size();i++)
        {
            Og[i]=lowercase(Og[i]);
        }
        if(ispalindrome(Og))
        {
            return true;
        }
        return false;
    }
};