import pandas as pd # import pandas (alias pd) which is needed for basic dataframe operations
# create a simple dataframe

def summarize_column(df, column):
    """
    Return simple descriptive statistics for one column.
    It takes a dataframe and column name as input and returns mean, min, and max.
    Stateless: no memory between calls.
    """
    return {
        "mean": df[column].mean(),
        "min": df[column].min(),
        "max": df[column].max(),
    }

data = {'age': [25, 30, 35, 40, 45], 
        'salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)
print(df)

# call the function to compute summary statistics for the 'age' column
summary = summarize_column(df, 'age')
print(summary)

class DataAnalysisAgent:
    def __init__(self, df):
        self.df = df
        self.history = []
        self.steps = 0

    def analyze_column(self, column):
        # Exception handling: check that the column exists before trying to analyze it
        if column not in self.df.columns:
            raise ValueError(
                f"Column '{column}' not found. "
                f"Available columns: {list(self.df.columns)}"
            )

        # If the column exists, the agent can safely proceed
        self.steps += 1

        result = {
            "column": column,
            "mean": self.df[column].mean(),
            "min": self.df[column].min(),
            "max": self.df[column].max(),
        }

        # Record the successful action in the agent's memory
        self.history.append(result)

        return result
        return result
    
# define the agent object
agent = DataAnalysisAgent(df)

result = agent.analyze_column("age")
print("Analysis Result:", result)
print("Agent History:", agent.history)  # now has one entry
print("Agent Steps:", agent.steps)    # now 1


result = agent.analyze_column("salary")
print("Analysis Result:", result)
print("Agent History:", agent.history) 
print("Agent Steps:", agent.steps) 

# Showcase Error Handling
try:
    agent.analyze_column("gender")
except ValueError as e:
    print("Column does not exist. Agent failed safely:")
    print(e)

print("Steps:", agent.steps)
print("History:", agent.history)
