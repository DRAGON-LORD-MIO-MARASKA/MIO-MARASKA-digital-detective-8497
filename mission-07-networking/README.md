# Mission 7 — How computers communicate

## 1. Task / objective
Explain basic network types and concepts, observe network lookup and connectivity information, and describe what happens when you open a website.

## 2. Work completed
- Completed the network-concepts table with explanations and examples for LAN, MAN, WAN, DNS, router, protocol, packet switching and client-server.
- Used Terminal to test connectivity and perform a DNS lookup.
- Wrote a step-by-step explanation of what happens when you open a website in a browser.

## 3. Commands / tools used
- `ping -c 4 example.com` — Send four packets to check if a remote server is reachable and measure round-trip time.
- `nslookup example.com` — Query a DNS server to find the IP address associated with a domain name.

## 4. My understanding

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
|---------|----------------------------|---------|
| LAN | A network covering a small area, such as a home, lab or office, connecting nearby devices | The Wi-Fi network in my home that links my laptop, phone and printer |
| MAN | A network covering a city or large campus area, larger than a LAN but smaller than a WAN | A university campus network that connects multiple buildings across a city block |
| WAN | A network covering large geographical areas, often connecting multiple LANs across cities or countries | The internet itself is the largest WAN, connecting networks worldwide |
| DNS | Translates human-readable domain names into IP addresses so computers can locate each other | Typing `google.com` in a browser → DNS resolves it to an IP like `142.250.x.x` |
| Router | Connects networks and forwards data between them, choosing the best path for each packet | A home router connects the local Wi-Fi network to the internet service provider |
| Protocol | A set of rules devices follow to communicate, ensuring data is sent, received and understood correctly | HTTP defines how a browser requests a web page and how the server responds |
| Packet switching | Data is divided into small packets that travel independently across the network and are reassembled at the destination | When downloading an image, it arrives as many small packets that the computer combines back into the full file |
| Client-server | A model where a client requests a service and a server provides it | A web browser (client) requests a page from a web server (server), which sends the HTML back |

### Task 7.2 — Observe network information

**Connectivity test (`ping`):**
- Sent four packets to `example.com`. All four received replies with low round-trip times.
- A connectivity test helps me check whether my computer can reach a remote server. If packets are lost or times are very high, there may be a network issue.

**DNS lookup (`nslookup`):**
- Queried `example.com` and received an IP address (e.g., `93.184.216.34`).
- A DNS lookup shows which IP address a domain name points to. This confirms that DNS resolution is working and reveals the server's address.

**Role of DNS when you enter a website name:**
When you type a URL like `example.com` in a browser, your computer does not know where that server is. It asks a DNS server to translate the name into an IP address. Once it has the IP, the browser can connect to the correct server and request the web page.

*(All IP addresses and network details in this document are publicly available example values. No personal IP, Wi-Fi name or private network information is included.)*

### Task 7.3 — What happens when you open a website

1. **You type the URL** — You enter `example.com` in the browser's address bar and press Enter.
2. **DNS resolution** — The browser asks a DNS server to translate `example.com` into an IP address (e.g., `93.184.216.34`).
3. **Connection to the server** — Using the IP address, the browser establishes a connection with the web server over the internet, following the TCP protocol to ensure reliable communication.
4. **HTTP request** — The browser sends an HTTP (or HTTPS) request to the server, asking for the web page at the specified URL.
5. **Server processes the request** — The web server receives the request, finds the requested page (HTML file, images, scripts), and prepares a response.
6. **Server sends the response** — The server sends the HTML content and any associated files back to the browser, broken into packets that travel across the network.
7. **Browser renders the page** — The browser receives the packets, reassembles them, interprets the HTML, CSS and JavaScript, and displays the finished web page on your screen.

## 5. Difficulties faced
No major difficulties. Remembering to redact any personal network information (IP addresses, Wi-Fi names) from outputs required attention.

## 6. How I resolved them
Used only publicly known example domains and IP addresses in this document. Any real output was reviewed and personal details removed.

## 7. Evidence / files
- This README.md documents all network concepts, observations and the website-opening explanation.

## 8. Commit details
- **Commit message:** "Explain networking concepts and website communication"
- **Pushed to GitHub:** Yes
