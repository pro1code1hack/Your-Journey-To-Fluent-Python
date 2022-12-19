# Design Principles

### Use refactor

_Once you have a better understanding of the issue and the trade-offs in the design, you may refactor the code to make
it more manageable. Your safety net—version control, tests, and linting—enables you to make changes with assurance._

### "Wide" is preferred above "Deep"

_Software components should be reusable in ways that the original author did not intend. In other words, expanding
beyond the initial use case should allow for unexpected functionality without significantly increasing complexity._

_Spend some time learning how things must operate at the base. Instead of deploying a weak, limited solution fast,
it is preferable to do it gradually._

### It's a Good Idea to Duck Type

_Duck typing handles things according to their capabilities rather than their type.
"It must be a duck if it quacks and walks like a duck," the saying goes._

_Interfaces are used by Python in general and scientific Python in particular to enable interoperability and reuse.
For instance, despite the fact that pandas was invented much later than numpy.sum,
it is feasible to send a pandas DataFrame to that method ()._

### Being permissive isn't always practical.

_Extremely perplexing errors can result from too liberal programming. If you want a flexible user interface that
attempts to "do the right thing" by assuming what the user wants, divide it into two layers: a thin "friendly" layer
on top of a "cranky" layer that only accepts the necessary information and performs the task. The grumpy layer should
be simple to test and have restrictions on what it may accept and return. It is feasible to construct several friendly
layers with various viewpoints and defaults thanks to this layered approach._

_Make function parameters necessary when in doubt. Optional arguments can conceal significant decisions that the user
should be aware they are making and are more difficult to find._

### Create Informative Error Messages

_Be precise. Include the incorrect value's name, its flaws, and possibly a suggestion on how to repair them.
For instance, the code should specify what it was seeking for and where it looked if it cannot find the file it
requires._

### Write readable code

_Your code will likely be viewed many more times than it is created, unless you are developing a script that you intend
to erase tomorrow or next week. And frequently, the "temporary answer" of today becomes the crucial code of tomorrow.
Therefore, choose names that are evocative and consistent, and prioritize clarity above brevity._

### Always Conserve Complexity

_Complexity is strictly greater than the system that the code is modeling and is always conserved.
Complexity-hiding tactics frequently backfire on the user._