import puppeteer from 'puppeteer';
import path from 'path';

// The manifest.json is in the root, so the extension path is the current directory.
const extensionPath = path.resolve('.');

(async () => {
  console.log(`Launching browser with extension ${extensionPath}`);

  const browser = await puppeteer.launch({
    headless: false,
    protocol: 'webDriverBiDi',
    args: [
      `--disable-extensions-except=${extensionPath}`,
      `--load-extension=${extensionPath}`,
    ],
  });

  console.log(`Creating a page`);
  const page = await browser.newPage();
  console.log(`Navigating to the extension page`);
  await page.goto('chrome-extension://mkeohjlfgalobdegbiheindkfjmgkiem/manifest.json');

  console.log(`Closing page`);
  await page.close()
  console.log(`Closed`);

  console.log(`Creating another page`);
  const another_page = await browser.newPage()
  console.log(`Navigating another page`);
  await another_page.goto('https://google.com')
  console.log(`Closing another page`);
  await another_page.close()

  console.log(`Closing browser`);
  await browser.close();
})();
