class Solution:
    def solveEquation(self, E: str) -> str:
    	[L,R] = E.replace('+x',' 1x').replace('-x',' -1x').replace('=x','=1x').replace('+',' ').replace('-',' -').split('=')
    	L, R, LC, RC = ['1x'] + L.split()[1:] if L[0] == 'x' else L.split(), R.split(), [0, 0], [0, 0]
    	for i in L: LC = [LC[0]+int(i[:-1]),LC[1]] if i[-1] == 'x' else [LC[0],LC[1]+int(i)]
    	for i in R: RC = [RC[0]+int(i[:-1]),RC[1]] if i[-1] == 'x' else [RC[0],RC[1]+int(i)]
    	return 'Infinite solutions' if LC == RC else 'No solution' if LC[0] == RC[0] else 'x=' + str((RC[1]-LC[1])//(LC[0]-RC[0]))
		
		