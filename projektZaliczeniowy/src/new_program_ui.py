import tkinter as tk
from tkinter import ttk, scrolledtext
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_visualizer import DataVisualizer
from data_loader import DataLoader

class ProgramUi:
    def __init__(self):
        self.data_loader = DataLoader('data/healthcare-dataset-stroke-data.csv')
        self.data_visualizer = DataVisualizer(self.data_loader.get_data())
        self.root = tk.Tk()
        self.root.title("Data Visualization Dashboard")
        self.figure_frame = None  # Frame to hold the canvas

        # Configure the grid layout manager
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Create a frame for displaying DataFrame outputs
        self.data_frame = ttk.Frame(self.root)
        self.data_frame.pack(fill='both', expand=True)
        self.text_area = scrolledtext.ScrolledText(self.data_frame, wrap=tk.WORD, width=80, height=20)
        self.text_area.grid(row=0, column=0, sticky='nsew', padx=(10, 5), pady=10)

        # Description text area
        self.description_area = scrolledtext.ScrolledText(self.data_frame, wrap=tk.WORD, width=40, height=20)
        self.description_area.grid(row=0, column=1, sticky='nsew', padx=(5, 10), pady=10)

    def clear_figure_frame(self):
        """Clears the current figure frame to prepare for a new visualization."""
        if self.figure_frame:
            for widget in self.figure_frame.winfo_children():
                widget.destroy()
            self.figure_frame.pack_forget()
            self.figure_frame = None

    def display_figure(self, fig):
        """Displays the given matplotlib figure in the UI."""
        self.clear_figure_frame()  # Clear previous figures
        self.figure_frame = ttk.Frame(self.root)
        self.figure_frame.pack(fill='both', expand=True)
        canvas = FigureCanvasTkAgg(fig, master=self.figure_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill='both', expand=True)
        canvas.draw()

    def display_dataframe(self, df):
        """Clears previous content and displays the given DataFrame in the text area."""
        self.text_area.delete('1.0', tk.END)  # Clear previous content
        self.text_area.insert(tk.END, df.to_string())  # Insert DataFrame as a string

    def run_visualization(self, visualization_func, description="", is_data=False):
        """Runs a visualization function and handles displaying the figure or data."""
        try:
            result = visualization_func()
            if isinstance(result, Figure):
                self.display_figure(result)
            elif is_data:
                self.display_dataframe(result)
            self.description_area.delete('1.0', tk.END)
            self.description_area.insert(tk.END, description)
            print("Visualization completed successfully.")
        except Exception as e:
            print(f"Error during visualization: {str(e)}")

    def run_ui(self):
        """Sets up the UI and buttons for running visualizations."""

        ttk.Button(self.root, text="Bar Diagram of Strokes per Age",
                   command=lambda: self.run_visualization(self.data_visualizer.bar_diagram_of_strokes_per_age, description='The graph “Age vs Number of cases” shows an increasing trend of stroke cases with age, particularly spiking after age 50, highlighting the heightened risk in older adults.')).pack(fill='x')
        ttk.Button(self.root, text="Pie of Strokes per Smoker",
                   command=lambda: self.run_visualization(self.data_visualizer.pie_of_strokes_per_smoker, description='The largest proportion of stroke patients have never smoked (37.0%), followed by a significant percentage with unknown smoking status (30.2%), indicating that factors other than active smoking, including genetics or other health conditions, may play major roles in stroke incidence; however, smoking history is still a notable risk factor, with 32.7% of stroke patients having smoked at some point in their lives (17.3% formerly smoked and 15.4% currently smoke).')).pack(fill='x')
        ttk.Button(self.root, text="Line of Man vs Woman per Age",
                   command=lambda: self.run_visualization(self.data_visualizer.line_of_man_vs_woman_per_age, description='The graph “Number of Strokes by Age Group and Gender” shows that stroke incidence peaks in the 50-59 age group for both genders, with females consistently exhibiting higher stroke rates than males throughout the age spectrum. After reaching the peak, stroke incidence declines for both genders, with rates converging as age increases beyond 80.')).pack(fill='x')
        ttk.Button(self.root, text="Scatter Plot (Glucose vs BMI)",
                   command=lambda: self.run_visualization(lambda: self.data_visualizer.scatter_plot('avg_glucose_level', 'bmi'), description='The scatter plot “Avg Glucose Level vs BMI” shows that among stroke patients, there is a wide range of BMI values across different average glucose levels, with no clear correlation between the two. This suggests that both high and low glucose levels are present across various BMI categories, indicating that stroke risk is influenced by multiple factors beyond just BMI and glucose levels.')).pack(fill='x')
        ttk.Button(self.root, text="Work Type Distribution",
                   command=lambda: self.run_visualization(self.data_visualizer.plot_work_type_distribution, description='The pie chart “Work Type Distribution” indicates that a significant majority of stroke patients were employed in the private sector (57.2%), highlighting a potentially high-stress environment or other risk factors prevalent in this group. Additionally, the presence of strokes among self-employed individuals (16.0%) and children (13.4%) suggests diverse risk factors across different demographics, while the relatively low incidence in government workers (12.9%) and those who never worked (0.4%) may indicate differing levels of risk exposure or access to healthcare.')).pack(fill='x')
        ttk.Button(self.root, text="Residence Type Distribution",
                   command=lambda: self.run_visualization(self.data_visualizer.plot_residence_type_distribution, description="The bar chart “Residence Type Distribution” reveals that stroke incidents are nearly equally distributed between urban and rural areas, suggesting that stroke risk factors are prevalent in both environments. This indicates the need for comprehensive stroke prevention and healthcare strategies that address both urban and rural populations.")).pack(fill='x')
        ttk.Button(self.root, text="Marital Status by Gender",
                   command=lambda: self.run_visualization(self.data_visualizer.plot_marital_status_by_gender, description="The bar chart “Marital Status by Gender” shows that married females have the highest incidence of strokes, followed by married males, indicating a possible link between marital status and stroke risk. Unmarried individuals of both genders exhibit lower stroke counts, suggesting that marital status may be a factor worth investigating further in stroke risk studies.")).pack(fill='x')
        ttk.Button(self.root, text="Pair Plot Of Age, Glucose, and BMI",
                   command=lambda: self.run_visualization(lambda: self.data_visualizer.plot_pair_plot(['age', 'avg_glucose_level', 'bmi']))).pack(fill='x')
        ttk.Button(self.root, text="Average of Columns",
                   command=lambda: self.run_visualization(lambda: self.data_visualizer.count_average_year_of_columns(['age', 'avg_glucose_level', 'bmi', 'stroke']), is_data=True, description='The table indicates that stroke patients are on average 43.2 years old, with an average glucose level of 106.1 mg/dL and an average BMI of 28.9, categorizing them as overweight. Furthermore, nearly 4.9% have a parent who also suffered from a stroke, underscoring the significant role of genetic factors in stroke risk.')).pack(fill='x')
        ttk.Button(self.root, text="Print Gender Distribution",
                   command=lambda: self.run_visualization(self.data_visualizer.print_gender_distribution, is_data=True, description='The table shows that 58.6% of stroke patients are female, 41.4% are male, and 0.02% identify as other, highlighting a higher prevalence of strokes among females compared to males.')).pack(fill='x')
        ttk.Button(self.root, text="Calculate Risk Score",
                   command=lambda: self.run_visualization(self.data_visualizer.calculate_risk_score, is_data=True)).pack(fill='x')
        self.root.mainloop()