from joblib import load
model = load('final_model.joblib')

review= input('Enter your review here: \n')

test=[review]

ans = model.predict(test)
print(ans)