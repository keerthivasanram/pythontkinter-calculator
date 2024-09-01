import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.create_widgets()
        
    def create_widgets(self):
        # Create an entry widget for displaying the input/output
        self.entry = tk.Entry(self.root, width=20, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define calculator buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Set initial row and column
        col = 0
        row = 1

        # Create buttons dynamically and define the command directly
        for button in buttons:
            if button in "1234567890+-*/":
                tk.Button(
                    self.root, 
                    text=button, 
                    width=5, 
                    height=2, 
                    font=("Arial", 16), 
                    command=lambda b=button: self.entry.insert(tk.END, b)
                ).grid(row=row, column=col, padx=5, pady=5)
            elif button == "C":
                tk.Button(
                    self.root, 
                    text=button, 
                    width=5, 
                    height=2, 
                    font=("Arial", 16), 
                    command=self.clear
                ).grid(row=row, column=col, padx=5, pady=5)
            elif button == "=":
                tk.Button(
                    self.root, 
                    text=button, 
                    width=5, 
                    height=2, 
                    font=("Arial", 16), 
                    command=self.calculate
                ).grid(row=row, column=col, padx=5, pady=5)
            
            col += 1
            if col > 3:  # There are only 4 columns
                col = 0
                row += 1
                
    def calculate(self):
        input_value = self.entry.get()
        
        try:
            result = eval(input_value)    
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "ERROR")
            
    def clear(self):
        self.entry.delete(0, tk.END)
    
    
# Initialize the main application window
root = tk.Tk()
root.geometry("300x400")

# Create an instance of the Calculator class
cal = Calculator(root)

# Run the main event loop
root.mainloop()
