# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ctypes                                      # provides low-level arrays

class DynamicArray:
  """A dynamic array class akin to a simplified Python list."""

  def __init__(self):
    """Create an empty array."""
    self._n = 0                                    # count actual elements
    self._capacity = 1                             # default array capacity
    self._A = self._make_array(self._capacity)     # low-level array

  def __len__(self):
    """Return number of elements stored in the array."""
    return self._n

  def cap(self):
      """Returns the capacity of the dynamicArray"""
      return self._capacity

  def change_len(self, value):
      """ increases or decreases self._n by value"""
      try:
          intX=int(value)
      except ValueError:
            print("Your value has to be an integer")
      if intX<0:
          self._n-=abs(intX)
      else:
          self._n+= intX

  def __getitem__(self, k):
    """Return element at index k."""
    if (-self.cap())<k<0:
       return self._A[len(self)+k]
    elif 0 <= k <(self.cap()):
       return self._A[k]
    elif k<(-self.cap()) or k>self.cap():
        raise ValueError("invalid index")
    print("nothing went through")                         # retrieve from array


  def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    self._A[self._n] = obj
    self._n += 1

  def _resize(self, c):                            # nonpublic utitity
    """Resize internal array to capacity c."""
    B = self._make_array(c)                        # new (bigger) array
    for k in range(self._n):                       # for each existing value
      B[k] = self._A[k]
    self._A = B                                    # use the bigger array
    self._capacity = c

  def _make_array(self, c):                        # nonpublic utitity
     """Return new array with capacity c."""
     return (c * ctypes.py_object)()               # see ctypes documentation

  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    for j in range(self._n, k, -1):                # shift rightmost first
      self._A[j] = self._A[j-1]
    self._A[k] = value                             # store newest element
    self._n += 1

  def remove_1stvalue(self, value):
    """Remove first occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version
    for k in range(self._n):
      if self._A[k] == value:              # found a match!
        for j in range(k, self._n - 1):    # shift others to fill gap
          self._A[j] = self._A[j+1]
        self._A[self._n - 1] = None        # help garbage collection
        self._n -= 1                       # we have one less item
        return                             # exit immediately
    raise ValueError('value not found')    # only reached if no match

  def remove_index(self, index):
      """ removes the index item without shifting them in self._A and reduce self._n """
      if len(self)==0:
          raise Empty("No element in the list")
#      if index>len(self) and self._capacity > index:
#          B=self._make_array(len(self._A))
#          for i in range(len(self._A)):
#              B[i]=self._A[index+i]
#          self._A=B
#          self._A[0]=None
      else:
          self._A[index]=None
      self._n-= 1


  def insertEfficient(self,k,value):
      if self._n==self._capacity:
          B=self._make_array(2*self._capacity)
          for j in range(self._n+1):
              if j<k:
                  B[j]=self._A[j]
              if j==k:
                  B[j]=value
              if j>k:
                  B[j]=self._A[j-1]
          self._A=B
          self._n+=1
          self._capacity=2*self._capacity
      else:
          for i in range(self._n,k,-1):
              self._A[i]=self._A[i-1]
          self._A[k]=value
          self._n+=1

  def removeAll(self,value):
      loop_counter=0
      count=0
      while loop_counter<self._n:
         if self._A[loop_counter]==value:
            count+=1
         if count>0 and self._A[loop_counter]!=value:
            self._A[loop_counter-count]=self._A[loop_counter]
         if loop_counter>self._n-count:
            self._A[loop_counter]=None
         loop_counter+=1
      self._n-=count
      if count==0:
         raise ValueError('value not found')
