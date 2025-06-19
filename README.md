# FactFlux

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/github/license/MeirKaD/FactFlux)
![Last Commit](https://img.shields.io/github/last-commit/MeirKaD/FactFlux)
![Issues](https://img.shields.io/github/issues/MeirKaD/FactFlux)
![Stars](https://img.shields.io/github/stars/MeirKaD/FactFlux?style=social)
![Forks](https://img.shields.io/github/forks/MeirKaD/FactFlux?style=social)

An intelligent multi-agent system for fact-checking social media posts using Agno framework and Bright Data tools.

## 🚀 Features

- **Multi-Platform Support**: TikTok, Instagram, Twitter/X, Facebook, YouTube, LinkedIn
- **Intelligent Tool Selection**: Automatically chooses optimal scraping methods
- **Comprehensive Analysis**: Content extraction, claim identification, cross-referencing, verdict synthesis
- **Authoritative Sources**: Verifies against news sites, fact-checkers, official sources
- **Confidence Scoring**: Evidence-based verdicts with transparency

## Demo

<div align="center">
  <a href="https://www.youtube.com/watch?v=l_JVNBlOFOc">
    <img src="https://img.youtube.com/vi/l_JVNBlOFOc/maxresdefault.jpg" alt="FactFlux Demo Video" width="600">
  </a>
  <p><em>Click to watch FactFlux in action</em></p>
</div>


## 📋 Prerequisites

- Python 3.8+
- Valid API keys for:
  - Google's Gemini
  - Bright Data

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MeirKaD/FactFlux.git
   cd FactFlux
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

## 🔧 Configuration

Create a `.env` file with your API keys:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
BRIGHT_DATA_API_KEY=your_bright_data_api_key_here
```

## 🎯 Usage

### Playground Mode (Recommended)
```bash
python playground_fact_check.py
```

## 🏗️ Architecture

### Agent Team Structure

1. **Content Extractor Agent**
   - Extracts post data using optimal Bright Data tools
   - Handles multiple platforms automatically

2. **Claim Identifier Agent**
   - Identifies verifiable factual claims
   - Separates facts from opinions/satire

3. **Cross-Reference Agent**
   - Verifies claims against authoritative sources
   - Performs reverse media searches

4. **Verdict Agent**
   - Synthesizes evidence and delivers final verdict
   - Provides confidence scores and reasoning

### Workflow Process

```
URL Input → Content Extraction → Claim Identification → Cross-Reference → Final Verdict
```

## 🛡️ Supported Platforms

- ✅ TikTok
- ✅ Instagram  
- ✅ Twitter/X
- ✅ Facebook
- ✅ YouTube
- ✅ LinkedIn

## 🚨 Error Handling

The system includes comprehensive error handling for:
- Invalid URLs
- Network failures
- API rate limits
- Malformed social media posts
- Missing content

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- Check the logs for detailed error information
- Ensure all API keys are valid and have sufficient credits
- Verify the social media URL is publicly accessible
- Review the supported platforms list

## 🔄 Updates

- Check for Agno framework updates: `pip install -U agno`
- Monitor Bright Data API changes
- Keep model versions updated in configuration

---

**Note**: This system is designed for educational and research purposes. Always respect platform terms of service and rate limits.
