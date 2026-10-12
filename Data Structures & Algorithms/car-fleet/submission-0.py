class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        minFleetTime = float("-inf")

        times = list(zip(position, speed))
        times.sort(key=lambda x: x[0], reverse=True)

        for i in range(len(times)):
            position, speed = times[i]
            time = (target - position) / speed
            if minFleetTime < time:
                fleet += 1
                minFleetTime = time
        
        return fleet
