
class Solution:
    def minMutation(self, startGene, endGene, bank):
        visited = {startGene}
        queue = [startGene]
        front = 0
        mutation = 0

        while front < len(queue):
            size = len(queue) - front

            for _ in range(size):
                curr_gene = queue[front]
                front += 1

                if curr_gene == endGene:
                    return mutation

                for gene in bank:
                    if gene not in visited:
                        count = 0

                        for i in range(8):
                            if curr_gene[i] != gene[i]:
                                count += 1

                        if count == 1:
                            visited.add(gene)
                            queue.append(gene)

            mutation += 1

        return -1
