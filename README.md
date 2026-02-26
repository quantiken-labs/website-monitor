# Website Monitor (Podman) — Test Version

⚠️ IMPORTANT NOTICE  
This software is a **test / evaluation version of a paid subscription service**.  
It is provided **strictly for testing, development, and evaluation purposes only**.

**Production use is not permitted.**  
Commercial use, resale, or long-term monitoring is **not allowed** without an active paid subscription.

---

## Project Structure

website-monitor/
├── monitor.py  
├── Containerfile  
├── .env  
└── README.md  

---

## How It Works

This test version demonstrates the core functionality of the paid service:

- Runs inside a Podman container
- Periodically sends HTTP requests to a configured website
- Detects downtime (timeouts or non-200 HTTP responses)
- Sends an email alert when downtime is detected

This version exists **only to validate functionality** and **evaluate behavior** in test environments.

---

## Intended Use (Test-Only)

This software may be used **only** for:

- Local testing
- Development environments
- Proof-of-concept deployments
- Feature evaluation

Not allowed:

- Production deployments
- Commercial monitoring
- SLA enforcement
- High-availability monitoring
- Resale or redistribution

---

## Requirements

- Podman installed
- Internet access from the test server
- SMTP credentials for alert testing

---

## Configuration

All configuration is done using environment variables.

### .env file (Test Only)

MONITOR_URL=https://test-website.com  
CHECK_INTERVAL=60  
EMAIL_USER=testemail@gmail.com  
EMAIL_PASS=testpassword  
EMAIL_TO=alerttest@gmail.com  

---

### Configuration Variables

MONITOR_URL  
Website to test monitoring against

CHECK_INTERVAL  
Time between test checks (seconds)

EMAIL_USER  
Test SMTP email username

EMAIL_PASS  
Test SMTP password

EMAIL_TO  
Test alert recipient

⚠️ Use test credentials only. Do not use production credentials.

---

## Build the Test Container

podman build -t website-monitor-test .

---

## Run the Test Monitor

podman run -d --env-file .env website-monitor-test

---

## Logs (Testing & Debugging)

podman logs website-monitor-test  

Live logs:

podman logs -f website-monitor-test

---

## Stop the Test Monitor

podman ps  
podman stop <container_id>

---

## Security Disclaimer

This test version:

- Is not production hardened
- Does not include alert throttling or redundancy
- May generate false positives
- Stores credentials in environment variables for testing simplicity

---

## Production Disclaimer

This software is **NOT suitable for production use**.

For guaranteed uptime checks, redundant monitoring, SLA enforcement, secure credential handling, and advanced alerting, a **paid subscription version is required**.

---

## License

Test License Only

Use of this software is limited to testing and evaluation.  
All other rights are reserved.
