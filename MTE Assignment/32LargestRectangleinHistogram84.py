def LargestRectangleArea(heights):
    heights.append(0)
    stack = []
    max_area = 0
    for i , h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i  if not stack else i - stack[-1] - 1
            max_area = max(max_area,height * width)
        stack.append(i)
        
    return max_area
heights = [2,1,5,6,2,3]
print(LargestRectangleArea(heights))
heights = [2,4]
print(LargestRectangleArea(heights))


