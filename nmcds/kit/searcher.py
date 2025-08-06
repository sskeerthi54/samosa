class WordSearcher:
    def __init__(self,matrix: list[list[str]]):
        self.matrix=matrix

    def search_word(self, word: str) -> list[tuple[int, int]]:
        word = word.lower()
        positions = []

        for row_idx, row in enumerate(self.matrix):
            for col_idx, cell in enumerate(row):
                if cell.lower() == word:
                    positions.append((row_idx, col_idx))

        return positions 

#example
matrix = [
    ["Hello" , "World"],
    ["Hi" , "hello"],
    ["HELLO" , "Python"]
]

searcher = WordSearcher(matrix)
result = searcher.search_word("hello")
print("Positions found",result)