Title: STL笔记
Date: 2014-08-10 18:12
Category: 笔记
Tags: C++,STL

##priority_queue自定义比较函数

模板声明带有三个参数
```
priority_queue<Type, Container, Functional>
```
Type 为数据类型， Container 为保存数据的容器，Functional 为元素比较方式。
Container 必须是用数组实现的容器，比如 vector, deque 但不能用 list.
STL里面默认用的是 vector. 比较方式默认用 operator< , 所以默认为小根堆。

```
#include < iostream >
#include < queue >
#include < functional >
 
using namespace std;
 
class cmp {
public:
    bool operator() (const int& a, const int& b) {
		return a > b;
	}
};
 
int main() {
	priority_queue< int, vector< int >, greater< int > > heap; //大根堆
	priority_queue< int, vector< int >, cmp> heap2; //自定义比较类
}
```


