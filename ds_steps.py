import streamlit as st
import graphviz as graphviz

# Create a graphlib graph object


graph = graphviz.Digraph()
graph.edge('Select a Data Set' , 'Explore Data')
graph.edge('Select a Data Set', 'Visualize Data')
graph.edge('Explore Data', 'Perform Data Cleaning')
graph.edge('Perform Data Cleaning', 'Perform Data Wrangling')
graph.edge('Use ML Algorithms','Build Machine Model')
graph.edge('Perform Data Wrangling', 'Build Machine Model')
graph.edge('Build Machine Model', 'Train Model')
graph.edge('Train Model', 'Test Model')
graph.edge('Test Model', 'Tested Model')
graph.edge('Tested Model', 'End')
graph.edge('Tested Model', 'Deploy Model')
graph.edge('Deploy Model','As Local Web App')
graph.edge('Deploy Model', 'As Cloud Web App, e.g. Streamlit/Heroku/AWS')


# st.graphviz_chart(graph)

