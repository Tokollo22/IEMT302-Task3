\A#!/.*python3?$

from sklearn.linear_model import LinearRegression

# Training data
X = [[1], [2], [3], [4], [5]]

y = [35000, 40000, 45000, 50000, 55000]

# Create the machine learning model
def main():
  model = LinearRegression()

# Train the model
  model.fit(X, y)

# Make a prediction
  prediction = model.predict([[5.5]])

  print("Predicted salary:", prediction[0])

if __name__ == "__main__":
    main()
