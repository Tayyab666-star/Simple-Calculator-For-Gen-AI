import streamlit as st

# Simple Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit App
def main():
    st.title("Simple Calculator")
    st.write("This is a basic calculator that performs addition, subtraction, multiplication, and division.")

    # Select operation
    operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])
    
    # Input numbers
    num1 = st.number_input("Enter the first number", format="%.2f")
    num2 = st.number_input("Enter the second number", format="%.2f")

    # Perform calculation based on the selected operation
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
            st.success(f"Result: {num1} + {num2} = {result}")
        elif operation == "Subtract":
            result = subtract(num1, num2)
            st.success(f"Result: {num1} - {num2} = {result}")
        elif operation == "Multiply":
            result = multiply(num1, num2)
            st.success(f"Result: {num1} * {num2} = {result}")
        elif operation == "Divide":
            result = divide(num1, num2)
            st.success(f"Result: {num1} / {num2} = {result}")

# Run the app
if __name__ == '__main__':
    main()
