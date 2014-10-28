Title: Scala学习笔记
Date: 2014-10-28
Category: Scala
Tag: 函数式编程, Scala
#Functional Programming Principles in Scala

##Programming Paradigms(编程范式)

Paradigm: In science, a *paradigm* describes distinct concepts or thought patterns in some scientific discipline.

Main programming paradigms:

 - imperative programming(命令式编程)
 - functional programming
 - logic programming

	
Orthogonal to it:

- object-oriented programming(面向对象的程序设计)

###Imperative programming

- modifying mutable(可变的) variables 
-  using assignments
-  and control structures such as if-then-else, loops, break,
continue, return.

The most common informal way to understand imperative programs is as instruction sequences for a Von Neumann(冯诺依曼) computer.

There’s a strong correspondence between

	Mutable variables  ≈ memory cells
	Variable dereferences ≈ load instructions
	Variable assignments ≈ store instructions
	Control structures ≈ jumps

Bottleneck(瓶颈): One tends to conceptualize data structures word-by-word.

##Functional Programming

- In a restricted sense, functional programming (FP) means
programming without mutable variables, assignments, loops,
and other imperative control structures.
- In a wider sense, a functional programming language enables
the construction of elegant programs that focus on functions.
- In particular, functions in a FP language are first-class citizens.
This means
	- they can be defined anywhere, including inside other functions
	- like any other value, they can be passed as parameters to functions and returned as results
	- as for other values, there exists a set operators to compose
	functions

#Elements of Programming

- Call-by-value has the advantage that it evaluates every function argument only once.  **(x: Int)**

		sumOfSquares(3, 2+2)
		sumOfSquares(3, 4)
		square(3) + square(4)
		3 * 3 + square(4)
		9 + square(4)
		9 + 4 * 4
	
- Call-by-name has the advantage that a function argument is not evaluated if the corresponding parameter is unused in the evaluation of the function body. **(y: => Double)**

		sumOfSquares(3, 2+2)
		square(3) + square(2+2)
		3 * 3 + square(2+2)
		9 + square(2+2)
		9 + (2+2) * (2+2)
		9 + 4 * (2+2)
		9 + 4 * 4

semicolons #分号

#Tail Recursion

Implementation Consideration: If a function calls itself as its last
action, the function’s stack frame can be reused. This is called ***tail recursion.***
⇒ Tail recursive functions are iterative processes.
In general, if the last action of a function consists of calling a function (which may be the same), one stack frame would be
sufficient for both functions. Such calls are called tail-calls.

尾调用的重要性在于它可以不在调用栈上面添加一个新的堆栈帧——而是更新它，如同迭代一般。尾递归因而具有两个特征：

- 调用自身函数(Self-called)；
- 计算仅占用常量栈空间(Stack Space)。

而形式上只要是最后一个return语句返回的是一个完整函数，它就是尾递归。

#Higher-Order Functions

Functions that take other functions as parameters or that return
functions as results are called ***higher order functions***.

##Summing with Higher-Order Functions

The type A => B is the type of a function that takes an argument of type A and returns a result of type B .

So, Int => Int is the type of functions that map integers to integers.

```scala
//Let’s define:
def sum(f: Int => Int, a: Int, b: Int): Int =
	if (a > b) 0
	else f(a) + sum(f, a + 1, b)
//We can then write:
def sumInts(a: Int, b: Int) = sum(id, a, b)
def sumCubes(a: Int, b: Int) = sum(cube, a, b)
def sumFactorials(a: Int, b: Int) = sum(fact, a, b)
//where
def id(x: Int): Int = x
def cube(x: Int): Int = x * x * x
def fact(x: Int): Int = if (x == 0) 1 else fact(x - 1)
```

##Anonymous Functions

***Anonymous Function***: a function without giving it a name.

```scala
def sumInts(a: Int, b: Int) = sum(x => x, a, b)
def sumCubes(a: Int, b: Int) = sum(x => x * x * x, a, b)
```

#Currying(柯里化)

把接受多个参数的函数变换成接受一个单一参数（最初函数的第一个参数）的函数，并且返回接受余下的参数而且返回结果的新函数的技术。

##Functions Returning Functions

```scala
def sum(f: Int => Int): (Int, Int) => Int = {
	def sumF(a: Int, b: Int): Int =
		if (a > b) 0
		else f(a) + sumF(a + 1, b)
	sumF //返回值
}
```
**sum is now a function that returns another function.**

	sum (cube) (1, 10)
	
- sum(cube) applies sum to cube and returns the sum of cubes
function.
- sum(cube) is therefore equivalent to sumCubes .
- This function is next applied to the arguments (1, 10) .

Generally, function application associates to the left:
	
	sum(cube)(1, 10) == (sum (cube)) (1, 10)

	def f ( args 1 )...( args n − 1 )( args n ) = E

is shown to be equivalent to

	def f = ( args 1 ⇒ ( args 2 ⇒ ...( args n ⇒ E )...))

