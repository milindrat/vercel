// api/index.js
export default function handler(req, res) {
    // Simple API endpoint to handle GET requests
    res.status(200).json({ message: "Hello from API!" });
  }
  