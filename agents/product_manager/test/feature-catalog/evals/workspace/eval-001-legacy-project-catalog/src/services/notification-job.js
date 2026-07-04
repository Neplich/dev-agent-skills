const cron = require("node-cron");

// Background job: every 10 minutes, email customers whose order status changed.
cron.schedule("*/10 * * * *", () => {
  // scan orders with pending notifications and send status emails
});
