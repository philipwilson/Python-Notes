## Introduction to Programming in Python

####  Drawing heavily on:

* Guttag, *Introduction to Computation and Programming Using Python*, Second Edition, ISBN 978-0-262-52962-4
* [MIT OpenCourseware 6.0001 (Fall 2016)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)
* [SICP in Python](http://www-inst.eecs.berkeley.edu/~cs61a/sp12/book/) - Translation to Python of Ableson & Sussman's classic *Structure and Interpretation of Computer Programs*


## Section 1:  Building Abstractions with Functions

### Lecture 1:  Introduction
* [Course Overview]()
* [What is computation?]()

* [Introduction to Python]()
  * [Installing Python 3]()
  * [Interactive Sessions and REPL]()
  * [First Example]()
  * [Practical Guidance:  Errors]()
  * [Editing and Running Program Files]()

* [Elements of Programming]()
  * [Primitive Expressions and Statements]()
  * [Means of Combination - Compound elements built from simpler ones]()
  * [Means of Abstraction - Compound elements named and manipulated as units]()

* [Expressions]()
  * [Scalar types]()
  * [type(), Type conversions]()
  * [Operators]()
  * [printing]()

### Lecture 2:  Expressions in more detail

* [Names and the Environment]()
* [Call Expressions]()
* [Importing Library Functions]()
* [Quick Look at Python Standard Library](https://docs.python.org/3/library/index.html)
* [Evaluating Nested Expressions]()
* [Floating Point Values]()
* [Some Simple Numerical Programs]()
* [Newton's Method]()
* [Function Diagrams]()

### Lecture 3: Defining new Functions

* [Defining New Functions]()
* [Environments]()
* [Calling User-Defined Functions]()
* [Local Names and Scoping]()
* [Practical Guidance:  Choosing Names]()
* [The Art of Functions]()
* [Docstrings]()
* [Default Argument Values]()

* [Control]()
  * [Statements]()
  * [Compound Statements]()
  * [Defining Functions II: Local Assignment]()
  * [Conditional Statements]()
    * [Boolean Context, Boolean Values, Intro Boolean Algebra]()
  * [Iteration]()
  * [Practical Guidance: Testing]()

* [Specifation and Testing]()

### Lecture 4: Higher-Order Functions

* [Higher-Order Functions]()
  * [Functions as Arguments]()
  * [Functions as General Methods]()
  * [Defining Functions III: Nested Definitions]()
  * [Functions as Returned Values]()
  * [Lambda Expressions]()
  * [Example: Newton's Method]()
  * [Abstractions and First-Class Functions]()
  * [Function Decorators]()

## Section 2:  Building Abstractions with Objects (SICP 'objects', Guttag Chapter 8)

### Lecture 5:

* [Introduction]()
  * [The Object Metaphor]()
  * [Native Data Types]()
* [Data Abstraction]()
  * [Example: Arithmetic on Rational Numbers]()
    * [Tuples]()
    * [Abstraction Barriers]()
    * [The Properties of Data]()
* [Sequences]()
  * [Nested Pairs]()
  * [Recursive Lists]()
  * [Tuples II]()
  * [Sequence Iteration]()
  * [Sequence Abstraction]()
  * [Strings]()
  * [Conventional Interfaces]()

### Lecture 6:  Mutable Data, Some Python Collections
* [Mutable Data]()
  * [Local State]()
  * [The Benefits of Non-Local Assignment]()
  * [The Cost of Non-Local Assignment]()
  * [Lists]()
  * [Dictionaries]()
  * [Example: Propagating Constraints]()

### Lecture 7:  Introduction to Object Oriented Programming
* [Object-Oriented Programming]()
  * [Objects and Classes]()
  * [Defining Classes]()
  * [Message Passing and Dot Expressions]()
  * [Class Attributes]()
  * [Inheritance]()
  * [Using Inheritance]()
  * [Multiple Inheritance]()
  * [The Role of Objects]()

### Lecture 8:  Implementing New Classes and Objects
* [Implementing Classes and Objects]()
  * [Instances]()
  * [Classes]()
  * [Using Implemented Objects]()
  
* [Generic Operations]()
  * [String Conversion]()
  * [Multiple Representations]()
  * [Generic Functions]()

## Section 3:  Structure and Interpretation of Computer Programs (SICP 'interpretation')

### Lecture 9:  Programming Languages I
* [Introduction]()
  * [Programming Languages]()
* [Functions and the Processes They Generate]()
  * [Recursive Functions]()
  * [The Anatomy of Recursive Functions]()
  * [Tree Recursion]()
  * [Example: Counting Change]()
  * [Orders of Growth]()
  * [Example: Exponentiation]()
  
* [Recursive Data Structures]()
  * [Processing Recursive Lists]()
  * [Hierarchical Structures]()
  * [Sets]()
* [Exceptions]()
  * [Exception Objects]()

### Lecture 10 and 11:  Programming Languages II
* [Interpreters for Languages with Combination]()
  * [Calculator]()
  * [Parsing]()
* [Interpreters for Languages with Abstraction]()
  * [The Scheme Language]()
  * [The Logo Language]()
  * [Structure]()
  * [Environments]()
  * [Data as Programs]()

## Section 4:  Distributed and Parallel Computing (SICP 'communication')

### Lecture 12:  Distributed Computing
* [Introduction]()
* [Distributed Computing]()
  * [Client/Server Systems]()
  * [Peer-to-peer Systems]()
  * [Modularity]()
  * [Message Passing]()
  * [Messages on the World Wide Web]()

### Lecture 13:  Parallel Computing 
* [Parallel Computing]()
  * [The Problem with Shared State]()
  * [Correctness in Parallel Computation]()
  * [Protecting Shared State: Locks and Semaphores]()
  * [Staying Synchronized: Condition variables]()
  * [Deadlock]()

## Section 5:  Sequences and Coroutines (SICP 'streams')

### Lecture 14: Sequences and Coroutines
* [Introduction]()
* [Implicit Sequences]()
  * [Python Iterators]()
  * [For Statements]()
  * [Generators and Yield Statements]()
  * [Iterables]()
  * [Streams]()
* [Coroutines]()
  * [Python Coroutines]()
  * [Produce, Filter, and Consume]()
  * [Multitasking]()

## Section 6:  Intro Algorithms and Data Structures


### Lecture 15: Introduction to Algorithmic Complexity (Guttag Chapter 9)
* [Thinking about Computational Complexity]()
* [Asymptotic Notation]()
* [Some Important Complexity Classes]()
  * [Constant]()
  * [Logarithmic]()
  * [Linear]()
  * [Log-Linear]()
  * [Polynomial]()
  * [Exponential]()

### Lecture 16: Some Fundamental Algorithms and Data Structures (Guttag Chapter 10)
* [Search Algorithms]()
* [Sorting Algorithms]()
* [Hash Tables]()
* [Trees]()

### Orphan Topics:

* [Modules]()
* [Files]()

* [Simple I/O]()
* [Python data model and special methods]()
* [pattern matching and regex]()

### Some Useful Links
* [Useful links](LINKS.md)



