        words = s.split()
        reversed_words = [word[::-1] for word in words]

        # Join the reversed words to form the final result
        return ' '.join(reversed_words)