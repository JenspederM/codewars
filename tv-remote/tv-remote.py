class TvRemote:
    def total_word_distance(self, word, n_cols=8, click=1, start_button='a'):
        def manhattan_distance(current_char, next_char, click=True):
            keys = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
            keyboard = {c: (i // n_cols, i % n_cols) for i, c in enumerate(keys)}
            cc_pos = keyboard.get(current_position)
            nc_pos = keyboard.get(next_position)
            x_distance = cc_pos[0] - nc_pos[0]
            y_distance = cc_pos[1] - nc_pos[1]
            return abs(x_distance) + abs(y_distance) + int(click)

        keys = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
        keyboard = {c: (i // n_cols, i % n_cols) for i, c in enumerate(keys)}
        total_distance = manhattan_distance(start_button, keys[0], click=False)

        for cc, nc in word, word[1:]:
            if nc == cc:
                total_distance += click
            else:
                cc_pos = keyboard.get(cc)
                nc_pos = keyboard.get(nc)
                total_distance += manhattan_distance(cc_pos, nc_pos, click=True)

        return total_distance


if __name__ == '__main__':
    remote = TvRemote()
    print(remote.total_word_distance('codewars'))
