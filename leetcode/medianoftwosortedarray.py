'''
https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
approach: binary search
we need to cut first list at a point and then cut the 2nd list such that left of x and y== right of y and x
1 2 | 3 4
6 7 | 7 8
to
1 2 3 4(maxLeftX) | +inf(minRightX)
-inf(maxLefty) | 6(minRightY) 7 7 8
(req split)

we want maxLeftX <= minRightY && maxLeftY <= minRightX
if not then go left and right in the first list and check to find the req condition 

time complexity =O(log(min(n,m)))
space complexity =O(1)

'''

class Solution(object):
    def findMedianSortedArrays(self, X, Y):
        
        #make X always with smaller length
        if len(X)>len(Y):
            X,Y=Y,X
        lx,ly=len(X),len(Y)
        lxy=lx+ly
        
        #case where anyone of the list is null jusr return the mid of another array
        if lx==0:
            if ly%2==0:
                return float((Y[(ly+1)//2] + Y[(ly-1)//2]))/2
            else:
                return Y[ly//2]
        #we divide both the lists into parts such that len(left part)=len(right part)
        start, end = 0, lx
        
        while start <= end:
            partitionx=(start + end)/2
            partitiony=(lx + ly + 1)/2 - partitionx
            print(partitionx,", ",partitiony)
            
            #incase the partition is at edges
            #if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
            #if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
            if partitionx == 0:
                maxleftx = float('-inf')
            else:
                maxleftx = X[partitionx-1]
            
            if partitionx == lx:
                minrightx = float('inf')
            else:
                minrightx = X[partitionx]
            
            if partitiony == 0:
                maxlefty = float('-inf')
            else:
                maxlefty = Y[partitiony-1]
            
            if partitiony == ly:
                minrighty = float('inf')
            else:
                minrighty = Y[partitiony]
            
            
            print((maxleftx,maxlefty) , (minrightx,minrighty))
            if maxleftx <= minrighty and maxlefty <= minrightx:
                
                # We have partitioned array at correct place
                # Now get max of left elements and min of right elements to get the median in case of 
                # even length combined array size or get max of left for odd length combined array size.
                if (lx + ly )%2==0: 
                    print(max(maxleftx,maxlefty),min(minrightx,minrighty))
                    return float(max(maxleftx,maxlefty) + min(minrightx,minrighty)) /2
                else:
                    return max(maxleftx,maxlefty)
                
            elif maxleftx > minrighty:
                end = partitionx - 1 
            else :
                start = partitionx + 1
                
            print(start,"-",end)
# public class MedianOfTwoSortedArrayOfDifferentLength {

#     public double findMedianSortedArrays(int input1[], int input2[]) {
#         //if input1 length is greater than switch them so that input1 is smaller than input2.
#         if (input1.length > input2.length) {
#             return findMedianSortedArrays(input2, input1);
#         }
#         int x = input1.length;
#         int y = input2.length;

#         int low = 0;
#         int high = x;
#         while (low <= high) {
#             int partitionX = (low + high)/2;
#             int partitionY = (x + y + 1)/2 - partitionX;

#             //if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
#             //if partitionX is length of input then there is nothing on right side. Use +INF for minRightX
#             int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : input1[partitionX - 1];
#             int minRightX = (partitionX == x) ? Integer.MAX_VALUE : input1[partitionX];

#             int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : input2[partitionY - 1];
#             int minRightY = (partitionY == y) ? Integer.MAX_VALUE : input2[partitionY];

#             if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
#                 //We have partitioned array at correct place
#                 // Now get max of left elements and min of right elements to get the median in case of even length combined array size
#                 // or get max of left for odd length combined array size.
#                 if ((x + y) % 2 == 0) {
#                     return ((double)Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY))/2;
#                 } else {
#                     return (double)Math.max(maxLeftX, maxLeftY);
#                 }
#             } else if (maxLeftX > minRightY) { //we are too far on right side for partitionX. Go on left side.
#                 high = partitionX - 1;
#             } else { //we are too far on left side for partitionX. Go on right side.
#                 low = partitionX + 1;
#             }
#         }

#         //Only we we can come here is if input arrays were not sorted. Throw in that scenario.
#         throw new IllegalArgumentException();
#     }

#     public static void main(String[] args) {
#         int[] x = {1, 3, 8, 9, 15};
#         int[] y = {7, 11, 19, 21, 18, 25};

#         MedianOfTwoSortedArrayOfDifferentLength mm = new MedianOfTwoSortedArrayOfDifferentLength();
#         mm.findMedianSortedArrays(x, y);
#     }
# }