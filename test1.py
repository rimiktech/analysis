def move_zeroes(nums):
    if nums is None:
        raise TypeError('nums cannot be None')
    pos = 0
    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1
    if pos < len(nums):
        nums[pos:] = [0] * (len(nums) - pos)

def splitArray(arr, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left, right = max(arr), sum(arr)

        while left < right:
            mid = left + ((right-left) >> 1)
            curr_sum, invalid, groups = 0, True, 0
            for num in arr:
                if num > mid:
                    inalid = False
                    break
                if num + curr_sum > mid:
                    groups += 1
                    curr_sum = 0
                curr_sum += num
            if invalid and groups < m:
                right = mid
            else:
                left = mid + 1
        return left

import os       
from PIL import Image, ImageDraw
def overlay_image(path, coordinates, water_mark_path):
    try:
        img_size = int(os.path.getsize(path)/1024)
        img_coordinates = coordinates
        res = list(map(eval, img_coordinates))
        img1 = Image.open(path)
        idraw = ImageDraw.Draw(img1)
        idraw.rectangle((res[0], res[1], res[2], res[3]), fill='black')
        idraw.rectangle((690, 500, 780, 510), fill='red')
        img2 = Image.open(water_mark_path)
        width, height = img2.size
        img2.paste(img1, (690-int(width/2),500-int(height/2)))                
        img1.save(path)
        return
    except Exception as ex:
        print(ex)


