class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        time_map_val = [value,timestamp]

        if key in self.time_map:
            self.time_map[key].append(time_map_val)
        else : 
            self.time_map[key] = [time_map_val]
        
        return None

        
    
    def get(self, key: str, timestamp: int) -> str:
         
        if key not in self.time_map:
         return ""
        else : 
          start = 0 
          end = len(self.time_map[key]) - 1
          while start <= end : 
             mid = (start+end)//2
             if  self.time_map[key][mid][1] == timestamp :
                return self.time_map[key][mid][0]
             else: 
                if timestamp < self.time_map[key][mid][1] : 
                    end = mid - 1 
                else :
                    start = mid +1
        
        if end == -1  : 
            return ""
        else : 
            return self.time_map[key][end][0]
        


         
        
