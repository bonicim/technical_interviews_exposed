"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

"""Commentary

The first and naive approach is to calculate the area for each possible pairs of lines, container, starting from
left to right. This is classic brute force and takes n^2 time.

Another approach involves understanding the problem at a deeper level.

First, note that we have containers within containers when you draw the lines on the Cartesian plane. Also note that the most
exterior container would have the leftmost and rightmost walls. Also note that in general, if we want to maximize the area of a rectangle, we
want the largest base and the largest height. Thus, ideally we want to have the largest base.

Second, note that the height of any container is limited by the smaller of the two exterior lines. For example, if we had heights of 8 and 2, the
actual height of the container would be 2.

Knowing these two things, we can use a sliding window approach to determine the max area. First, we set pointers at the left and right most containers.
We set maxarea to be that area. Then we shrink our window by determining which is the smaller height and the moving the pointer associated with that height in the hopes
of finding a new and larger height. Recall that although we shrink our base, perhaps we can find a really, really big height that will make up for the loss in base. We keep
sliding this window until the pointers overlap. This takes N time.
"""


def two_pointers_solution(height):
    left, right = 0, len(height) - 1
    maxarea = 0

    while left < right:
        smallest_height = min(height[left], height[right])
        base = right - left
        current_area = base * smallest_height

        maxarea = max(maxarea, current_area)

        if height[left] < height[right]:
            left += 1
        elif height[right] < height[left]:
            right -= 1
        # if both sides are equal, then we keep checking to see if there is still a larger side
        # it doesn't matter which side we should shrink since they're both equal
        else:
            right -= 1
            # left +=1

    return maxarea


def brute_force(height):
    maxarea = 0

    for index, high in enumerate(height):
        for right_index in range(index + 1, len(height)):
            smallest_height = min(high, height[right_index])
            base = right_index - index
            area = smallest_height * base
            maxarea = max(maxarea, area)

    return maxarea
