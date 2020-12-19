"""
    只与最后一个元素0的前面的连续1的个数有关系。
    似乎大家都沒有理解最高贊的評論，都是從0開始遍歷數組。事實上因為只要數組最後一個數是0，那麼這個數組肯定可以被0，10，11分割。那麼只需要考慮最後一個0前面連續1的個數，個數是偶數則TRUE，否則FALSE。所以從數組末尾開始遍歷效率會更高。
"""
"""
作者：pu-pu-pu-wu
链接：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/solution/cong-zui-hou-2ge-wei-zhi-de-shu-zi-lai-pan-duan-by/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # 遍历数组，遇0 索引+1, 遇1索引+2
        n = len(bits)
        i = 0
        while i < n-2:
            if bits[i]==0:
                i+=1
            else:
                i+=2
        # 跳出循环后，如果直接跳到导数第二个位置，则做如下判断：
        if i == n-2 and bits[-2] == 1:
            return False
        else:
            return True
        # 跳出循环，如果直接跳到最后一个位置，则只能是True(已经包含在上面的else当中了，不需要下面的判断)
        # if i == n-1:
        #     return True


