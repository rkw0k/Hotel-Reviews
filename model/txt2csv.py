import sys

fn_old = "rating_count_location.txt"
fn_new = "rating_count,location.csv"
f_old = open(fn_old)
f_new = open(fn_new, 'w')
f_new.truncate()

text = f_old.read().replace("|", ",")
f_new.write(text)

f_new.close()
f_old.close()