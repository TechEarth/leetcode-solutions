class TimeMap:
        
    def __init__(self):
        self.dic = {}

    def set(self, key, value, timestamp):
        if key not in self.dic:
            self.dic[key] = [(timestamp, value)]
        else:
            self.dic[key].append((timestamp, value))
        
    def get(self, key, timestamp):
        if key not in self.dic: return ""
        arr = self.dic[key]
        # print(arr)
        l, r = 0, len(arr)-1
        i = 0
        while l <= r:
            mid = l + (r-l)//2
            if timestamp > arr[mid][0]:
                l = mid+1
            elif timestamp < arr[mid][0]:
                r = mid-1
            else:
                return arr[mid][1]
                
        curTime = arr[r][0]
        return arr[r][1] if timestamp >= curTime else ""