#Functions and Data

##Classes

In Scala, we do this by defining a class:

```scala
class Rational(x: Int, y: Int) {
	def numer = x
	def denom = y
}
```
This definition introduces two entities:

- A new type, named Rational (有理数).
- A constructor Rational to create elements of this type.

Scala keeps the names of types and values in different namespaces. So there’s no conflict between the two defintions of Rational .

##Objects

We call the elements of a class type objects.

We create an object by prefixing an application of the constructor of the class with the operator new .

*Example*

	new Rational(1, 2)

##Members of an Object

Objects of the class Rational have two members, numer and denom .
We select the members of an object with the infix operator ‘.’ (like in Java).

**Example**
```scala
val x = new Rational(1, 2)   > x: Rational = Rational@2abe0e27
x.numer                      > 1
x.denom                      > 2
```

#Evaluation and Operators

 **1.Any method with a parameter can be used like an infix operator.**

It is therefore possible to write

	r add s                                             r.add(s)
	r less s           /* in place of */          r.less(s)
	r max s                                             r.max(s)

**2.Operators can be used as identifiers.**

*于是就可以方便的重载运算符了*

#Class Hierarchies(类层次)

##Abstract Classes

Consider the task of writing a class for sets of integers with the
following operations.
```scala
abstract class IntSet {
	def incl(x: Int): IntSet
	def contains(x: Int): Boolean
}
```
IntSet is an ***abstract class***.

Abstract classes can contain members which are missing an implementation (in our case, incl and contains ).

Consequently, no instances of an abstract class can be created with the operator *new* .

Let’s consider implementing sets as binary trees.
There are two types of possible trees: a tree for the empty set, and a tree consisting of an integer and two sub-trees.
Here are their implementations:
```scala
//这是可持久化的二叉搜索树
//IntSet is called the superclass of Empty and NonEmpty .(C中的基类)
//Empty and NonEmpty are subclasses of IntSet .
class Empty extends IntSet {
	def contains(x: Int): Boolean = false
	def incl(x: Int): IntSet = new NonEmpty(x, new Empty, new Empty)
}

class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet {
	def contains(x: Int): Boolean =
		if (x < elem) left contains x
		else if (x > elem) right contains x
		else true
	def incl(x: Int): IntSet =
		if (x < elem) new NonEmpty(elem, left incl x, right)
		else if (x > elem) new NonEmpty(elem, left, right incl x)
		else this
}
```

##Implementation and Overriding

The definitions of contains and incl in the classes Empty and NonEmpty implement the abstract functions in the base trait IntSet .
It is also possible to redefine an existing, non-abstract definition in a
subclass by using override .
```scala
abstract class Base {
	def foo = 1
	def bar: Int
}
class Sub extends Base {
	override def foo = 2
	def bar = 3
}
```

##Programs

Create standalone applications in Scala.
Each such application contains an object with a **main method**.
For instance, here is the “Hello World!” program in Scala.
```scala
object Hello {
	def main(args: Array[String]) = println(”hello world!”)
}
```

##Traits

In Java, as well as in Scala, a class can only have one superclass.
But what if a class has several natural supertypes to which it conforms or from which it wants to inherit code?
Here, you could use ***traits***.
A trait is declared like an abstract class, just with trait instead of abstract class .

```scala
trait Planar {
	def height: Int
	def width: Int
	def surface = height * width
}

class Square extends Shape with Planar with Movable ...
```

#Polymorphism(多态)

##Value Parameters

```
package week4
trait IntList ...
class Cons(val head: Int, val tail: IntList) extends IntList ...
class Nil extends IntList ...
```

A list is eithter

- an empty list new Nil
- a list new Cons(x, xs) consisting of a head element x and a tail list xs.

Note the abbreviation **(val head: Int, val tail: IntList)** in the defitions of Cons.

This defines at the same time parameters and fields of a class.

It is equivalent to:

```scala
class Cons(_head: Int, _tail: IntList) extends IntList {
	val head = _head
	val tail = _tail
}
```

##Type Parameters

类似于template吧
```scala
trait List[T] {
	def isEmpty: Boolean
	def head: T
	def tail: List[T]
class Cons[T](val head: T, val tail: List[T]) extends List[T] {
	def isEmpty = false
}
class Nil[T] extends List[T] {
	def isEmpty = true
	def head = throw new NoSuchElementException("Nil.head")
	def tail = throw new NoSuchElementException("Nil.tail")
}
```
We can then write:

```scala
singleton[Int](1)
singleton[Boolean](true)
```
scala 编译器可以自动判断类型,所以可以简写成

```scala
singleton(1)
singleton(true)
```

##polymorphism

ploymorphism means that a function type comes "in many forms"
In programming it means that

- the function can be applied to arguments of many types
- the type can have instances of many types


> Written with [StackEdit](https://stackedit.io/).
