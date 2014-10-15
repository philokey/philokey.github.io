Title: C++中的类
Date: 2014-10-15
Category: C++
Tag: class, C++

##公有继承

通过 is-a 的方式进行继承

 - 基类先被创建
 - 派生类通过成员初始化列表将基类信息传递给基类构造hanshu
 - 如果省略成员初始化列表,基类将使用默认构造函数
 - 派生类过期时,先调用派生类的析构函数

###基类和派生类的特殊关系
```
class A {
private:
    string name;
public:
    void print() {
        printf("A\n");
    }
    A(string st) {
        name = st;
    }
};
class B: public A {
public:
    B(string st):A(st){}
};
```
基类指针可以再不进行显示类型转换的情况下指向派生类的对象; 基类引用可以再不进行显式类型转换的情况下引用派生类对象
```
B tp("abc");
A &rt = tp; //right
A *pt = &tp; //right
```
不能将基类对象和地址赋给派生类引用和指针
```
A tp("abc");
B &rr = tp; //wrong
B *pr = &tp;//wrong
```

以上两条符合"类型从高到底可以自动转换"

###多态公有继承

当一个方法在基类和派生类中的行为不同时，重新修改基类中的那个方法，使之具有多态。一般有两种机制用于实现多态公有继承：

 1. 在派生类中重新定义基类的方法
 2. 使用虚函数（虚方法）

如果方法是通过引用或指针而不是对象调用的，如果没有采用虚函数方法，则程序根据引用类型或指针类型选择方法，如果采用虚函数了，则程序根据引用或者指针指向的对象的类型来选择方法。

```
//behavior with non-virtual VieAcct()
//method chosen according to reference type
Brass dom();
BrassPlus dot();
Brass &b1_ref = dom;
Brass &b2_ref = dot;
b1_ref.VeiAcct(); //use Brass::VieAcct()
b2_ref.VeiAcct(); //use Brass::VieAcct()
```

```
//behavior with virtual VieAcct()
//method chosen according to object type
Brass dom();
BrassPlus dot();
Brass &b1_ref = dom;
Brass &b2_ref = dot;
b1_ref.VeiAcct(); //use Brass::VieAcct()
b2_ref.VeiAcct(); //use BrassPluss::VieAcct()
```

析构函数应该是虚拟的

###静态联编和动态联编：

联编：将源代码中函数调用解释为执行特定的函数代码成为函数名联编。C/C++在编译过程中进行的联编称之为静态联编，又称为早期联编；在程序运行过程中联编称之为动态联编，也称为晚期联编。编译器对非虚拟方法使用静态联编，对虚拟方法使用动态联编。

###虚函数的工作机制

C++规定了虚函数的行为，但将实现方法留给了编译器作者。不需要知道实现方法就可以使用虚函数，但是了解虚函数的工作原理有助于更好的理解虚函数：

通常，编译器处理虚函数的方法是：给每个类对象添加一个隐藏成员。隐藏成员中保存了一个指向函数地址数组的指针。这种数组称为虚函数表(virtual function table,vtbl)。虚函数表中存储了为类对象进行声明的虚函数的地址。例如，基类对象包含一个指针，该指针指向基类中所有虚函数的地址表。派生类

将包含一个指向对立地址表的指针。如果派生类提供了虚函数的新定义，该虚函数表将保存新函数的地址，如果派生类没有重新定义虚函数，则该vtbl将保存

函数原始版本的地址。如果派生类定义了 新的虚函数，则该函数的地址也将被添加到vtbl中。但是注意，无论类中包含多少个虚函数，都只需要在对象中添加1个地址成员表，只是表的大小不一样。

###虚函数的注意事项
- 在基类方法的声明中使用关键字virtual可使该方法在基类以及所有的派生类（包括从派生类的派生出来的派生类）中是虚拟的，因为方法在基类中被声明为虚拟的后，它在派生类中自动默认为虚拟的。

- 如果使用指向对象的引用或指针来调用虚方法，程序将使用为对象类型定义的方法，而不使用为引用或指针类型定义的方法。这个就是动态联编（晚期）联编。这个行为非常重要，因为这样就可以使得基类指针或引用可以指向派生类对象

- 构造函数不能是虚函数，因为派生类不能继承构造函数，所以没有什么意义
 
- 构函数应当是虚函数，除非类不做基类。通常应该给基类提供一个虚析构函数，即使它不需要析构函数。

-  友元函数不能是虚函数，因为友元不是类成员，而只有类成员才能是虚函数。如果由于这个原因而导致了设计问题 ，可以通过友元函数使用虚函数来解决。

- 如果派生类没有重新定义函数，将使用该函数的基类版本。如果派生类位于派生类链中，则将使用最新的虚函数方法办法，如果基类是隐藏的除外。

- 重新定义隐藏方法

```
calss Dwelling {
public:
	virtual void showperks (int a) const;
...
};
class Houve: public Dwelling {
public:
	virtual void showperks()const;
...
}

Hovel trump;
trump.showperks(); //valid
trump.showperks(); //invalid
```

###Protected

protected和private 相似，在类外只能用公有类成员访问protected部分中的类成员. protected与private的区别只有在派生类中能体现出来, 派生类的成员可以直接访问protected保护成员.

###抽象基类

纯虚函数(pure virtual function)：在本类里不能有实现（描述功能），实现需要在子类中实现. 纯虚函数声明的结尾处为 = 0.
```
virtual double Area()const = 0; //a pure virtual function
```
抽象类：一个类可以抽象出不同的对象来表达一个抽象的概念和通用的接口，这个类不能实例化(创造)对象。有纯虚函数的类是抽象类.



