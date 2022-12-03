class Foo(object): __slots__ = ('foo',)
class Bar(object): pass

def get_set_delete(obj):
  obj.foo = 'foo'
  obj.foo
  del obj.foo
  
def test_foo():
  get_set_delete(Foo())
  
def test_bar():
  get_set_delete(Bar())
