import os
import subprocess
import tkinter as tk

class VoiceAssistant(tk.Tk):
    def _init_(self):
        super()._init_()

        # Set the window title and size
        self.title("Voice Assistant")
        self.geometry("600x400")

        # Create the main frame
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the input and output widgets
        self.input_text = tk.Text(main_frame, bg="lightgray", font=("Arial", 14))
        self.input_text.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.output_text = tk.Text(main_frame, bg="white", font=("Arial", 14))
        self.output_text.pack(side=tk.BOTTOM, fill=tk.X, expand=True)

        # Create the button to submit the input
        submit_button = tk.Button(main_frame, text="Submit", command=self.submit)
        submit_button.pack(side=tk.BOTTOM)

    def submit(self):
        # Get the input text
        input_text = self.input_text.get("1.0", tk.END).strip()

        # Clear the input text widget
        self.input_text.delete("1.0", tk.END)

        # Process the input text
        self.process_input(input_text)

    def process_input(self, input_text):
        # Split the input text into words
        words = input_text.split()

        # Check if the first word is a command
        if words[0] == "scan":
            # Run the antivirus scan
            self.run_antivirus_scan()
        elif words[0] == "exit":
            # Exit the program
            self.destroy()
        else:
            # Print an error message
            self.output_text.insert(tk.END, "Unrecognized command\n")

    def run_antivirus_scan(self):
        # Run the antivirus scan
        result = subprocess.run(["antivirus_command"], stdout=subprocess.PIPE)

        # Print the scan results
        self.output_text.insert(tk.END, result.stdout)

if '_name_' == "_main_":
    app = VoiceAssistant()
app.mainloop()