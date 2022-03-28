class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        instructions1 = instructions.split()
        current_orientation = 0  # up: 0/right: 1,  down:2 /left: 3
        orientation_dict = {0: 1, 1: 1, 2: -1, 3: -1}
        current_position = [0, 0]

        for instruction in instructions:
            if instruction == "G":
                if current_orientation == 0 or current_orientation == 2:
                    # move in the y
                    current_position[1] += orientation_dict[current_orientation]

                else:
                    # move in the x
                    current_position[0] += orientation_dict[current_orientation]

            elif instruction == "R":
                current_orientation = (current_orientation + 1) % 4
            else:
                current_orientation = (current_orientation - 1) % 4
                if current_orientation == -1:
                    current_orientation = 3
        # current_orientation & current_position work

        if current_orientation != 0 or current_position == [0, 0]:
            return True
        return False

print(Solution.isRobotBounded(Solution(),"GG"))