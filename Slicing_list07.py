def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    if n>0:
      return  list1[0::n]
    if n<0:
       return list1[-1::n]

print(main([1,2,3,4,5,7],-1))