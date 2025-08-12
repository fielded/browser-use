import asyncio
from agents import login_agent, planning_agent ,password_reset , packing_agent , add_product , auto_routes , psm_orders,stock_report, analytics_exports , route_forwarding
from helpers.browser_session import get_browser_and_context

async def main():
    browser, browser_context = await get_browser_and_context()

    try:
    
   #  print("==Running Password Reset agent ===")
   #  await password_reset.run_agent(browser=browser, browser_context=browser_context)
     
   #  print("=== Running Packing agent ===")
   #  await packing_agent.run_agent(browser=browser, browser_context=browser_context)
   
     print("== Running Auto route generation agent == ")
     await auto_routes.run_agent(browser=browser, browser_context=browser_context)
   
   #  print("== Running stock report agent==")
   #  await stock_report.run_agent(browser=browser, browser_context=browser_context)
     
     print("== Running Route forwarding agent ==")
     await route_forwarding.run_agent(browser=browser, browser_context=browser_context)
     
     print("== Running Analytics Exports agent ==")
     await analytics_exports.run_agent(browser=browser, browser_context=browser_context)
     
     print("== Running Main orders agent ==")
     await psm_orders.run_agent(browser=browser, browser_context=browser_context)
   
     print("== Running Product Addition agent ==")
     await add_product.run_agent(browser=browser, browser_context=browser_context)
     
     print("=== Running Login Agent ===")
     await login_agent.run_agent(browser=browser, browser_context=browser_context)

     print("\n=== Handover to Planning Agent ===")
     await planning_agent.run_agent(browser=browser, browser_context=browser_context)
    
    finally:
        # Ensure the browser is closed even if an error occurs
        await browser_context.close()
        await browser.close()
        print("Browser and context closed.")

if __name__ == "__main__":
    asyncio.run(main())
