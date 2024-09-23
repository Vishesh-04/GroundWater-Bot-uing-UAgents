# Groundwater Details Providing Fetch.ai Agent
## Project Description
The Groundwater Query Agent is a district-based groundwater data retrieval system built using Fetch.AI's uAgents library. This agent allows users to input a district name and fetch detailed groundwater statistics, such as annual groundwater draft, replenishable groundwater resources, and the projected demand for future years. The data is sourced from a JSON file and presented in a user-friendly format to help users understand the groundwater availability and usage in specific districts.


## Features
### 1. District-Based Groundwater Query:
Users can input the name of any district to retrieve the latest groundwater data.
The agent automatically fetches and displays detailed groundwater statistics for the specified district.
### 2. Groundwater Data Details:
Annual Domestic & Industrial Draft: Displays the amount of groundwater used for domestic and industrial purposes.
Annual Irrigation Draft: Shows the amount of groundwater used for irrigation.

Total Annual Groundwater Draft: Provides the total groundwater usage for the district.

Replenishable Groundwater Resources: Displays the annual replenishable groundwater available.

Natural Discharge during Non-Monsoon: Shows the amount of groundwater naturally discharged during the non-monsoon season.

Net Groundwater Availability: Displays the total groundwater available for use.
Projected Demand up to 2025: Shows the projected demand for groundwater in the future.

Stage of Groundwater Development: Provides the current stage of groundwater development in percentage.
### 3. Error Handling:
The agent handles exceptions and notifies users if there is any failure in retrieving groundwater data.
## Use Cases
#### 1. Urban and Rural Planning:
Scenario: A city planner or water resource manager needs to understand the current groundwater usage in a specific district.

Solution: The user inputs the district name, and the agent provides detailed groundwater data to help in resource planning and decision-making.
#### 2. Agricultural Planning:
Scenario: A farmer or agricultural planner wants to check the availability of groundwater for irrigation.

Solution: The user inputs their district and receives data on groundwater availability for irrigation, assisting in crop planning.
#### 3. Policy Making:
Scenario: A government official is drafting policies related to groundwater management.

Solution: The official inputs various districts and retrieves data to help understand groundwater trends and allocate resources efficiently.
#### 4. Environmental Research:
Scenario: A researcher is studying groundwater depletion across various 
districts.

Solution: The researcher can query the agent for groundwater data across different regions for their analysis.
## Technical Details
Agent: The agent is built using Fetch.AI's uAgents library.

Data Source: Groundwater data is stored in a JSON file and is retrieved based on district queries.

Protocol: The groundwater_protocol handles user queries and manages responses.

Data Handling: The agent processes groundwater data to provide status alerts and detailed statistics, ensuring users receive accurate updates on groundwater availability.
## Future Enhancements
Historical Groundwater Data: Provide users with trends over previous years to assist in long-term planning.
Predictive Analytics: Integrate machine learning models to predict future groundwater levels based on current usage.
Web Interface: Develop a web interface where users can visually explore groundwater data.
Localization: Support for multiple languages to cater to a global audience.
## Project Implementation Video
[Demo Video Link](https://drive.google.com/file/d/1ipdPG3cfjkF-dhbVCLvWBjJLwwEfKIv2/view?usp=sharing)

## How to Run the Project
### Step 1: Create a Account on DeltaV
### Step 2: Search for Ground Water
### Step 3: Follow the Demo Video

## Collabration
This project is created with support of Fetch.ai Innovation Lab, Meerut Institute of Engineering and Technology, Meerut, Uttar Pradesh, India.
