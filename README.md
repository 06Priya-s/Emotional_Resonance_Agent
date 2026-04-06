# Emotional Resonance Agent

An AI-powered agent built with Google ADK (Agent Development Kit) and Gemini that analyzes and optimizes content for specific emotional responses.


## 🎯 What It Does

This agent performs **one clearly defined task**: analyzing content and providing recommendations to enhance emotional resonance for target emotions like empathy, excitement, trust, urgency, curiosity, inspiration, nostalgia, humor, serenity, and anticipation.



## 🚀 Live Demo

The agent is deployed on Google Cloud Run and accessible via ADK Dev UI:

**Live URL:** `https://emotional-resonance-guide-734642101049.europe-west1.run.app`

<img width="1898" height="1048" alt="Screenshot 2026-04-07 013057" src="https://github.com/user-attachments/assets/a10c8a0d-d6e1-4b3e-98d0-d49c09cf24a1" />



## 📋 Features

- ✅ Single-purpose AI agent for focused responses
- ✅ ADK-based architecture
- ✅ Gemini-powered natural language understanding
- ✅ HTTP endpoint for easy interaction
- ✅ Cloud Run deployment for scalability


## 🛠️ Technologies Used

|        Technology           |                          Purpose                      |
|       -------------         |                        ------------                   |
|         Google ADK          |            Agent development and orchestration        |
|        Google Gemini        | Natural language understanding and emotional analysis |
|           Python            |                     Core agent logic                  |
|       Google Cloud Run      |             Serverless deployment and hosting         |
|         ADK Dev UI          |                 Interactive web interface             |




## 📁 Project Structure
<pre> emotional-resonance-agent/
├── init.py # Python package initializer
├── agent.py # ADK Emotional Resonance Agent logic
└── requirements.txt # Python dependencies </pre>



## 🔧 Local Development

### Prerequisites

- Python 3.11+
- Google Cloud account
- Gemini API key



### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/emotional-resonance-agent.git
cd emotional-resonance-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY="your-api-key-here"

# Run the ADK development server
python -m adk serve
