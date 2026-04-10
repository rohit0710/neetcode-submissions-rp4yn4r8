class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_speed = dict(zip(position, speed))
        position.sort(reverse=True)
        output = []
        for pos in position:
            time = (target - pos)/car_speed[pos]
            if output and output[-1] >= time:
                continue
            else:
                output.append(time)
        return len(output)