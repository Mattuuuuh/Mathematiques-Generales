\begin{verbatim}
num = 1000
for i in range(1,1001):
    if i%8 == 0 or i%12 == 0 or i%15 == 0:
        num -= 1
print(num)
>>> 783
\end{verbatim}
