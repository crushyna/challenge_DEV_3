import random


class DNASequenceObject:

    def __init__(self, sequence: str):
        self.original_sequence = self.confirm_original_sequence(sequence)

    def confirm_original_sequence(self, sequence) -> str:
        message = f"{sequence} added"
        self.original_sequence = sequence
        print(message)
        return self.original_sequence

    def get_reverse_sequence(self) -> str:
        return self.original_sequence[::-1]

    def extend_sequence(self, number: int) -> str:
        available_characters = ['A', 'T', 'C', 'G', 'N']
        new_string = self.original_sequence
        for i in range(number):
            random_char = random.choice(available_characters)
            new_string = new_string + random_char

        self.original_sequence = new_string
        return self.original_sequence

    def trim_sequence(self, desired_length: int) -> str:
        self.original_sequence = self.original_sequence[:desired_length]

        return self.original_sequence

    def read_from_file(self, filename: str) -> str:
        f = open(filename, "r")
        new_sequence = f.read().strip()
        self.original_sequence = new_sequence

        return self.original_sequence
