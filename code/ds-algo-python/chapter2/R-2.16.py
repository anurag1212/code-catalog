"""
max(0, (stop − start + step − 1) // step)

(stop - start)/step + (step - 1)/step
This is because floor is calculated in // so if a
number is not divisible by step, the extra %step
value is shaved off, and since range is end-exclusive,
it results in the last value being cut off. Thus, we
add step-1 to ensure a value above the last needed value
is cut off. Adding just step would work except in cases
where %step is 0.
"""
