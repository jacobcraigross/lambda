# lambda (or anonymous) functions

In computer programming, an anonymous function (function literal, lambda abstraction) is a function definition that is not bound to an identifier. Anonymous functions are often:[1]

arguments being passed to higher-order functions, or
used for constructing the result of a higher-order function that needs to return a function.
If the function is only used once, or a limited number of times, an anonymous function may be syntactically lighter than using a named function. Anonymous functions are ubiquitous in functional programming languages and other languages with first-class functions, where they fulfill the same role for the function type as literals do for other data types.

Anonymous functions originate in the work of Alonzo Church in his invention of the lambda calculus in 1936, before electronic computers, in which all functions are anonymous.[2] In several programming languages, anonymous functions are introduced using the keyword lambda, and anonymous functions are often referred to as lambdas or lambda abstractions. Anonymous functions have been a feature of programming languages since Lisp in 1958, and a growing number of modern programming languages support anonymous functions.

Anonymous functions are a form of nested function, in allowing access to variables in the scope of the containing function (non-local variables). This means anonymous functions need to be implemented using closures. Unlike named nested functions, they cannot be recursive without the assistance of a fixpoint operator (also termed an anonymous fixpoint or anonymous recursion) or binding them to a name.[3]

