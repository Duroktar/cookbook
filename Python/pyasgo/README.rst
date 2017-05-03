pyingo
======

I suck at the learning so I'm gonna try to put some python code next
to the go *equivilant* or as close as possible.


Index
-----

* Imports_
* Variables_
* Functions_
* Classes_
* Collections_
* Iteration_
* Loops_
* Recursion_
* `Common patterns`_
* `Standard Library`_
* Sources_


Imports
-------

**Single import**

* **Go**

.. code-block:: go

    import "time"

* **Python**

.. code-block:: python

    import time


**Multiple import**

* **Go**

.. code-block:: go

    import (
        "time"
        "string"
    )

* **Python**

.. code-block:: python

    import time
    import string


**Import by url**

* **Go**

.. code-block:: go
    
    import (
        "github.com/jmcvetta/neo4j"
    )


Variables
---------

* **Go**

.. code-block:: go

    x := 3


* **Python**

.. code-block:: python

    x = 3


Functions
---------

* **Go**

.. code-block:: go

    import "time"

    func greeting() string {
        return "Hello world, the time is: " + time.Now().String()
    }


* **Python**

.. code-block:: python

    import time

    def greeting():
        return "Hello world, the time is: " + str(time.now())


Classes
-------

NOTE: Go does not have a "Class" type, however a "struct" is similar

**Creation and Initialization**

* **Go**

.. code-block:: go

    package main


    type User struct {
        FirstName   string
        LastName    string
    }

    func main() {
        a := User{FirstName: "Oderus", LastName: "Urungus"}
        b := User{"Oderus", "Urungus"}
    }


* **Python**

.. code-block:: python

    class User:
        def __init__(self, first, last):
            self.first_name = first
            self.last_name = last

    if __name__ == '__main__':
        a = User(first="Oderus", last="Urungus")
        b = User("Oderus", "Urungus")


**Methods**

* **Go**

.. code-block:: go

    package main

    import "fmt"


    type User struct {
        FirstName   string
        LastName    string
    }

    func (user User) Introduce() {
        fmt.Printf("Hello, my name is %s %s", user.FirstName, user.LastName)
    }

    func main() {
        user := User{FirstName: "Oderus", LastName: "Urungus"}
        user.Introduce()
    }


* **Python**

.. code-block:: python

    class User:
        def __init__(self, first, last):
            self.first_name = first
            self.last_name = last

        def introduce(self):
            print("Hello, my name is %s %s" % (self.first_name, self.last_name))


    if __name__ == '__main__':
        user = User("Oderus", "Urungus")
        user.introduce()


Collections
-----------

**dict** is like a **map**

`Maps are not safe for concurrent use`__

__ http://golang.org/doc/faq#atomic_maps/

* **Go**

.. code-block:: go

    map[KeyType]ValueType       // go map type

    m = make(map[string]int)    // m is a map of string keys to int values
    // or
    m = map[string]int{}        // shortcut, see the "{}" at the end
    m["route"] = 666

    i := m["route"]

    j := m["root"]          // returns 0 if key doesn't exist.
    // j == 0
    
    i, ok := m["route"]     // ok is true if key exists
    _, ok := m["route"]     // test for key, ignore value

    for key, value := range m {
        fmt.Println("- Key:", key, "- Value:", value)
    }

    delete(m, "route")

    data := map[string]int {    // initialize a map with data
        "rsc":  3711,
        "r":    2138,
        "gri":  1908,
        "adg":  912,
    }

* **Python**

.. code-block:: python

    data = {            # initialize a dict with data
        "rsc":  3711,
        "r":    2138,
        "gri":  1908,
        "adg":  912,
    }

**Array**

* The type [n]T is an array of n values of type T.

.. code-block:: go

    // base
    var a [10]int       // a is an array of 10 ints

    var b [2]string     // b is an array of 2 strings
    b[0] = "Hello"
    b[1] = "world"

    // or
    strings := [2]string{"Hello", "world"}

    // another example
    primes := [6]int{2, 3, 5, 7, 11, 13}

    // array of 10 integers set to 0
    empty_data := [10]int{}

**slice**

* The type []T is a slice with elements of type T.

