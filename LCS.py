class LCS:
    def __init__(self, seq1, seq2, algo):
        """
        Create a new incident for LCS class
        :param seq1: a list
        :param seq2: a list
        :param algo: the algorithm object to be chosen
        """
        self.seq1 = seq1
        self.seq2 = seq2
        self.algo = algo

    def run(self):
        """
        Run the algorithm
        :return: result list and the time cost
        """
        self.algo.run(self.seq1, self.seq2)
        result = self.algo.get_Result()
        time = self.algo.get_Time()

        return result, time

