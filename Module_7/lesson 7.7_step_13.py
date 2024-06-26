from abc import ABC, abstractmethod
from textwrap import wrap


class Paragraph(ABC):
    def __init__(self, length: int) -> None:
        self.length = length
        self._text = ""

    def add(self, text: str):
        self._text += text + " "

    @abstractmethod
    def end(self):
        self._text = ""


class LeftParagraph(Paragraph):
    def end(self):
        print(*[text for text in wrap(self._text, width=self.length)], sep="\n")
        super().end()


class RightParagraph(Paragraph):
    def end(self):
        for text in wrap(self._text, width=self.length):
            print(text.rjust(self.length))
        super().end()


# INPUT DATA:

# TEST_1:
leftparagraph = LeftParagraph(10)

leftparagraph.add("death")
leftparagraph.add("can have me")
leftparagraph.add("when it earns me")
leftparagraph.end()

# TEST_2:
rightparagraph = RightParagraph(10)

rightparagraph.add("death")
rightparagraph.add("can have me")
rightparagraph.add("when it earns me")
rightparagraph.end()

# TEST_3:
leftparagraph = LeftParagraph(23)

leftparagraph.add("Multiply noise and joy")
leftparagraph.add("Sing songs in a good hour")
leftparagraph.add("Friendship grace and youth")
leftparagraph.add("Our birthday girls")
leftparagraph.end()

leftparagraph.add("Meanwhile the winged child")
leftparagraph.add("friends greeting you")
leftparagraph.add("Secretly thinks sometime")
leftparagraph.add("I will be the birthday boy")
leftparagraph.end()

# TEST_4:
rightparagraph = RightParagraph(28)

rightparagraph.add("I will not regret the roses")
rightparagraph.add("Withered with a light spring")
rightparagraph.add("I love the grapes on the vines")
rightparagraph.add("Ripened in the hands under the mountain")
rightparagraph.end()

rightparagraph.add("The beauty of my green valley")
rightparagraph.add("Golden joy of autumn")
rightparagraph.add("oblong and transparent")
rightparagraph.add("Like the fingers of a young maiden")
rightparagraph.end()