.. code-block:: go

    // array of integers 1 - 10
    a := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}    // a = array of 10 ints

    // python-like
    fmt.Println(a)          // prints -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fmt.Println(a[:3])      // prints -> [1, 2, 3]
    fmt.Println(a[3:6])     // prints -> [4, 5, 6] etc..

    // Copy
    b = make([]T, len(a))
    copy(b, a)  // or b = append([]T(nil), a...)

    // Cut
    a = append(a[:i], a[j:]...)

    // Delete (Preserve order)
    a = append(a[:i], a[i+1:]...)  // or a = a[:i+copy(a[i:], a[i+1:])]

    // Delete (Doesn't preserve order)
    a[i], a = a[len(a)-1], a[:len(a)-a]

    // Pop
    x, a = a[len(a)-1, a[:len(a)-1]

    // Push
    a = append(a, x)


Iteration
---------

Iterate/enumerate over a list/array


**Go**

.. code-block:: go

    package main

    import (
        "fmt"
    )

    func main() {
        strings := [4]string{
            "Hey",
            "Ho",
            "Let's",
            "Go",
        }

        for index, value := range strings {
            fmt.Printf("%s - %s", index, value)
        }
    }


**Python**

.. code-block:: python

    strings = [
        "Hey",
        "Ho",
        "Let's",
        "Go",
    ]

    if __name__ == '__main__':
        for index, value in enumerate(strings):
            print("%s - %s" % (index, value))

Loops
-----

**Go only has for loops**

* **Go**

.. code-block:: go

    import (
            "fmt"
    )

    func fib(n int) int {
        a, b := 0, 1
        for i := 0; i < n; i++ {
            a, b = b, a+b
        }
        return b
    }

    func main() {
        for i := 0; i < 10; i++ {
            fmt.Println(fib(i))
        }
    }


* **Python**

.. code-block:: python

    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b

    for x in range(10):
        print(fib(x))


Recursion
---------

* **Python**

.. code-block:: python

    def fib_rec(n):
        if n <= 1:
            return 1
        else:
            return fib_rec(n-1) + fib_rec(n-2)

    for x in range(10):
        print(fib_rec(x))


* **Go**

.. code-block:: go

    import (
            "fmt"
    )

    func fibRec(n int) int {
        if n <= 1 {
            return 1
        }
        return fibRec(n-1) + fibRec(n-2)
    }

    func main() {
        for i := 0; i < 10; i++ {
            fmt.Println(fibRec(i))
        }
    }

Common patterns
---------------

Get the directory of the currently running script


**Go**

.. code-block:: go

    package main

    import (
        "fmt"
        "os"
        "path"
    )

    ex, err := os.Executable()
    if err != nil {
        panic(err)
    }

    script_dir := path.Dir(ex)
    fmt.Println(script_dir)

**Python**

.. code-block:: python
    
    import os.path

    script_dir = os.path.abspath(os.path.dirpath(__file__))
    print(script_dir)



Concurrency
-----------

* **Python**

.. code-block:: python

    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
            yield a

    if __name__ == '__main__':
        for x in fib(10):
            print(x)
        print('done')


* **Go**

.. code-block:: go

    func fib(c chan int, n int) {
        a, b := 0, 1
        for i := 0; i < n; i++ {
            a, b = b, a+b
            c <- a
        }
        close(c)
    }
    func main() {
        c := make(chan int)
        go fib(c, 10)

        for x := range c {
            fmt.Println(x)
        }
    }

*"Generator Style"*

.. code-block:: go

    func fib(n int) chan int {
        c := make(chan int)
        go func() {
            a, b := 0, 1
            for i := 0; i < n; i++ {
                a, b = b, a+b
                c <- a
            }
            close(c)
        }()
        return c
    }

    func main() {
        for x := range fib(10) {
            fmt.Println(x)
        }
    }


Standard Library
================

* os.getenv
* os.path_
* os.path.join_
* os.path.abspath_


os.path
-------

**Go**

.. code-block:: go

    import "path/filepath"

**Python**

.. code-block:: python

    import os.path


os.path.join
------------

**Go**

.. code-block:: go

    import "path/filepath"

    filepath.join("a", "b", "c")


**Python**

.. code-block:: python

    import os.path

    os.path.join("a", "b", "c")


os.path.abspath
---------------

**Go**

.. code-block:: go

    import "path/filepath"

    a := filepath.Abs("Movies")

**Python**

.. code-block:: python

    import os.path

    a = os.path.abspath("Movies")

os.getenv
---------

**Go**

.. code-block:: go

    package main

    import (
        "fmt"
        "os"
    )

    func main() {
        key := "USER"
        val, ok := os.LookupEnv(key)
        if !ok {
            fmt.Printf("%s not set\n", key)
        } else {
            fmt.Printf("%s=%s\n", key, val)
        }
    }

**Python**

.. code-block:: python

    import os.path

    if __name__ == '__main__':
        target = "USER"
        val = os.getenv(target)
        if not val:
            print("%s not set" % target)
        else:
            print("%s=%s" % (target, val))



Sources
-------

* https://talks.golang.org/2013/go4python

