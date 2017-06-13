# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
#
#
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
#
#
# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found a number", num)


# def fib(n):  # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#
# fib(2000)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# orice = [4, 5, 5, 3]







def rem_dupl(orice):
    new = []
    new = [n for n in orice if n not in new]
    # for n in orice:
    #     if n not in new:
    #         new.append(n)

    return new

# print(rem_dupl(orice))


# class Car(object):
#     condition = "new"
#
#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg = mpg
#
#     def display_car(self):
#         return "This is a {} {} with {} MPG.".format(self.color, self.model, self.mpg)
#
#     def drive_car(self):
#         self.condition = "used"
#         return self.condition
# c = Car("a", "b" , "c")
# print(c.drive_car())
#
#
#
# print(Car.condition)

