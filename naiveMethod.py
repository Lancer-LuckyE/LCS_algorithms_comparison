import time

class naiveMethod:
    def __init__(self):
        self.__result = []
        self.__time_cost = 0.0  # in sec
        self.__sub_seq = []

    def get_Result(self):
        return self.__result

    def get_Time(self):
        return self.__time_cost

    def __get_Sub_Seq(self, seq, cur_index, sub_seq):
        """
        Add all sub_sequence in the call attribute sub_seq
        :param seq: a list, the origin list
        :param cur_index: current index of the origin list
        :param sub_seq: the subsquence found
        :return: a list of all subsequence found in the given sequence.
        """
        if cur_index == len(seq):
            if len(sub_seq) != 0:
                self.__sub_seq.append(sub_seq)
        else:
            self.__get_Sub_Seq(seq, cur_index + 1, sub_seq)
            self.__get_Sub_Seq(seq, cur_index + 1, sub_seq + [seq[cur_index]])
        return self.__sub_seq

    def __is_sub_seq(self, sub_seq, seq):
        """
        Check is the first sequence is a subsequence of the second given sequence
        :param sub_seq: a list, the sequence to be check if it is a subsequence
        :param seq: a list
        :return: boolean, true if sub_seq is subsequence of the seq, false otherwise
        """
        m = 0
        for n in seq:
            if n == sub_seq[m]:
                m += 1
                if m == len(sub_seq):
                    break
        if m == len(sub_seq):
            return True
        else:
            return False

    def run(self, seq1, seq2):
        """
        Run the algorithm
        :param seq1: a list
        :param seq2: a list
        :return:
        """
        max_len = 0
        start_time = time.time()
        sub_seqs1 = self.__get_Sub_Seq(seq1, 0, [])
        for sub_seq in sub_seqs1:
            if self.__is_sub_seq(sub_seq, seq2) and len(sub_seq) > max_len:
                max_len = len(sub_seq)
                self.__result = sub_seq
        # time.sleep(5)
        end_time = time.time()
        self.__time_cost = end_time - start_time
