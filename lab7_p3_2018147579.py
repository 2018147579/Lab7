
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
        
        ### YOUR CODE HERE ###
        
        # Check if arr is a 2D list
        if not all(isinstance(inner_list, list) for inner_list in arr):
            raise not2DError()

        # Check if all inner lists have the same length
        if len(set(len(inner_list) for inner_list in arr)) != 1:
            raise unevenListError()
        
        ######

        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###
        
        # Number of rows is the length of the list
        rows = len(self)
        # Number of columns is the length of the first inner list
        cols = len(self[0]) if rows > 0 else 0

        return f'list_2D: {rows}*{cols}'

        ######

    def transpose(self):

        ### YOUR CODE HERE ###

        # Transpose of the matrix
        return list_D2([list(row) for row in zip(*self)])
        
        ######


    def __matmul__(self, others):
        
        ### YOUR CODE HERE ###
        
        if len(self[0]) != len(others):
            raise improperMatrixError()

        # Matrix multiplication
        result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*others)] for row_a in self]
        return list_D2(result)

        ######

    def avg(self):

        ### YOUR CODE HERE ###
        
        total_elements = sum(len(row) for row in self)
        total_sum = sum(sum(row) for row in self)
        return total_sum / total_elements if total_elements else 0
    
        ######
