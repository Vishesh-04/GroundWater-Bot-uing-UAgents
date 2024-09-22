from uagents import Agent, Context, Protocol, Model
from pydantic import Field
from ai_engine import UAgentResponse, UAgentResponseType

# Define the protocol for groundwater queries
groundwater_protocol = Protocol(name="groundwater_protocol")

# Define the model for querying groundwater data
class QueryGroundwaterRequest(Model):
    location: str = Field(description="Location for groundwater query")

# Function to fetch groundwater data from JSON file
def fetch_groundwater_data(location, data):
    for district_data in data:
        if district_data.get('district_name', '').lower() == location.lower():
            return True, district_data
        
        # Return False if no matching district is found
    return False, None

# Handler for processing groundwater query requests
@groundwater_protocol.on_message(model=QueryGroundwaterRequest, replies={UAgentResponse})
async def handle_groundwater_query(ctx: Context, sender: str, msg: QueryGroundwaterRequest):
    data = ctx.storage.get("data")
    if not data:
        error_message = "Groundwater data is not available."
        await ctx.send(sender, UAgentResponse(message=error_message, type=UAgentResponseType.FINAL))
        return

    status, groundwater_data = fetch_groundwater_data(msg.location, data)

    if status:
        # Format the groundwater data for response
        groundwater_info = (
            f"Groundwater data for {msg.location}:\n"
            f"District: {groundwater_data.get('district_name', 'N/A')}\n"
            f"Annual Domestic & Industrial Draft: {groundwater_data.get('annual_domestic_industrial_draft', 0.0)} m³\n"
            f"Annual Irrigation Draft: {groundwater_data.get('annual_irrigation_draft', 0.0)} m³\n"
            f"Total Annual Groundwater Draft: {groundwater_data.get('annual_groundwater_draft_total', 0.0)} m³\n"
            f"Annual Replenishable Groundwater Resources: {groundwater_data.get('annual_replenishable_groundwater_resources', 0.0)} m³\n"
            f"Natural Discharge during Non-Monsoon: {groundwater_data.get('natural_discharge_during_non_monsoon', 0.0)} m³\n"
            f"Net Groundwater Availability: {groundwater_data.get('net_groundwater_availability', 0.0)} m³\n"
            f"Projected Demand up to 2025: {groundwater_data.get('projected_demand_upto_2025', 0.0)} m³\n"
            f"Groundwater Availability for Irrigation: {groundwater_data.get('groundwater_availability_for_irrigation', 0.0)} m³\n"
            f"Stage of Groundwater Development: {groundwater_data.get('stage_of_groundwater_development', 0.0)}%\n"
        )
        await ctx.send(sender, UAgentResponse(message=groundwater_info, type=UAgentResponseType.FINAL))
    else:
        error_message = "Failed to retrieve groundwater data."
        await ctx.send(sender, UAgentResponse(message=error_message, type=UAgentResponseType.FINAL))

# Create an instance of the Agent class
agent = Agent()
agent.include(groundwater_protocol, publish_manifest=True)

if __name__ == "__main__":
    agent.run()