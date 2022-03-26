# get inputs
original_hats = input().split()
target_hats = input().split()
 
n_differences = sum([o != t for o, t in zip(original_hats, target_hats)])
 
msg = 'No' if n_differences == 2 else 'Yes'
print(msg)
