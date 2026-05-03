class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        counter = 1
        prev = chars[0]

        for i in range(1, len(chars) + 1):
            if i == len(chars):
                char = None
            else:
                char = chars[i]
            
            if char == prev:
                counter += 1
            elif counter > 1:
                string = prev + str(counter)
                s += string
                counter = 1
            else:
                s += prev
            prev = char
        
        s.split()
        chars[:len(s)] = s
        
        return len(s)