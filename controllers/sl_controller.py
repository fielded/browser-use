import asyncio
from  agents import main_agent
from helpers.browser_session import get_browser_session

async def main():
    browser_session = await get_browser_session()

    try:
    
      print("==Running Password Reset agent ===")
      await main_agent.run_agent(browser_session=browser_session, tasks="tasks/SL/password_reset.yaml", feature="Password Reset")
      
      print("=== Running Packing agent ===")
      await main_agent.run_agent(browser_session=browser_session, tasks="tasks/SL/packing.yaml", feature="Packing")
    
      print("== Running SL Product Addition agent ==")
      await main_agent.run_agent(browser_session=browser_session, tasks="tasks/SL/add_product.yaml", feature="SL Product Addition")
      
      print("=== Running SL Login Agent ===")
      await main_agent.run_agent(browser_session=browser_session, tasks="tasks/SL/login", feature="SL Login")

      print("\n=== Handover to Resupply Planning Agent ===")
      await main_agent.run_agent(browser_session=browser_session, tasks="tasks/PSM/resupply_plan.yaml", feature="Resupply Planning")
      
    finally:
      # Ensure the browser is closed even if an error occurs
      await browser_session.close()
      print("Browser session closed.")
