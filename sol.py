import asyncio
from pyppeteer import launch

async def autoconnect_solgpt():
    # Launch browser (set headless=False if you want to see the browser)
    browser = await launch(headless=True)
    page = await browser.newPage()

    # Go to solgpt.ai
    await page.goto('https://solgpt.ai/', {'waitUntil': 'networkidle2'})

    # Example: Wait for a "Connect Wallet" button and click it
    # You need to inspect the actual button selector on solgpt.ai
    try:
        # Wait for the connect button to appear (adjust selector accordingly)
        await page.waitForSelector('button.connect-wallet', timeout=5000)
        await page.click('button.connect-wallet')
        print("Clicked Connect Wallet button")

        # If there's a popup or modal for wallet connection, handle it here
        # For example, wait for wallet modal and select wallet type
        # await page.waitForSelector('button.wallet-type', timeout=5000)
        # await page.click('button.wallet-type')

        # Add more steps if needed for wallet authentication

    except Exception as e:
        print("Connect wallet button not found or error:", e)

    # Optionally, take a screenshot after connection attempt
    await page.screenshot({'path': 'solgpt_connect.png'})

    # Close browser
    await browser.close()

# Run the async function
asyncio.get_event_loop().run_until_complete(autoconnect_solgpt())
