
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        Q = ["0000"]
        visited = set()
        deadends = set(deadends)
        front = 0
        minimum_steps = 0

        if "0000" in deadends:
            return -1

        visited.add("0000")

        while front < len(Q):
            size = len(Q) - front

            for i in range(size):
                current = Q[front]
                front += 1

                if current == target:
                    return minimum_steps

                for j in range(4):
                    digit = int(current[j])

                    for change in [-1, 1]:
                        new_digit = (digit + change) % 10
                        new_state = current[:j] + str(new_digit) + current[j + 1:]

                        if new_state not in deadends and new_state not in visited:
                            Q.append(new_state)
                            visited.add(new_state)

            minimum_steps += 1

        return -1
