
# coding: utf-8

# In[43]:

here are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


# In[105]:

nums1=[1,3]
nums2=[2]
num = nums1 + nums2
num.sort()
if(len(num)%2==0):
    median=(num[int(len(num)/2-1)]+num[int(len(num)/2)])/2
else:
    median=num[int(len(num)/2-0.5)]
median

