# Proggramming Principles

_Because they pertain to clean code, these three concepts are ones that every developer should be concerned with._

### DRY Principle

_The DRY principle or “Don’t Repeat” makes sure that changing one component of a system does not need changing other,
conceptually
unrelated components. Therefore, it is a successful method of simplifying the development process. Additionally,
logically connected items change predictably and consistently, keeping them in sync._

_It indicates that it involves more than just pasting code, albeit that is still a part of it. It also involves using
various pieces of identical code. Even while it's possible to have separate code in many locations that all do the same
function differently, this is something that should be avoided._

+ Example:

```python
print('******************************')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('Hello')
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print('******************************')
```

_To solve this problem me can use decorators_

+ Example:

```python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
```

### KISS Principle

_The keep it simple, stupid rule states that simplicity is the key to developing a successful product.
The KISS approach is applicable to the design and creation of digital goods, but it's also commonly employed
in other professions like management or engineering._

_Sometimes you may just use the features of the programming language you are using instead of implementing
anything new to meet your needs._

_Keep It Short and Simple, Keep It Sweet, and Keep It Straightforward are other abbreviations for KISS.
All of these versions, nevertheless, pertain to the same strategy._

+ Example:

```python
😖
f = lambda x: 2 if x >= 2 else x / f(x - 2)
```

_Now look at this version:_

+ Example:

```python
 🤩

def exemple(number: int) -> int:
    if number >= 2:
        return 1
    else:
        return number / exemple(number - 2)
```

### YAGNI Principle

_Extreme programming is where you aren't going to need it (YAGNI) philosophy originated. It calls on programmers
to create features only when they are genuinely required, not when they anticipate or presume that something could be
helpful in the future._

_As both of them strive for a simpler answer, this approach is comparable to the KISS principle.
The distinction between both is that YAGNI concentrates on eliminating pointless logic and functionality,
whereas KISS concentrates on complexity._

_It means that functionality should only be implemented when you actually need it, not simply because you believe you
might need it in the future._