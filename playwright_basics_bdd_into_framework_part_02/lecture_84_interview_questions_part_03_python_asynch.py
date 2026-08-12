# =============== Question 01 ========================
"""
        Is python synchronous or asynchronous ?

ANSWER:
        Both java and python are by default synchronous which means, they run the code in a
        sequential manner. One by one in ascending order the code is executed. I mean one line,
        then the next line, then the next line, this is how python codes are executed. However,
        by explicitly, we can make java and python asynchronous. That means codes will be executed
        randomly but based on also logic.

        But Javascript is asynchronous as we know, when we load a website, sometimes header becomes
        visible first or sometimes footer or other content. That's because of javascript

        REMEMBER: when we want anything asynchronous, we always use "async" keyword in python before any
        steps or methods or functions and also need to call the "main" function in async mode.



"""
import asyncio
import time


def simple_regular_default_code_of_synchronous(name1, name2):
    print(f"First Name {name1} comes first")
    # this means stop entire thread for 1.5 seconds then continue
    time.sleep(1.5)
    print(f"Last name {name2} comes last")


async def it_is_an_async_code(name1, name2):
    print(f"First Name {name1} comes first")
    # this means "I need to wait 1.5 seconds. While I'm waiting, let another coroutine run."
    await asyncio.sleep(1.5)
    print(f"Last name {name2} comes last")


async def main():
    await asyncio.gather(it_is_an_async_code("Musarrat", "Jahan"),
                         it_is_an_async_code("Utsob", "Akter"))

asyncio.run(main())
