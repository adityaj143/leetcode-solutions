class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            # Find all words that fit in this line
            line_words = []
            line_length = 0

            while i < len(words):
                word_len = len(words[i])

                # +1 is for the space before the new word
                if line_length + word_len + len(line_words) > maxWidth:
                    break

                line_words.append(words[i])
                line_length += word_len
                i += 1

            # Last line OR only one word
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)
                continue

            # Fully justify the line
            total_spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            # Minimum spaces per gap
            spaces_each = total_spaces // gaps

            # Extra spaces go to the leftmost gaps
            extra_spaces = total_spaces % gaps

            line = ""

            for j in range(gaps):
                line += line_words[j]
                line += " " * (spaces_each + (1 if j < extra_spaces else 0))

            line += line_words[-1]

            result.append(line)

        return result
