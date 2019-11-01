import time


class dynamicProgramming:
    def __init__(self, size1, size2):
        self.__result = []
        self.__time_cost = 0.0  # in sec
        self.__size1 = size1
        self.__size2 = size2
        self.__accumulated_table = []  # to keep trace on the length of the subsequence
        self.__solution_table = []  # to keep trace on the solution subsequence

    def get_Result(self):
        return self.__result

    def get_Time(self):
        return self.__time_cost

    def get_accumulated_table(self):
        return self.__accumulated_table

    def get_solution_table(self):
        return self.__solution_table

    def fill_tables(self, seq1, seq2):
        """
        Fills up two tables, accumulated length table and the solution construction table
        :param seq1: a list, the first sequence
        :param seq2: a list, the second sequence
        :return: return the filled accumulated length table and the solution construction table
        """
        for i in range(self.__size1 + 1):
            accumulated_row = []
            solution_row = []
            for j in range(self.__size2 + 1):
                accumulated_row.append(0)
                solution_row.append('X')
            self.__accumulated_table.append(accumulated_row)
            self.__solution_table.append(solution_row)

        for i in range(1, self.__size1 + 1):
            for j in range(1, self.__size2 + 1):
                if seq1[i - 1] == seq2[j - 1]:
                    self.__accumulated_table[i][j] = self.__accumulated_table[i - 1][j - 1] + 1
                    self.__solution_table[i][j] = 'Down'
                else:
                    if self.__accumulated_table[i - 1][j] >= self.__accumulated_table[i][j - 1]:
                        self.__accumulated_table[i][j] = self.__accumulated_table[i - 1][j]
                        self.__solution_table[i][j] = 'Up'
                    else:
                        self.__accumulated_table[i][j] = self.__accumulated_table[i][j - 1]
                        self.__solution_table[i][j] = 'Left'

        return self.__accumulated_table, self.__solution_table

    def __run(self, seq1, i, j):
        """
        Constructs the solution of the longest subsequence
        :param seq1: a list, the first sequence
        :param i: int, length of the first sequence
        :param j: int, length of the second sequence
        :return:
        """
        if i == 0 or j == 0:
            return
        if self.__solution_table[i][j] == 'Down':
            self.__run(seq1, i - 1, j - 1)
            self.__result.append(seq1[i - 1])
        elif self.__solution_table[i][j] == 'Up':
            self.__run(seq1, i - 1, j)
        else:
            self.__run(seq1, i, j - 1)

    def run(self, seq1, seq2):
        """
        Runs the algorithm
        :param seq1: a list
        :param seq2: a list
        :return:
        """
        start_time = time.time()
        self.fill_tables(seq1, seq2)
        self.__run(seq1, self.__size1, self.__size2)
        end_time = time.time()
        self.__time_cost = end_time - start_time