def peakIndexInMountainArray(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #this is will increase 0,1,2,3,0,1

        s,e = 0,len(arr)-1

        while s < e :
            mid = (s+e)//2

            if  arr[mid+1] > arr[mid]:
                s = mid+1

            else : e = mid
        return e



arr =[0,2,1,0]

print(peakIndexInMountainArray(arr))

        
