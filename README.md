### Hexlet tests and linter status:

[![Actions Status](https://github.com/RustSaf/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/RustSaf/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/1b347846c0c66e6c280e/maintainability)](https://codeclimate.com/github/RustSaf/python-project-49/maintainability)


### Overview and Installation

This project includes the logical games united under a common name "Brain games".
These games are math exercises.

_Install the pip package using the command:_
```python
$ python3 -m pip install --user dist/*.whl
```

The package includes 6 games in total:
- "brain-even" is a parity game. Answer "yes" if the number is even, otherwise answer "no".
- "brain-calc" is addition, subtraction or multiplication exercise. You should find the result of the expression.
- "brain-gcd" is greatest common divisor exercise. Find the greatest common divisor of given numbers.
- "brain-progression" is math progression exercise. You should find what number is missing in the progression.
- "brain-prime" is exercise to find a prime number. Answer "yes" if given number is prime. Otherwise answer "no".
- "brain-game". This game is intended only for getting to know the player.



_To start the game, enter its name, for example:_
```
$ brain-even
```

_At the beginning, each game introduces itself to the player:_
```
Welcome to the Brain Games!
May I have your name? _You name_
Hello, _You name_!
```

_After the introduction the game displays the question, for example:_ 
```
Answer "yes" if the number is even, otherwise answer "no".
```

_After that series of three similar mathematical problems follows, for example:_
```
Question: 24
```

_You answer and press Enter, for example:_
```
Your answer: yes
```

_If the answer is correct, the game module displays a message:_ 
```
Correct!
```

_If all three answers are correct, the game will display a message:_ 
```
Congratulations, _Your name_!
```

_If one of the answers is incorrect, the game will display:_
```
_You answer_ is wrong answer ;(. Correct answer was _Correct answer_.
Let's try again, _Your name_!
```

This is where the game ends.


### Usage

Examples of usage "Brain Games" on ![asciinema.org](https://asciinema.org):

_Installation the pip package and launching the game brain-even_

[![asciicast1](https://asciinema.org/a/Nx40PPsyifkRWp5sE2kBeND0n.png)](https://asciinema.org/a/Nx40PPsyifkRWp5sE2kBeND0n)

_Launching the game brain-calc_

[![asciicast2](https://asciinema.org/a/PSwWy5V0hQnMPlVsoEHLsVcEE.png)](https://asciinema.org/a/PSwWy5V0hQnMPlVsoEHLsVcEE)

_Launching the game brain-gcd_

[![asciicast3](https://asciinema.org/a/LKTbMynzvh4EDh3r5hawnSt5g.png)](https://asciinema.org/a/LKTbMynzvh4EDh3r5hawnSt5g)

_Launching the game brain-progression_

[![asciicast4](https://asciinema.org/a/CKYT8VAvxaSclPRhqJ1gw35rd.png)](https://asciinema.org/a/CKYT8VAvxaSclPRhqJ1gw35rd)

_Launching the game brain-prime_

[![asciicast5](https://asciinema.org/a/5CXzVzHOEsIDQp2uSMOLRQV0x.png)](https://asciinema.org/a/5CXzVzHOEsIDQp2uSMOLRQV0x)

_Launching the game brain-game_
[![asciicast6](https://asciinema.org/a/JvOfrLlPtkpWo3GSbvRDswk4S.png)](https://asciinema.org/a/JvOfrLlPtkpWo3GSbvRDswk4S)


### Links

_This project was built using these tools_:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://python-poetry.org/)                                        | "Python dependency management and packaging made easy"  |
| [flake8](https://flake8.pycqa.org/)                                         | "Your tool for style guide enforcement"                 |

---
