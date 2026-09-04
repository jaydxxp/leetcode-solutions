// Last updated: 05/09/2026, 01:35:27
/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
private:
    int FindPeak(MountainArray &mountainArr)
    {
        int l=0;
        int r=mountainArr.length()-1;
        int ans=-1;
        while(l<r)
        {
            int mid=l+(r-l)/2;
            if(mountainArr.get(mid)<mountainArr.get(mid+1))
            {
                l=mid+1;
                
            }
            else
            {
                r=mid;
            }
        }
        return l;
    }
    int FindValAsc(MountainArray &mountainArr,int target,int r,int l)
    {
        while(l<=r)
        {
            int mid=l+(r-l)/2;
            int val=mountainArr.get(mid);
            if(val==target)
            {
                return mid;
            }
            else if(val<target)
            {
                l=mid+1;
            }
            else
            {
                r=mid-1;
            }
            
        }
        return -1;
    }
    int FindValDesc(MountainArray &mountainArr,int target,int r,int l)
    {
        while(l<=r)
        {
            int mid=l+(r-l)/2;
            int val=mountainArr.get(mid);
            if(val==target)
            {
                return mid;
            }
            else if(val>target)
            {
                l=mid+1;
            }
            else
            {
                r=mid-1;
            }
            
        }
        return -1;
    }
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int peak= FindPeak(mountainArr);
        int ans= FindValAsc(mountainArr,target,peak,0);
        if(ans!=-1)
        {
            return ans;
        }
        return FindValDesc(mountainArr,target,mountainArr.length()-1,peak+1);
    }
};