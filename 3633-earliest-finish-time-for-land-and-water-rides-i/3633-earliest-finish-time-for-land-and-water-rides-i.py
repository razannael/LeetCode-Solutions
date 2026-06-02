#sreesha
class Solution:
    def earliestFinishTime(self, lst: List[int], ldt: List[int], wst: List[int], wdt: List[int]) -> int:
        def bs(val,arr):
            low=0
            high=len(arr)-1
            ans=-1
            while low<=high:
                mid=(low+high)>>1
                if arr[mid][0]>val:
                    high=mid-1
                else:
                    ans=mid
                    low=mid+1
            return ans
        land_slide=[]
        water_slide=[]
        suffix_min_land_slide=[float('inf')]*(len(lst))
        prefix_min_land_slide=[]
        prefix_min_water_slide=[]
        suffix_min_water_slide=[float('inf')]*(len(wst))

        #land slide implementation
        for i in range(len(lst)):
            land_slide.append((lst[i],ldt[i]))
        land_slide.sort()
        #for prefix just see the duration time 
        #prefix land slide
        for i in range(len(lst)):
            if i==0:
                prefix_min_land_slide.append(land_slide[0][1])
            else:
                prefix_min_land_slide.append(min(prefix_min_land_slide[-1],land_slide[i][1]))

        #suffix land_slide
        #for suffix min see the sum of start and duration
        for i in range(len(lst)-1,-1,-1):
            if i==len(lst)-1:
                suffix_min_land_slide[-1]=min(suffix_min_land_slide[-1],(land_slide[i][0]+land_slide[i][1]))
            else:
                suffix_min_land_slide[i]=min(suffix_min_land_slide[i+1],(land_slide[i][0]+land_slide[i][1]))

        #water slide implementation
        for i in range(len(wst)):
            water_slide.append((wst[i],wdt[i]))
        water_slide.sort()

        #suffix water slide
        for i in range(len(wst)-1,-1,-1):
            if i==len(wst)-1:
                suffix_min_water_slide[-1]=min(suffix_min_water_slide[-1],(water_slide[i][0]+water_slide[i][1]))
            else:
                suffix_min_water_slide[i]=min(suffix_min_water_slide[i+1],(water_slide[i][0]+water_slide[i][1]))
        #prefix water slide
        for i in range(len(wst)):
            if i==0:
                prefix_min_water_slide.append(water_slide[0][1])
            else:
                prefix_min_water_slide.append(min(prefix_min_water_slide[-1],water_slide[i][1]))
        #go on land_slide first 
        ans=float('inf')
        for i in range(len(lst)):
            #we are picking this 
            end=land_slide[i][0]+land_slide[i][1]
            idx=bs(end,water_slide)
            if idx==-1:
                ans=min(ans,suffix_min_water_slide[0])
            else:
                ans=min(ans,(suffix_min_water_slide[idx+1] if idx+1<len(wst) else float('inf')),prefix_min_water_slide[idx]+end)
        for i in range(len(wst)):
            #we are picking this 
            end=water_slide[i][0]+water_slide[i][1]
            idx=bs(end,land_slide)
            if idx==-1:
                ans=min(ans,suffix_min_land_slide[0])
            else:
                ans=min(ans,(suffix_min_land_slide[idx+1] if idx+1<len(lst) else float('inf')),prefix_min_land_slide[idx]+end)
        return ans
        