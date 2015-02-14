import math

fn1 = 1
fn2 = 1
fn3 = 2
count = 3
dig = 1

while dig < 1000:
    fn1 = fn2
    fn2 = fn3
    fn3 = fn2+fn1
    count += 1
    dig = math.floor(math.log10(fn3))+1

print (count)
