# list operations


def append():
    # ['1', 'hello', '4.5', '0kh', '-0986']
    sample=[]
    print("type:",type(sample))
    n=int(input("enter the number of count to insert:"))
    for i in range(0,n):
        sample.append(input(f"enter the{i+1} value for list "))
    print("the final updated list",sample)

def extend():
    sample= ['1', 'hello', '4.5', '0kh', '-0986']
    sample.extend("extend")
    sample.append("hello")
    print("list after update :",sample)#both extend and add (+) does same but + need an new list here extend will append data in same list 


def insert():
    sample=[]
    print("emplty",sample)
    sample.insert(1,6)#insert element in exsting index it moves old element to next index and insert new element in required position 
    sample.insert(0,0)
    sample.insert(1,0)
    print(sample)

def pop():
       sample= ['1', 'hello', '4.5', '0kh', '-0986']
       sample.pop()
       sample.pop(-2)
       print(sample)#use index #or if index not specified then elete it from last


def remove():
     sample= ['1', 'hello', '4.5', '0kh', '-0986']
     sample.remove('1')#remove specific element 
     print(sample)


def reverse():
      sample= ['1', 'hello', '4.5', '0kh', '-0986']
      print(sample.reverse())
    #   print(sample.reverse())
      print(sample)

def length():
    #   sample= ['1', 'hello', '4.5', '0kh', '-0986']
    #   length=len(sample)
    #   print(length)
    sample = ['1', 'hello', '4.5', '0kh', '-0986']
    print(len(sample))
    # print("The length of the list is:", length)


def minimum():
      sample= ['1', 'hello', '4.5', '0kh', '-0986']
      print(min(sample))

def maximum():
      sample= ['1', 'hello', '4.5', '0kh', '-0986']
      print(max(sample))

def count():
      sample= ['1', 'hello', '4.5', '0kh', '-0986']
      print(sample.count('1'))

def find_index():
      
      sample= ['1', 'hello', '4.5', '0kh', '-0986']
      print(sample.index('1'))


def mul():
     sample=[100, 150, 200, 250, 300]
     cube=[]
     for ele in sample:
       print(ele)   
       new=ele**3
       cube.append(new)
     print(cube)


if __name__=='__main__':
    # minimum()
    # maximum()
    # count()
    # find_index()
    mul()