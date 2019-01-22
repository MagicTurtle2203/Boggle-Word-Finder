class WordChecker:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0])
        self.letter_dict = self._create_letter_dict()

    def find_word(self, word: str) -> bool:
        stack = self._find_first_indexes(word[0])
        word_index = 1

        while stack:
            curr, used, prefix = stack.pop()
            if prefix == word:
                return True
            else:
                stack_len = len(stack)

                if word_index < len(word) - 1:
                    stack.extend((j, used | {j}, prefix + word[word_index])
                                 for j in self.get_adjacent(curr) if j not in used
                                 and self.letter_dict[j] == word[word_index + 1])
                else:
                    stack.extend([(curr, used | {curr}, prefix + word[word_index])])

                if stack_len < len(stack):
                    word_index += 1
        return False

    def get_adjacent(self, index: (int, int)) -> {(int, int)}:
        index_list = []

        for rdelta, cdelta in [(i, n) for i in range(-1, 2) for n in range(-1, 2) if i != 0 or n != 0]:
            if 0 <= index[0] + rdelta < self.rows and 0 <= index[1] + cdelta < self.columns:
                index_list.append((index[0] + rdelta, index[1] + cdelta))

        return index_list

    def _find_first_indexes(self, letter: str) -> [((int, int), {(int, int)}, str)]:
        result_list = []

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == letter:
                    result_list.append(((x, y), {(x, y)}, letter))

        return result_list

    def _create_letter_dict(self):
        letter_dict = dict()

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                letter_dict[(x, y)] = self.board[x][y]

        return dict(letter_dict)


if __name__ == '__main__':
    testBoard = [
        ["E", "A", "R", "A"],
        ["N", "L", "E", "C"],
        ["I", "A", "I", "S"],
        ["B", "Y", "O", "R"]]

    testBoard1 = [
        ["I", "L", "A", "W"],
        ["B", "N", "G", "E"],
        ["I", "U", "A", "O"],
        ["A", "S", "R", "L"]]

    # assert WordChecker(testBoard).find_word("RACE")
    # assert WordChecker(testBoard1).find_word("BINGO")
    # assert WordChecker(testBoard1).find_word("LINGO")
    assert WordChecker(testBoard1).find_word("ILNBIA")
    assert WordChecker(testBoard1).find_word("BUNGIE") is False
    assert WordChecker(testBoard1).find_word("BINS") is False
    assert WordChecker(testBoard1).find_word("SINUS") is False