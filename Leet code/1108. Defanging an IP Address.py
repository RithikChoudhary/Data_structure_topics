class Solution:
    def defangIPaddr(self, address: str) -> str:
        var = ""      
        for i in address:
            if "." in i:
                var = var + "[{}]".format
            else:
                var = var + i
        return var
    
