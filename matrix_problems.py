class Matrix:
    @staticmethod
    def mul_of_matrix(a,b):
        a_row=len(a)
        a_col=len(a[0])
        b_row=len(b)
        b_col=len(b[0])
        if a_col!=b_row:
            return False
        else:
            c=[]
            for i in range(a_row):
                row=[]
                for j in range(b_col):
                    row.append(0)
                c.append(row)
            for i in range(a_row):
                for j in range(b_col):
                    for k in range(a_col):
                        c[i][j]+=a[i][k]*b[k][j]
            return c
    @staticmethod
    def add_of_matrix(a,b):
        a_row=len(a)
        a_col=len(a[0])
        b_row=len(b)
        b_col=len(b[0])
        if a_row!=b_row or a_col!=b_col:
            return False
        c=[]
        for i in range(a_row):
            row=[]
            for j in range(a_col):
                row.append(a[i][j]+b[i][j])
            c.append(row)
        return c
a=[[1,2,3],
    [4,5,6]]
    
b=[[7,8],
    [9,10],
    [11,12]]       
obj=Matrix()
mul_res=obj.mul_of_matrix(a,b)
add_res=obj.add_of_matrix(a,b)
print(f"Multiplication result:-")
if mul_res:
    for r in mul_res:
        print(r)
else:
    print("Multiplication is not possible")
print(f"Addition result:-")
if add_res:
    for r in add_res:
        print(r)
else:
    print("Addition is not possible")
