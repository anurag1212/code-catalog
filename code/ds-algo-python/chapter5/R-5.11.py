def sum_mat(m,i,n1,j,n2):
    if n1 is None or n2 is None:
        n1 = len(m)
        n2 = len(m[0])
    if n1==n2==1:
        return m[i][j]
    elif n1==1:
        return sum_mat(m,i,n1,j,n2//2) + sum_mat(m,i,n1,j+n2//2,n2-n2//2)
    else:
        return sum_mat(m,i,n1//2,j,n2) + sum_mat(m,i+n1//2,n1-n1//2,j,n2)

#TODO understand constraints properly
