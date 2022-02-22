a = 20.94
p = 4.53
w = 0.5
k = a * p ** 0.37 * w ** 0.18
f_y = 47.8
t_cp = 100
t_w = -9.5
q_t = 163914
q = (f_y * k * (t_cp - t_w) - q_t) * 100 / q_t
count = 1
while q < 10:
    w += 0.0000001
    k = a * p ** 0.37 * w ** 0.18
    q = (f_y * k * (t_cp - t_w) - q_t) * 100 / q_t
w -= 0.0000001
k = a * p ** 0.37 * w ** 0.18
q = (f_y * k * (t_cp - t_w) - q_t) * 100 / q_t
print(w,q)

