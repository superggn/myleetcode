"""
    完全封装版本
    重写ordered dict
    get和put都是访问元素，重写时添加移动元素在链表中位置的功能
    https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/
"""
import collections


class LRUCache(collections.OrderedDict):
    """
        继承ordered_dict
        定义get和post
        get：    把访问的变量放到最后
                返回访问的变量
        post：   把访问的变量放到最后
                更改访问的变量
                若超过该点最大值，pop访问时间最早的变量

    """


    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
