import numpy as np

test_table = np.array([[8, 6, 2, 4], [6, 7, 11, 10], [3, 5, 7, 6], [5, 10, 12, 9]])


class HungarianMethod:
    def __init__(self, table):
        self.table = np.asarray(table)
        self.result = np.asarray(table)
        self.mask = np.zeros(self.result.shape)
        self.n_rows = self.result.shape[0]
        self.rows = []
        self.cols = []

    def row_reduction(self):
        row_min = self.result.min(axis=1)
        result = (self.result.transpose() - row_min).transpose()
        print(f'Row Minimum: {row_min}\n'
              f'\n'
              f'{result}')
        return result

    def col_reduction(self):
        col_min = self.result.min(axis=0)
        result = self.result - col_min
        print(f'Column Minimum: {col_min}\n'
              f'\n'
              f'{result}')
        return result

    def minimum_number_of_lines(self):
        shadow = self.result.copy()
        row_sum = np.count_nonzero(shadow == 0, axis=1)
        col_sum = np.count_nonzero(shadow == 0, axis=0)
        n_zeros = (shadow == 0).sum()
        count = 0
        cols = self.cols
        rows = self.rows

        while count < n_zeros:

            max_row = row_sum.max()
            max_col = col_sum.max()

            if max_row >= max_col:
                row = row_sum.argmax()
                self.mask[row, :] = max_row
                rows.append(row)
                count += max_row
            else:
                col = col_sum.argmax()
                self.mask[:, col] = max_col
                cols.append(col)
                count += max_col

            if len(rows) > 0:
                row_sum[rows] = 0
            elif len(cols) > 0:
                col_sum[cols] = 0

        print(f'Covered fields:\n'
              f'\n{self.mask}')

        self.cols = cols
        self.rows = rows

        return (len(self.cols) + len(self.rows)) >= self.result.shape[0]

    def subtract_min_from_remainder(self):
        remainder = self.result[self.mask == 0]
        minimum = remainder.min()
        self.result[self.mask == 0] -= minimum
        print(f'Subtract minimum from untouched fields:\n\n{self.result}')

    def make_assignment(self):
        resources = np.zeros(self.result.shape[0])

        for col in np.arange(0, self.result.shape[0] - 1):
            best_row = self.result
            resources[col] = best_row + 1

        return resources - 1

    def solution(self):
        print(f'Input table:\n{self.table}\n')
        self.result = self.row_reduction()
        self.result = self.col_reduction()
        found_optimal = self.minimum_number_of_lines()

        while not found_optimal:
            print(f'\nLooking for optimal solution...\n\n')
            self.subtract_min_from_remainder()
            found_optimal = self.minimum_number_of_lines()

        print(f'\nOptimal Solution found!\n{self.result}\n\nMaking assignments...')

        print(f'{self.make_assignment()}')
