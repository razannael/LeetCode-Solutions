class Solution:

	def __init__(self, radius: float, x_center: float, y_center: float):
		self.r = radius
		self.x, self.y = x_center, y_center
    

	def randPoint(self) -> List[float]:
		theta = uniform(0,2*pi)
		R = sqrt(uniform(0,self.r**2))
		return [self.x+R*cos(theta), self.y+R*sin(theta)]