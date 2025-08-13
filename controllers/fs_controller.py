import asyncio
from  agents import main_agent
from helpers.browser_session import get_browser_session

async def main():
    browser_session = await get_browser_session()

    try:
    
      # print("==Running Password Reset agent ===")
      # await agent.run_agent(browser_session=browser_session, tasks="tasks/SL/password_reset.yaml", feature="Password Reset")
      
      # print("=== Running Packing agent ===")
      # await agent.run_agent(browser_session=browser_session, tasks="tasks/SL/packing.yaml", feature="Packing")
    
      print("== Running Auto route generation agent == ")
      await main_agent.run_agent(browser_session=browser_session, tasks="tasks/PSM/auto_routes.yaml", feature="Auto Route Generation")
    
      # print("== Running stock report agent==")
      # await agent.run_agent(browser_session=browser_session, tasks="tasks/PSM/stock_report.yaml", feature="Stock Report")
      
      # print("== Running Route forwarding agent ==")
      # await agent.run_agent(browser_session=browser_session, tasks="tasks/PSM/route_forwarding.yaml", feature="Route Forwarding")
      
      # print("== Running Analytics Exports agent ==")
      # await agent.run_agent(browser_session=browser_session, tasks="tasks/PSM/analytics_exports.yaml", feature="Analytics Exports")
      
      # print("== Running Main orders agent ==")
      # await agent.run_agent(browser_session=browser_session, tasks="tasks/PSM/psm_orders.yaml", feature="PSM Orders")
    
      # print("== Running Product Addition agent ==")
      # await agent.run_agent(browser_session=browser_session, tasks="tasks/PSM/add_product.yaml", feature="Product Addition")
      
      # print("=== Running Login Agent ===")
      # await agent.run_agent(browser_session=browser_session, tasks="tasks/PSM/login.yaml", feature="Login")

      # print("\n=== Handover to Planning Agent ===")
      # await agent.run_agent(browser_session=browser_session, tasks="tasks/PSM/planning.yaml", feature="Planning")
      
    finally:
      # Ensure the browser is closed even if an error occurs
      await browser_session.close()
      print("Browser session closed.")


# if __name__ == "__main__":
#     asyncio.run(main())
